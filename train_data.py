import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# load data

data = pd.read_csv("spam.csv", encoding='latin-1')
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# encoding

le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])
nltk.download('stopwords')

# text preprocessing
def preprocess(text):
    text = text.lower()
    text = re.sub('[^a-z0-9]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)

data['message'] = data['message'].apply(preprocess)

# TRAIN AND TEST MODEL

tfidf = TfidfVectorizer(ngram_range=(1,2), max_features=5000)
X = tfidf.fit_transform(data['message'])
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y,random_state=42)

# LOGISTIC REGRESSION MODEL

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

# SAVE MODEL
pickle.dump(model, open("detect.pkl", "wb"))
pickle.dump(tfidf, open("vectorizer.pkl", "wb"))