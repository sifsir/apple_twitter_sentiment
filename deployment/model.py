"""
GC7
Nama: Sifra Hilda Juliana Siregar
Batch: HCK-009
// model.py //
This programme was created for model prediction.
"""
import streamlit as st
import pandas as pd
import joblib
import json
import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
from function import text_preprocessing
from tensorflow.keras.models import load_model
import numpy as np

def run():
    st.title("Sentiment Prediction")
    input_text=st.text_input(label='Enter your text!')

    input_df = pd.DataFrame([input_text], columns=['text'])

    with open('stopwords.txt', 'r') as sw:
        stopwords = json.load(sw)
    stopwords = set(stopwords)
    stemmer = PorterStemmer()

    input_df['text_processed'] = input_df['text'].apply(lambda x: text_preprocessing(x, word_stemmer=stemmer, sw=stopwords))
    if st.button(label= "predict"):
        model = load_model("checkpoint2")
        pred = model.predict(input_df.text_processed)
        pred = np.argmax(pred, axis=1)
        if pred == 0:
            st.write('negative')
        elif pred == 1:
            st.write('neutral')
        else:
            st.write('positive')