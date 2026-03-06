import streamlit as st
import pickle

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

st.title("Spam Detection App")

msg = st.text_input("Enter a message")

if st.button("Predict"):
    msg_vector = vectorizer.transform([msg])
    result = model.predict(msg_vector)

    st.write("Prediction value:", result[0])   # DEBUG


    if result[0] == 1:
        st.write("Spam Message 🚫")
    else:
        st.write("Not Spam ✅")
