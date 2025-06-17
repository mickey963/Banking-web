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