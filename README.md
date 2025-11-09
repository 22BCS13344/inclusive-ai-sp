# 🧠 InclusiveAI — AI-Powered Accessible Learning Platform  

> **Making education inclusive through AI-driven personalization and accessibility tools.**

---

## 📌 Overview  
**InclusiveAI** is a smart learning platform designed to enhance accessibility and inclusivity in education.  
It personalizes learning experiences for students with **cognitive, sensory, or physical disabilities** by intelligently adapting instructional materials and formats to maximize comprehension and engagement.

The system also includes a **Text-to-Speech feature** for visually impaired learners, enabling them to upload or type text and instantly hear it as clear audio.

---

## 🚀 Features  

- 🧩 **AI-Powered Personalization:**  
  Suggests the best learning format (text, audio, video, interactive) based on disability type.

- 🗣️ **Text-to-Speech Converter:**  
  Converts uploaded `.txt` files or typed text into speech for visually impaired users.

- 📊 **Custom Dataset Training:**  
  Trains on a dataset containing disability types and preferred learning content.

- 🌐 **Streamlit Web Interface:**  
  Simple, interactive UI for accessibility and ease of use.

---

## 🧰 Tech Stack  

| Component | Technology |
|------------|-------------|
| Frontend UI | Streamlit |
| Machine Learning | scikit-learn |
| Data Handling | pandas |
| Text-to-Speech | pyttsx3 |
| Programming Language | Python 3 |

---

## 🧩 Dataset  

A sample dataset named `learning_data.csv` is used for training.  
Example structure:

| disability_type | preferred_content |
|------------------|-------------------|
| visual | audio |
| hearing | captioned_video |
| dyslexia | audio |
| adhd | interactive |
| autism | game_based |

You can expand the dataset for better accuracy and model performance.

---

## 💡 How It Works  

1. User selects or enters their **disability type**.  
2. The ML model predicts the **most suitable learning format**.  
3. The app displays a recommendation like “Audio content is best suited.”  
4. Optionally, users can upload or type text to use the **Text-to-Speech** feature.

---

## 🧠 Future Enhancements  

- 🗂️ Larger, real-world dataset for improved accuracy.  
- 🌍 Multilingual text-to-speech support.  
- 🤖 AI-based adaptive quizzes and progress tracking.  
- 🧏‍♀️ Integration with speech recognition for hearing-impaired users.  
- 🎨 Modern UI improvements for accessibility and aesthetics.

---

## 🏁 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/InclusiveAI.git
cd InclusiveAI
