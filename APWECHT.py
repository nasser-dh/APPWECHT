import streamlit as st

st.set_page_config(page_title="Wallet", layout="centered")

# Colors for WeChat/clean style
BG = "#f6f8fa"         # almost white background
PRIMARY = "#1d4b8f"    # main blue
CARD = "#fff"          # card background

st.markdown(
    f"""
    <style>
        .main {{
            background-color: {BG};
        }}
        .wallet-card {{
            background: {CARD};
            border-radius: 22px;
            padding: 30px 24px 20px 24px;
            margin-bottom: 22px;
            box-shadow: 0 4px 16px #dde2ec38;
        }}
        .action-btn {{
            background: {PRIMARY};
            color: #fff !important;
            border: none;
            border-radius: 15px;
            padding: 16px 0;
            font-size: 17px;
            font-weight: 600;
            width: 100%;
            margin-bottom: 12px;
            transition: box-shadow .2s;
            box-shadow: 0 2px 8px #b5c7e644;
        }}
        .action-btn:hover {{
            box-shadow: 0 4px 20px #b5c7e699;
        }}
        .balance-label {{
            color: #888;
            font-size: 15px;
            margin-bottom: 4px;
        }}
        .balance-value {{
            color: {PRIMARY};
            font-size: 33px;
            font-weight: bold;
            margin-bottom: 18px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
st.markdown('<div class="balance-label">Available Balance</div>', unsafe_allow_html=True)
st.markdown('<div class="balance-value">3,280 SAR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<button class="action-btn">Send</button>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<button class="action-btn">Pay</button>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<button class="action-btn">Top Up</button>', unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)
st.markdown("### Recent Transactions")
for name, typ, amt, dt in [
    ("Zaid", "Send Money", "-50", "1 min ago"),
    ("Mobily", "Bill Paid", "-115", "2 hr ago"),
    ("Ahmad", "Received Money", "+200", "Today"),
]:
    st.markdown(
        f'<div style="background:#fff;border-radius:16px;padding:11px 18px;margin-bottom:10px;box-shadow:0 1px 6px #e6e6e644;">'
        f'<b>{name}</b> <span style="color:#888;">{typ}</span> <span style="float:right;color:{PRIMARY};">{amt} SAR</span>'
        f'<br><span style="color:#ccc;font-size:13px;">{dt}</span></div>',
        unsafe_allow_html=True
    )
