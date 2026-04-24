# 📘 Question Difficulty Classifier

This project uses a fine-tuned BERT model to classify questions into three difficulty levels:

* Easy
* Medium
* Hard

---

## 🚀 Features

* BERT-based text classification using Hugging Face Transformers
* Takes question + subject + options as input
* Predicts difficulty level
* Deployed using Gradio on Hugging Face Spaces

---

## 🧠 Model Details

* Model: `bert-base-uncased`
* Fine-tuned for 3-class classification
* Dataset: BhashaBench-Krishi (English subset)

---

## 🌐 Live Demo

👉 https://huggingface.co/spaces/Chandana777/question-difficulty-classifier

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚠️ Note

Due to GitHub file size limitations, the trained model is **not included in this repository**.

👉 The model is hosted separately on Hugging Face and loaded during runtime.

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Transformers (Hugging Face)
* Gradio

---

## ▶️ Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
python app.py
```

---

## 🎯 Output

* Predicts difficulty level: Easy / Medium / Hard
* Can be extended for educational or assessment systems

---

## 📌 Future Improvements

* Add confidence scores
* Support multilingual inputs
* Improve dataset balance

---

## 📜 License

This project is for educational and research purposes.
