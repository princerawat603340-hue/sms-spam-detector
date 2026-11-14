import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer 
import pickle
st.title("SMS Spam Classifier")
new_dataframe=pd.read_csv('new_dataframe')
words=CountVectorizer(max_features=400,stop_words='english')
def detector(input):
    count=0
    for character in  input :
        if character in words.get_feature_names_out():
            count+=1
            if count==5:
                return 'spam'
    return 'ham'
