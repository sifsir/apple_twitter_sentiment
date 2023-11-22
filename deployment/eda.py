
"""
GC7
Nama: Sifra Hilda Juliana Siregar
Batch: HCK-009
// eda.py //
This programme was created for EDA deployment.
"""
import streamlit as st
import pandas as pd

# Function to run in app.py
def run():
    st.title("Explatoratory Data Analysis")

    df = pd.read_csv("apple-twitter-sentiment-texts.csv")

    # The first 10 data
    st.header("The First 10 Entry Data")
    st.table(df.head(10))

    # Text Length
    st.header("Average Text Length by Sentiment")
    st.image("avglength.png", caption="Figure 1")
    st.caption(""" This is a visualisation of the average text length by Sentiment).

    1. Negative: 91.062682
    2. Neutral: 98.446941
    3. Positive: 98.475524 """)

    # Sentiment Percentage
    st.header("Sentiment Percentage")
    st.image("sentimentpercentage.png", caption="Figure 2")
    st.caption(""" This is a visualisation of a pie chart representing the percentage of the different sentiments of tweets.

    1. Negative: 42.1%

    2. Neutral: 49.1%
               
    3. Positive: 8.77%.""")

    