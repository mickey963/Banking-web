import streamlit as st
from datetime import datetime

# Session State Initialization 
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'balance' not in st.session_state:
    st.session_state.balance = 200_000
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# Sign in
def login():
    st.title("🏦 BOI Bank - Sign In")
    username = st.text_input("Username").lower()
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        if username == "michael" and password == "1234":
            st.session_state.logged_in = True
            st.success("Sign In successful!")
            st.rerun()
        else:
            st.error("Unknown User")
