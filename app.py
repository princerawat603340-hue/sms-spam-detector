import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer 
import pickle
st.title("SMS Spam Detector")
st.header('This is a simple SMS spam detector app.The model is trained on a dataset with Fake Retailer Rewards & Gift Cards messages.Therefore it can detect them')
st.markdown('Other categories of spam detection will be added in future updates')
words = pickle.load(open('vectorizer.pkl', 'rb'))
def detector(input_sms):
    count = 0
    sms_words = input_sms.lower().split()

    for word in sms_words:
        if word in words.get_feature_names_out():
            count += 1

    percentage = (count / len(sms_words)) * 100

    if count >= 4:
        return 'Spam' ,percentage
    else:
        return 'Not Spam', percentage
with st.form("sms_form"):

    txt = st.text_area(
        "Enter Your SMS Here",
        placeholder="Type or paste your SMS message...",
        height=150
    )

    submit = st.form_submit_button(label="Submit")

    if submit:
        if txt.strip():
            result, percentage = detector(txt)

            if result == 'Spam':
                st.error(f"🚨 SPAM MESSAGE")
            else:
                st.success(f"✅ NOT SPAM MESSAGE")

            st.write(f"Spam Vocabulary Matching: **{percentage:.2f}%**")

            st.progress(min(percentage / 100, 1.0))

        else:
            st.warning("Please enter a message to classify.")