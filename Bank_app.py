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

# User Dashboard 
def dashboard():
    st.title("💰Dashboard")
    st.markdown("Welcome back, Michael")

    st.subheader("🔁 Make a Transaction")
    with st.form("transaction_form"):
        action = st.radio("Select action", ["Deposit", "Withdraw"], key="form_action")
        amount = st.number_input("Amount (₦)", min_value=0.0, step=1000.0, key="form_amount")
        submitted = st.form_submit_button("Submit Transaction")

        if submitted:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if amount <= 0:
                st.warning("Enter a valid amount.")
            elif action == "Deposit":
                st.session_state.balance += amount
                st.session_state.transactions.append({
                    "type": "Deposit",
                    "amount": amount,
                    "time": now
                })
                st.success(f"Deposited ₦{amount:,.2f}")
            elif action == "Withdraw":
                if amount > st.session_state.balance:
                    st.error("Insufficient funds!")
                else:
                    st.session_state.balance -= amount
                    st.session_state.transactions.append({
                        "type": "Withdraw",
                        "amount": amount,
                        "time": now
                    })
                    st.success(f"Withdrew ₦{amount:,.2f}")

    # Display Balance
    st.markdown(f"### 💼 Account Balance: ₦{st.session_state.balance:,.2f}")

    st.subheader("📜 Transaction History")
    if st.session_state.transactions:
        for txn in reversed(st.session_state.transactions):
            st.markdown(f"- {txn['time']} | {txn['type']} of ₦{txn['amount']:,.2f}")
    else:
        st.write("No transactions yet.")


if st.session_state.logged_in:
    dashboard()
else:
    login()