import streamlit as st
import pickle
import re
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from langdetect import detect
from deep_translator import GoogleTranslator

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))


st.set_page_config(page_title="AI Scam Detection", layout="wide")

st.markdown("""
<style>

/* Main App Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Sidebar Background */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #111827);
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    background-color: #1e293b !important;
    color: white !important;
}

/* Text Area */
textarea {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #334155 !important;
}

/* Buttons */
.stButton>button {
    background-color: #3b82f6;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
}

.stButton>button:hover {
    background-color: #2563eb;
    color: white;
}

/* Headers */
h1, h2, h3 {
    color: #f1f5f9;
}
/* Download Button */
.stDownloadButton>button {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 8px;
    padding: 10px 18px;
    border: 1px solid #334155;
}

.stDownloadButton>button:hover {
    background-color: #22c55e !important;
    color: white !important;
}



</style>
""", unsafe_allow_html=True)



# LOAD MODEL 

model = pickle.load(open("detect.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# SESSION STATE

if "history" not in st.session_state:
    st.session_state.history = []

# TEXT PREPROCESSING

def preprocess(text):
    text = text.lower()
    text = re.sub('[^a-z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]
    return " ".join(words)


# SCAM TYPE DETECTION

def predict_scam_type(msg):
    msg = msg.lower()

    if "bank" in msg or "account" in msg:
        return "Bank Fraud"
    elif "win" in msg or "prize" in msg:
        return "Lottery Scam"
    elif "upi" in msg or "pay" in msg:
        return "UPI Fraud"
    elif "click" in msg or "link" in msg:
        return "Phishing"
    else:
        return "General Spam"


#  MULTILANGUAGE PREDICTION

def multilingual_predict(msg):

    try:
        lang = detect(msg)
    except:
        lang = "en"

    if lang != "en":
        msg_en = GoogleTranslator(source='auto', target='en').translate(msg)
    else:
        msg_en = msg

    cleaned_msg = preprocess(msg_en)
    data = vectorizer.transform([cleaned_msg])

    result = model.predict(data)[0] 
    probability = model.predict_proba(data)[0][1]

    return result, probability, lang, msg_en


def keyword_override(msg, model_result, model_probability):

    scam_keywords = [
        "click", "urgent", "deactivate", "account",
        "activate", "refund", "otp", "verify",
        "bank", "lottery", "prize", "blocked",
        "suspended", "update", "limited",
        "offer", "winner", "congratulations"
    ]

    text = msg.lower()

    if any(word in text for word in scam_keywords):
        return 1, 0.95 
    else:
        return model_result, model_probability


# SIDEBAR NAVIGATION

menu = st.sidebar.selectbox("Navigation", ["User Panel", "Admin Dashboard"])

# USER PANEL

if menu == "User Panel":

    st.title("📩 AI Scam Message Detection System")

    msg = st.text_area("Enter Message")

    if st.button("Check Message"):

        if msg.strip() == "":
            st.warning("⚠ Please enter a message to detect")

        else:
            result, probability, detected_lang, msg_en = multilingual_predict(msg)
            final_result, final_probability = keyword_override(msg_en, result, probability)
            st.write(f"🌐 Detected Language: {detected_lang.upper()}")

        

            if final_result == 1:
                st.error("⚠ Scam Message Detected!")
                scam_type = predict_scam_type(msg)
                status = "Scam"
                st.write(f"### 🔎 Scam Probability: {round(probability * 100, 2)}%")
            else:
                st.success("✅ Safe Message")
                scam_type = "Not Scam"
                status = "Safe"

            st.write("### 🚨 Scam Type:", scam_type)
            

            # Saved Message History
            st.session_state.history.append({
                "Message": msg,
                "Prediction": status,
                "Scam Type": scam_type,
                
            })

# ADMIN 

if menu == "Admin Dashboard":

    st.title("📊 Admin Dashboard")

    if len(st.session_state.history) == 0:
        st.info("No Data Available Yet")

    else:
        df = pd.DataFrame(st.session_state.history)

        total = len(df)
        scam_count = len(df[df["Prediction"] == "Scam"])
        safe_count = len(df[df["Prediction"] == "Safe"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Messages Checked", total)
        col2.metric("Scam Detected", scam_count)
        col3.metric("Safe Messages", safe_count)

        st.subheader("📈 Prediction Chart")
        chart_data = df["Prediction"].value_counts()
        fig, ax = plt.subplots()

        colors = []

        for label in chart_data.index:
           if label == "Scam":
               colors.append("red")
           else:
               colors.append("green")

        ax.bar(chart_data.index, chart_data.values, color=colors)

        ax.set_title("Scam vs Safe Messages")
        ax.set_ylabel("Number of Messages")

        st.pyplot(fig)

        st.subheader("📄 Message History")
        st.dataframe(df)

        # Download CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "⬇ Download Report",
            csv,
            "scam_report.csv",
            "text/csv"
        )
