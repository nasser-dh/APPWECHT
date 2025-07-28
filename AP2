import streamlit as st

# Dummy data
wallet_balance = 3280
transactions = [
    {"name": "Zaid", "type": "Send Money", "amount": -50, "date": "1 min ago"},
    {"name": "Mobily", "type": "Bill Paid", "amount": -115, "date": "2 hr ago"},
    {"name": "Ahmad", "type": "Received Money", "amount": 200, "date": "Today"},
]
reward_points = 220
contacts = ["Ahmad", "Zaid", "Mona"]

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio("Go to", ["Home", "Send Money", "QR Pay", "Bill Pay", "Rewards", "Profile"])

if menu == "Home":
    st.title("Welcome, Ahmed! 👋")
    st.subheader(f"Wallet Balance: {wallet_balance:,} SAR")
    st.markdown("#### Quick Actions")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.button("Send Money")
    col2.button("QR Pay")
    col3.button("Bill Pay")
    col4.button("Top-Up")
    col5.button("Rewards")
    
    st.markdown("### Recent Transactions")
    for t in transactions:
        st.write(f"**{t['name']}** — {t['type']} : {t['amount']} SAR ({t['date']})")
    
    st.info(f"🏅 Rewards Points: {reward_points}")

elif menu == "Send Money":
    st.title("Send Money")
    recipient = st.selectbox("Select Recipient", contacts)
    amount = st.number_input("Amount (SAR)", min_value=1, step=1)
    message = st.text_input("Optional message")
    if st.button("Send"):
        st.success(f"{amount} SAR sent to {recipient}!")

elif menu == "QR Pay":
    st.title("QR Pay")
    st.write("🚧 Demo: QR Scan feature coming soon!")
    st.write("Show your QR or scan merchant QR to pay.")

elif menu == "Bill Pay":
    st.title("Bill Pay")
    biller = st.selectbox("Select Biller", ["Mobily", "STC", "Electricity"])
    bill_amount = st.number_input("Bill Amount (SAR)", min_value=1, step=1)
    if st.button("Pay Bill"):
        st.success(f"Bill of {bill_amount} SAR paid to {biller}!")

elif menu == "Rewards":
    st.title("Rewards Center")
    st.metric("Current Points", reward_points)
    st.write("Earn more points by paying bills, sending money, and using QR Pay.")
    st.warning("Redeem feature coming soon!")

elif menu == "Profile":
    st.title("Profile")
    st.write("Name: Ahmed")
    st.write("Phone: +966 5xxxxxxx")
    st.write("Language: Arabic/English")
    st.write("KYC Status: Verified")
    st.write("For help, contact support@superwallet.sa")
