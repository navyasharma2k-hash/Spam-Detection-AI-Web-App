# Spam-Detection-AI-Web-App
An AI-powered Spam Detection Web Application built using Machine Learning and Streamlit. The app classifies text messages as Spam 🚫 or Not Spam ✅ in real time using a trained machine learning model.  This project demonstrates Natural Language Processing (NLP) techniques combined with machine learning deployment in a user-friendly web interface.
Live Demo
Run locally using Streamlit:
python -m streamlit run app.py
Then open:
https://zbrrpsjjxcf5fae652upjn.streamlit.app/

Project Overview
Spam messages are a major problem in communication systems such as email, SMS, and social media. This project uses machine learning and text vectorization to automatically detect spam messages.
The workflow:
Preprocess text messages
Convert text to numerical features using TF-IDF Vectorization
Train a Machine Learning Classification Model
Save the trained model using Pickle
Deploy the model with Streamlit Web App

Project Architecture
Spam-Detection/
│
├── app.py                # Streamlit Web Application
├── model.pkl             # Trained Machine Learning Model
├── vectorizer.pkl        # TF-IDF Vectorizer
├── spam.csv              # Dataset
├── train_model.ipynb     # Model training notebook
└── README.md             # Project Documentation

Tech Stack
Programming Language
Python
Machine Learning
Scikit-learn
Natural Language Processing
TF-IDF Vectorization
Web Framework
Streamlit
Libraries
pandas
numpy
scikit-learn
pickle

Machine Learning Pipeline
1️⃣ Data Preprocessing
Remove special characters
Convert text to lowercase
Remove stopwords
Tokenization
2️⃣ Feature Extraction
Using TF-IDF Vectorization
Text → TF-IDF → Numerical Vector
3️⃣ Model Training
Common models used for spam detection:
Naive Bayes
Logistic Regression
Support Vector Machine
Example:
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train, y_train)
4️⃣ Model Serialization
Save trained model:
import pickle
pickle.dump(model, open("model.pkl","wb"))

Web Application Interface
The Streamlit app allows users to:
✔ Enter a message
✔ Click Predict
✔ View spam classification instantly

Example:

Input:
Free money claim your prize now

Output:
Spam Message 🚫

Application Preview
Spam Detection App
Enter a message:
[ Free money claim your prize now ]
[ Predict ]
Prediction value: 1
Spam Message 🚫

Example Predictions
| Message                         | Prediction |
| Win a free iPhone now           | Spam       |
| Congratulations you won lottery | Spam       |
| Let's meet tomorrow             | Not Spam   |
| Call me when you reach home     | Not Spam   |

