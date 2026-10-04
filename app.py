import streamlit as st

import streamlit as st
import joblib
import pandas as pd

model = joblib.load("./artifacts/classification_model.pkl")

st.title("Customer Classification")
st.write("Predict whether a customer is Bronze, Silver, or Gold.")

recence = st.number_input("Recence", min_value=0.0)
frequence = st.number_input("Frequence", min_value=0.0)
montant = st.number_input("Montant", min_value=0.0)

if st.button("Predict"):
    rfm = pd.DataFrame({
        "Recency":[recence],
        "Frequency":[frequence],
        "Monetary":[montant]
    })
    prediction = model.predict(rfm)

    st.success(f"Classe prédite : {prediction[0]}")