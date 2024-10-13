import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import json

#Initialize Firebase with credentials from Streamlit secrets
cred = credentials.Certificate(st.secrets["firebase_credentials"])

def fetch_scores():
    scores_ref = db.reference('users')  
    scores = scores_ref.get()
    print(scores)  
    return scores

st.title("High Scores")

scores = fetch_scores()
if scores:
    
    sorted_scores = sorted(
        [(value['name'], value['score']) for value in scores.values()],
        key=lambda x: x[1],  
        reverse=True  
    )
    score_data = pd.DataFrame(sorted_scores, columns=["Name", "Score"])

    st.table(score_data)

else:
    st.write("No scores available.")
