import streamlit as st

# --- WeChat-style UI template ---
BG = "#f6f8fa"         # WeChat-like background
CARD = "#fff"          # Card background
PRIMARY = "#1890ff"    # WeChat blue

st.set_page_config(page_title="Wallet", layout="centered")

st.markdown(
    f"""
    <style>
        .main {{
            background-color: {BG};
        }}
        .wallet-card {{
            background: {CARD};
            border-radius: 16px;
            padding: 24px 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px #e7eaf322;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
# --- End WeChat-style template ---

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

# ---- Home Page ----
if menu == "Home":
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title("Welcome, Ahmed! 👋")
    st.subheader(f"Wallet Balance: {wallet_balance:,} SAR")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.button("Send Money")
    col2.button("QR Pay")
    col3.button("Bill Pay")
    col4.button("Top-Up")
    col5.button("Rewards")

    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.markdown("### Recent Transactions")
    for t in transactions:
        color = "green" if t['amount'] > 0 else "red"
        st.write(f"**{t['name']}** — {t['type']} : "
                 f"<span style='color:{color}'>{t['amount']} SAR</span> ({t['date']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.info(f"🏅 Rewards Points: {reward_points}")

# ---- Send Money ----
elif menu == "Send Money":
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title("Send Money")
    recipient = st.selectbox("Select Recipient", contacts)
    amount = st.number_input("Amount (SAR)", min_value=1, step=1)
    message = st.text_input("Optional message")
    if st.button("Send"):
        st.success(f"{amount} SAR sent to {recipient}!")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- QR Pay ----
elif menu == "QR Pay":
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title("QR Pay")
    st.write("🚧 Demo: QR Scan feature coming soon!")
    st.write("Show your QR or scan merchant QR to pay.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Bill Pay ----
elif menu == "Bill Pay":
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title("Bill Pay")
    biller = st.selectbox("Select Biller", ["Mobily", "STC", "Electricity"])
    bill_amount = st.number_input("Bill Amount (SAR)", min_value=1, step=1)
    if st.button("Pay Bill"):
        st.success(f"Bill of {bill_amount} SAR paid to {biller}!")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Rewards ----
elif menu == "Rewards":
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title("Rewards Center")
    st.metric("Current Points", reward_points)
    st.write("Earn more points by paying bills, sending money, and using QR Pay.")
    st.warning("Redeem feature coming soon!")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Profile ----
elif menu == "Profile":
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title("Profile")
    st.write("Name: Ahmed")
    st.write("Phone: +966 5xxxxxxx")
    st.write("Language: Arabic/English")
    st.write("KYC Status: Verified")
    st.write("For help, contact support@superwallet.sa")
    st.markdown('</div>', unsafe_allow_html=True)
