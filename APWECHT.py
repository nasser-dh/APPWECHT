import streamlit as st

# WeChat-style: soft almost-white background, blue accents, round cards
BG = "#f6f8fa"         # Light, almost white (WeChat feel)
PRIMARY = "#1890ff"    # WeChat’s accent blue (a bit lighter and fresh)
CARD = "#fff"          # Pure white cards

st.set_page_config(page_title="Wallet", layout="centered")

st.markdown(
    f"""
    <style>
        .main {{
            background-color: {BG};
        }}
        .wallet-card {{
            background: {CARD};
            border-radius: 18px;
            padding: 26px 22px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px #e7eaf3cc;
        }}
        .action-btn {{
            background: {PRIMARY};
            color: #fff !important;
            border: none;
            border-radius: 14px;
            padding: 16px 0;
            font-size: 16px;
            font-weight: bold;
            width: 100%;
            margin-bottom: 12px;
        }}
        .balance-label {{
            color: #666;
            font-size: 14px;
            margin-bottom: 3px;
        }}
        .balance-value {{
            color: {PRIMARY};
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 18px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Card for Balance
st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
st.markdown('<div class="balance-label">Available Balance</div>', unsafe_allow_html=True)
st.markdown('<div class="balance-value">3,280 SAR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Action Buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<button class="action-btn">Send</button>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<button class="action-btn">Pay</button>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<button class="action-btn">Top Up</button>', unsafe_allow_html=True)

# Recent Transactions
st.markdown('<br>', unsafe_allow_html=True)
st.markdown("### Recent Transactions")
for name, typ, amt, dt in [
    ("Zaid", "Send Money", "-50", "1 min ago"),
    ("Mobily", "Bill Paid", "-115", "2 hr ago"),
    ("Ahmad", "Received Money", "+200", "Today"),
]:
    st.markdown(
        f'<div style="background:#fff;border-radius:13px;padding:10px 18px;margin-bottom:8px;box-shadow:0 1px 3px #e6e6e633;">'
        f'<b>{name}</b> <span style="color:#888;">{typ}</span> <span style="float:right;color:{PRIMARY};">{amt} SAR</span>'
        f'<br><span style="color:#bbb;font-size:13px;">{dt}</span></div>',
        unsafe_allow_html=True
    )
