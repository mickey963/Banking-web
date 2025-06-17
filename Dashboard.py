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
                    st.success(f"Withdrew ₦{amount:,.2f}"