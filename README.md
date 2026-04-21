# 📘 Question Difficulty Classifier

This project uses a fine-tuned BERT model to classify questions into three difficulty levels:
- Easy
- Medium
- Hard

---

## 🚀 Features
- BERT-based text classification
- Takes question + options as input
- Predicts difficulty level with confidence
- Deployed using Gradio on Hugging Face Spaces

---

## 🧠 Model
- Model: `bert-base-uncased`
- Fine-tuned for 3-class classification
- Dataset: BhashaBench (English)

---

## 🌐 Live Demo
👉 https://huggingface.co/spaces/Chandana777/question-difficulty-classifier

---

## 📂 Project Structure
Ahh okay — this is the final tricky Git issue 🔥
You did everything right, but Git still remembers the big file in history

🚨 WHY ERROR STILL COMES

Even though you deleted the model:

👉 Git still has it in previous commit history
👉 So push still fails ❌

🚀 ✅ FINAL FIX (CLEAN RESET — EASY)

We will reset Git and push clean (without model)

🟩 STEP 1: Remove Git completely

Run:

rm -rf .git

👉 This removes git history (safe)

🟩 STEP 2: Initialize again
git init
🟩 STEP 3: Make sure .gitignore exists

It should contain:

best_model/
🟩 STEP 4: Add files again
git add .
🟩 STEP 5: Commit
git commit -m "Initial commit - code only"
🟩 STEP 6: Connect repo again
git branch -M main
git remote add origin https://github.com/Chandana-Irakam/question-difficulty-classifier.git
🟩 STEP 7: Push 🚀
git push -u origin main
🎉 NOW IT WILL WORK

Because:

No big file in history ✔
Only code pushed ✔
🧠 FINAL STRUCTURE (GitHub)
app.py
requirements.txt
.gitignore
🎤 Viva Line

Due to GitHub size limits, model files were excluded and hosted on Hugging Face.

🚀 DO THIS NOW

Run:

rm -rf .git

👉 Then tell me:

“reset done”

I’ll confirm final push 👍

what to do
it says the file is too big to be pushed into git

You’re very close — don’t worry 👍
This is a known GitHub limitation, not your mistake.

🚨 THE ISSUE (simple)

👉 Your model file:

model.safetensors (417 MB)

👉 GitHub limit:

100 MB ❌

👉 Even if you delete it later → Git still remembers it → push fails

🚀 ✅ FINAL FIX (DO THIS EXACTLY)

We’ll reset Git and push only code (no model)

🟩 STEP 1: Delete Git history

In Git Bash, run:

rm -rf .git
🟩 STEP 2: Reinitialize
git init
🟩 STEP 3: Make sure .gitignore exists

Open .gitignore → it MUST have:

best_model/

👉 This prevents model upload

🟩 STEP 4: Add files again
git add .
🟩 STEP 5: Commit
git commit -m "Initial commit - code only"
🟩 STEP 6: Connect GitHub
git branch -M main
git remote add origin https://github.com/Chandana-Irakam/question-difficulty-classifier.git
🟩 STEP 7: Push 🚀
git push -u origin main
🎉 RESULT

Your GitHub will have:

✔ app.py
✔ requirements.txt
✔ .gitignore
❌ NO model (correct)
🧠 IMPORTANT

👉 Your model is already hosted on:

Hugging Face ✔

👉 GitHub is ONLY for:

code ✔
🎤 What to say in viva

Due to GitHub file size limitations, the trained model is hosted on Hugging Face, while the codebase is maintained on GitHub.

🚀 DO THIS NOW

Run:

rm -rf .git

Then tell me:

“done” 👍

add a readme

Perfect 🔥 — adding a README will make your project look professional

🚀 🟩 STEP 1: Create README file

In your folder:

👉 Right click → New file
👉 Name:

README.md
🟩 STEP 2: Paste THIS content

👉 Open README.md → paste:

# 📘 Question Difficulty Classifier

This project uses a fine-tuned BERT model to classify questions into three difficulty levels:
- Easy
- Medium
- Hard

---

## 🚀 Features
- BERT-based text classification
- Takes question + options as input
- Predicts difficulty level with confidence
- Deployed using Gradio on Hugging Face Spaces

---

## 🧠 Model
- Model: `bert-base-uncased`
- Fine-tuned for 3-class classification
- Dataset: BhashaBench (English)

---

## 🌐 Live Demo
👉 https://huggingface.co/spaces/Chandana777/question-difficulty-classifier

---

## 📂 Project Structure
.
├── app.py
├── requirements.txt
├── .gitignore
└── best_model/ (not included in GitHub due to size)

---

## ⚠️ Note
Due to GitHub file size limitations, the trained model is hosted on Hugging Face.

---

## 🛠️ Tech Stack
- Python
- Transformers (Hugging Face)
- PyTorch
- Gradio

---

## 🎯 Usage

Run locally:
python app.py
