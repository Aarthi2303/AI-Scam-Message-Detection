# 🛡️ AI Scam Message Detection System

👩🏼‍💻An intelligent multilingual scam detection system 💻built using Machine Learning and Streamlit.  
This project detects fraudulent or spam messages📱 in multiple languages and provides real-time prediction with an interactive admin dashboard📊.

---

## 📌 Project Overview

The AI Scam Detection System is designed to identify scam messages such as:

- Bank Fraud
- Phishing Attacks
- Lottery Scams
- UPI Fraud
- General Spam

The system supports multilingual input by automatically detecting the language and translating it into English before performing machine learning prediction.

---

## 🚀 Key Features

✅ Multilingual Message Detection  
✅ Automatic Language Detection  
✅ Auto Translation to English  
✅ Machine Learning Based Prediction  
✅ Keyword Override Safety Layer  
✅ Scam Probability Score  
✅ Scam Type Classification  
✅ Admin Dashboard with Analytics  
✅ Downloadable CSV Report  
✅ Session-based Message History  

---

## 🧠 System Architecture

### 1️⃣ User Input  
User enters a message in any language.

### 2️⃣ Language Detection  
The system detects language using `langdetect`.

### 3️⃣ Translation  
If the message is not English, it is translated using `googletrans`.

### 4️⃣ Text Preprocessing  
- Lowercasing  
- Removing special characters  
- Removing stopwords using NLTK  

### 5️⃣ Feature Extraction  
The cleaned text is transformed using a pre-trained `TF-IDF Vectorizer`.

### 6️⃣ Machine Learning Model  
A trained classification model predicts:
- Scam (1)
- Safe (0)

### 7️⃣ Keyword Override Layer  
Additional scam keywords are checked to improve accuracy.

### 8️⃣ Admin Dashboard  
Displays:
- Total messages
- Scam count
- Safe count
- Visualization chart
- Full message history
- CSV export option

---

## 🛠️ Technologies Used

| Technology    |       Purpose              |
|------------   |----------------------------|
| Python        |  Core Programming          |
| Streamlit     | Web Application Framework  |
| Scikit-learn  | Machine Learning Model     |
| TF-IDF        | Feature Extraction         |
| NLTK          | Text Preprocessing         |
| Langdetect    | Language Detection         |
| Googletrans   | Translation                |
| Pandas        | Data Handling              |
| Matplotlib    | Visualization              |

----------------------------------------------

## 📂 Project Structure
AI-Scam-Message-Detection/
│
├── app.py              # Main Streamlit Application
├── detect.pkl          # Trained ML Model
├── vectorizer.pkl      # TF-IDF Vectorizer
├── requirements.txt    # Required Python Libraries
├── README.md           # Project Documentation

## How to Run
    pip install -r requirements.txt
    streamlit run app.py

---

## 📊 Admin Dashboard Features

- Real-time Metrics
- Scam vs Safe Bar Chart
- Message History Table
- CSV Report Download
- Clean UI with Custom Styling

---

## 🔍 Example Scam Messages

- "Your bank account has been suspended. Click here to verify."
- "Congratulations! You have won ₹50,000."
- "आपका बैंक खाता बंद कर दिया गया है। तुरंत सत्यापित करें।"
- "Tu cuenta bancaria está bloqueada. Verifícala ahora."
- ¿Has terminado el trabajo?
- உங்கள் வங்கி கணக்கு முடக்கப்பட்டுள்ளது. உடனே சரிபார்க்கவும்.
- As-tu terminé le projet ?


---

## 🎯 Future Improvements

- Deep Learning (BERT / Transformer)
- Real-time SMS API Integration
- User Authentication System
- Database Storage (MySQL)
- Cloud Deployment
- Model Performance Metrics Display
- Confidence Threshold Tuning

---

## 📈 Use Case

This system can be used for:

- Banking Fraud Detection
- Email Filtering Systems
- SMS Scam Detection
- Cybersecurity Monitoring
- Financial Fraud Prevention

---

## 👩‍💻 Author
Aarthi A
MCA Student
Developed as a Machine Learning project.

---

