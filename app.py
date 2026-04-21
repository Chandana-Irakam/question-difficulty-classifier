import gradio as gr
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load your saved BERT model
model = AutoModelForSequenceClassification.from_pretrained("best_model")
tokenizer = AutoTokenizer.from_pretrained("best_model")

model.eval()

labels = ["Easy", "Medium", "Hard"]

def predict(question, subject, a, b, c, d):

    text = f"Question: {question} Domain: {subject} Options: {a} | {b} | {c} | {d}"

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=384
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs).item()
    confidence = probs[0][pred].item()

    return f"{labels[pred]} ({confidence*100:.2f}%)"


# UI
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Textbox(label="📝 Question"),
        gr.Textbox(label="📚 Subject"),
        gr.Textbox(label="Option A"),
        gr.Textbox(label="Option B"),
        gr.Textbox(label="Option C"),
        gr.Textbox(label="Option D"),
    ],
    outputs="text",
    title="📘 Question Difficulty Classifier",
    description="Classifies questions into Easy, Medium, or Hard"
)

demo.launch()