import os
import numpy as np
import torch

from datasets import load_dataset, ClassLabel
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback
)
from sklearn.metrics import accuracy_score, f1_score, classification_report
from torch.nn import CrossEntropyLoss
from huggingface_hub import login

from config import *

# 🔐 login via env variable
login(token=os.getenv("HF_TOKEN"))

# Load dataset
dataset = load_dataset("bharatgenai/BhashaBench-Krishi", "English")
full_data = dataset["test"]  # using as full dataset

label_feature = ClassLabel(names=LABEL_NAMES)

def encode(example):
    example["label"] = label_feature.str2int(example["question_level"])
    return example

full_data = full_data.map(encode)
full_data = full_data.cast_column("label", label_feature)

train_test = full_data.train_test_split(
    test_size=0.2,
    stratify_by_column="label",
    seed=SEED
)

train_data = train_test["train"]
test_data = train_test["test"]

def preprocess(example):
    return {
        "text": (
            example["question"] + " [SEP] " +
            example["subject_domain"] + " [SEP] " +
            example["option_a"] + " " +
            example["option_b"] + " " +
            example["option_c"] + " " +
            example["option_d"]
        )
    }

train_data = train_data.map(preprocess)
test_data = test_data.map(preprocess)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def tokenize(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH
    )

train_data = train_data.map(tokenize, batched=True)
test_data = test_data.map(tokenize, batched=True)

train_data.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])
test_data.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=NUM_LABELS
)

model.config.hidden_dropout_prob = DROPOUT
model.config.attention_probs_dropout_prob = DROPOUT

class_weights = torch.tensor(CLASS_WEIGHTS)

class WeightedTrainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        labels = inputs.get("labels")
        outputs = model(**inputs)
        logits = outputs.get("logits")

        loss_fct = CrossEntropyLoss(weight=class_weights.to(logits.device))
        loss = loss_fct(logits.view(-1, NUM_LABELS), labels.view(-1))

        return (loss, outputs) if return_outputs else loss


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)

    return {
        "accuracy": accuracy_score(labels, preds),
        "f1": f1_score(labels, preds, average="macro")
    }


training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    learning_rate=LEARNING_RATE,
    per_device_train_batch_size=TRAIN_BATCH_SIZE,
    per_device_eval_batch_size=EVAL_BATCH_SIZE,
    num_train_epochs=EPOCHS,
    weight_decay=WEIGHT_DECAY,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    logging_steps=50,
    max_grad_norm=1.0,
    report_to="none",
    seed=SEED
)

trainer = WeightedTrainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
)

trainer.train()

predictions = trainer.predict(test_data)

y_pred = np.argmax(predictions.predictions, axis=1)
y_true = predictions.label_ids

print("Final Accuracy:", accuracy_score(y_true, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, target_names=LABEL_NAMES))

trainer.save_model("best_model")
tokenizer.save_pretrained("best_model")
