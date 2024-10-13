import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd


firebase_credentials = {
    "type": st.secrets["type"],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"],
    "universe_domain": st.secrets["universe_domain"]
}



cred = credentials.Certificate(firebase_credentials)  
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://wakefield-scoreboard-default-rtdb.firebaseio.com/'  
})

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