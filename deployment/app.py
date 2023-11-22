"""
GC7
Nama: Sifra Hilda Juliana Siregar
Batch: HCK-009
// app.py //
This programme was created for the model deployment as the main interface.
"""

import streamlit as st
import eda
import model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediction'])

if page == 'Home Page':
    st.header('Hello Netizen!') 
    st.write('')
    st.write('Graded Challenge 7')
    st.write('Nama      : Sifra Siregar')
    st.write('Batch     : HCK-009')
    st.write('Objectives    : Create a model that can predict the sentiment value of a given text.')
    st.write('')
    st.caption('Please choose the menu on the sidebar!')
    st.write('')
    st.write('')
    with st.expander("Background"):
        st.caption("The 'Apple Twitter Sentiment Texts' dataset is a bunch of Twitter posts about what people think of Apple. It is full of different views that can help computers learn to understand how people feel about Apple's stuff. This info is great for seeing how much people like Apple and for tackling tricky language stuff like jokes and emojis online. It's really useful for companies to quickly see what their customers are saying about them.")

    with st.expander("Problem Statement"):
            st.caption('Aim to accurately analyze and interpret the sentiments expressed in tweets regarding Apple, to better understand public opinion and improve customer engagement strategies.')

    with st.expander("Conclusion"):
            st.caption("LSTM 2 model we used to figure out if tweets about Apple are positive, negative, or neutral is really good at picking up neutral tweets but gets a bit mixed up with the positive ones. It's great at learning from examples it's seen before, but it doesn't do as well when it sees new tweets it hasn't seen in training. We need to make some tweaks so it can get better at telling when tweets are actually saying something good.")
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()