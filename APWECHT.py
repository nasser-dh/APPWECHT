import streamlit as st
import random
import string
from datetime import datetime

# --------------- GLOBAL DESIGN AND STYLES ---------------
st.set_page_config(page_title="KSA SuperApp", layout="wide", initial_sidebar_state="collapsed")

PRIMARY = "#1aad19"   # WeChat green, can change to blue for Saudi
BG = "#f7f8fa"
CARD = "#fff"

st.markdown(
    f"""
    <style>
        body, .main, .block-container {{
            background: {BG} !important;
        }}
        .bottom-nav {{
            position: fixed;
            left: 0; right: 0; bottom: 0;
            background: #fff;
            border-top: 1px solid #eee;
            z-index: 9999;
            display: flex;
            justify-content: space-evenly;
            padding: 8px 0 4px 0;
        }}
        .nav-btn {{
            color: #999 !important;
            font-size: 22px;
            text-align: center;
            padding: 0 12px;
        }}
        .nav-btn.active {{
            color: {PRIMARY} !important;
            font-weight: bold;
        }}
        .wechat-card {{
            background: {CARD};
            border-radius: 18px;
            padding: 22px 18px 18px 18px;
            margin-bottom: 18px;
            box-shadow: 0 2px 10px #e2e5ea44;
        }}
        .service-btn {{
            background: #f4f4f4;
            border-radius: 15px;
            padding: 15px 7px 10px 7px;
            text-align: center;
            margin-bottom: 16px;
            cursor:pointer;
            border:none;
            font-size:15px;
        }}
        .service-btn:hover {{
            background: #e9f9ee;
        }}
        .chat-bubble-user {{
            background: #d0fdd8;
            border-radius: 18px 18px 6px 18px;
            padding: 10px 16px;
            margin-bottom: 6px;
            align-self: flex-end;
            max-width: 80%;
            font-size:15px;
        }}
        .chat-bubble-other {{
            background: #f1f1f1;
            border-radius: 18px 18px 18px 6px;
            padding: 10px 16px;
            margin-bottom: 6px;
            align-self: flex-start;
            max-width: 80%;
            font-size:15px;
        }}
        .chat-container {{
            display: flex;
            flex-direction: column;
            min-height: 420px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------- APP STATE (MULTI-PAGE MINI-APP STYLE) ---------------
if "nav" not in st.session_state:
    st.session_state["nav"] = "home"
if "wallet_balance" not in st.session_state:
    st.session_state["wallet_balance"] = 4150
if "transactions" not in st.session_state:
    st.session_state["transactions"] = [
        {"name": "Noon", "type": "Shopping", "amount": -140, "date": "Today"},
        {"name": "Uber", "type": "Ride", "amount": -36, "date": "Yesterday"},
        {"name": "Abdullah", "type": "Received", "amount": 200, "date": "Yesterday"},
    ]
if "reward_points" not in st.session_state:
    st.session_state["reward_points"] = 480
if "chat_list" not in st.session_state:
    st.session_state["chat_list"] = [
        {"contact": "Support Bot 🤖", "history": [
            {"from": "other", "msg": "Welcome to SuperApp KSA! How can we help you today?", "time": "09:10"},
        ]}
    ]
if "active_chat" not in st.session_state:
    st.session_state["active_chat"] = 0
if "profile_name" not in st.session_state:
    st.session_state["profile_name"] = "Ahmed"
if "profile_mobile" not in st.session_state:
    st.session_state["profile_mobile"] = "+9665xxxxxxx"

# --------------- MINI-APP DEFINITIONS ---------------
services = [
    {"name": "Chat", "icon": "💬", "nav": "chat"},
    {"name": "Wallet", "icon": "💳", "nav": "wallet"},
    {"name": "Food", "icon": "🍔", "nav": "food"},
    {"name": "Transport", "icon": "🚗", "nav": "rides"},
    {"name": "Recharge", "icon": "📱", "nav": "recharge"},
    {"name": "Bills", "icon": "🧾", "nav": "bills"},
    {"name": "Shopping", "icon": "🛍️", "nav": "shopping"},
    {"name": "Government", "icon": "🏛️", "nav": "gov"},
    {"name": "Rewards", "icon": "🎁", "nav": "rewards"},
]

nav_items = [
    {"nav": "home", "icon": "🏠", "label": "Home"},
    {"nav": "chat", "icon": "💬", "label": "Chat"},
    {"nav": "discover", "icon": "🌐", "label": "Discover"},
    {"nav": "wallet", "icon": "💳", "label": "Wallet"},
    {"nav": "profile", "icon": "👤", "label": "Profile"},
]
st.markdown('<div style="height:26px;"></div>', unsafe_allow_html=True)
bottom_nav_html = '<div class="bottom-nav">'
for item in nav_items:
    active = "active" if st.session_state["nav"] == item["nav"] else ""
    bottom_nav_html += f'<a href="#" class="nav-btn {active}" onclick="window.location.search=\'?nav={item["nav"]}\'">{item["icon"]}<br><span style="font-size:13px">{item["label"]}</span></a>'
bottom_nav_html += '</div>'
st.markdown(bottom_nav_html, unsafe_allow_html=True)

def goto(nav):
    st.session_state["nav"] = nav

params = st.experimental_get_query_params()
if "nav" in params and params["nav"][0] in [i["nav"] for i in nav_items]:
    st.session_state["nav"] = params["nav"][0]

# --------------- PAGE LOGIC (MINI-APPS AS PAGES) ---------------

# --- HOME: Mini-App Grid ---
if st.session_state["nav"] == "home":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{PRIMARY};font-weight:700;margin-bottom:12px;'>KSA SuperApp 🇸🇦</h2>", unsafe_allow_html=True)
    st.markdown(f"<b>Welcome, {st.session_state['profile_name']}!</b>")
    st.markdown(f"<span style='color:#444;font-size:18px;'>Balance:</span> <b style='color:{PRIMARY};font-size:22px'>{st.session_state['wallet_balance']:,} SAR</b>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.markdown("<b style='font-size:17px;'>Services & Mini-Apps</b><br>", unsafe_allow_html=True)
    ncols = 4
    cols = st.columns(ncols)
    for i, service in enumerate(services):
        with cols[i % ncols]:
            if st.button(f"{service['icon']}<br>{service['name']}", key=f"grid_{service['nav']}", help=f"Open {service['name']}", use_container_width=True):
                goto(service["nav"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- CHAT PAGE: WhatsApp-like with contacts ---
elif st.session_state["nav"] == "chat":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("💬 Chat")
    contacts = [chat["contact"] for chat in st.session_state["chat_list"]]
    contact = st.selectbox("Select Contact", contacts, index=st.session_state["active_chat"])
    idx = contacts.index(contact)
    st.session_state["active_chat"] = idx
    chat_hist = st.session_state["chat_list"][idx]["history"]
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in chat_hist:
        bubble_class = "chat-bubble-user" if chat["from"] == "user" else "chat-bubble-other"
        st.markdown(f'<div class="{bubble_class}">{chat["msg"]}<span style="float:right;color:#aaa;font-size:11px;margin-left:10px;">{chat["time"]}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    col_chat, col_send = st.columns([5, 1])
    with col_chat:
        chat_input = st.text_input("Type your message", key="chat_input", label_visibility="collapsed", placeholder="Write a message...")
    with col_send:
        if st.button("📤"):
            now = datetime.now().strftime("%H:%M")
            if chat_input.strip():
                chat_hist.append({"from": "user", "msg": chat_input, "time": now})
                st.session_state["chat_input"] = ""
                chat_hist.append({"from": "other", "msg": "Received! (demo reply)", "time": now})
    st.markdown('</div>', unsafe_allow_html=True)

# --- DISCOVER PAGE: List All Mini-Apps/Services ---
elif st.session_state["nav"] == "discover":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🌐 Discover Services")
    for service in services:
        if st.button(f"{service['icon']}  {service['name']}", key=f"discover_{service['nav']}", use_container_width=True):
            goto(service["nav"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- WALLET PAGE: Balance, Transaction Feed, Actions ---
elif st.session_state["nav"] == "wallet":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("💳 Wallet")
    st.markdown(f"<b>Available:</b> <span style='color:{PRIMARY};font-size:24px'>{st.session_state['wallet_balance']:,} SAR</span>", unsafe_allow_html=True)
    st.info("Use 'Top Up', 'Send', 'Bill', or pay in services. All updates instantly!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.markdown("#### Transactions")
    for t in st.session_state["transactions"][:8]:
        color = "green" if t['amount'] > 0 else "red"
        st.markdown(
            f"**{t['name']}** — {t['type']} : "
            f"<span style='color:{color}'>{t['amount']} SAR</span> ({t['date']})",
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Wallet actions (mini)
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Top Up"):
            goto("recharge")
    with col2:
        if st.button("💸 Send"):
            goto("chat")
    with col3:
        if st.button("🧾 Bills"):
            goto("bills")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOD MINI-APP ---
elif st.session_state["nav"] == "food":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🍔 Food Delivery")
    food_menu = [
        {"name": "Burger", "price": 22, "img": "🍔"},
        {"name": "Pizza", "price": 32, "img": "🍕"},
        {"name": "Shawarma", "price": 18, "img": "🌯"},
        {"name": "Salad", "price": 12, "img": "🥗"},
    ]
    food = st.selectbox("Choose food", [f"{f['img']} {f['name']} - {f['price']} SAR" for f in food_menu])
    qty = st.number_input("Quantity", min_value=1, max_value=10, value=1)
    if st.button("Order Now"):
        item = food.split(" - ")[0].strip()
        price = int(food.split(" - ")[1].split()[0])
        total = price * qty
        if total > st.session_state["wallet_balance"]:
            st.error("Insufficient balance!")
        else:
            st.session_state["wallet_balance"] -= total
            st.session_state["transactions"].insert(0, {
                "name": item,
                "type": "Food Order",
                "amount": -total,
                "date": "Now",
            })
            st.success(f"Ordered {qty} x {item} for {total} SAR!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TRANSPORT MINI-APP (Uber/Careem) ---
elif st.session_state["nav"] == "rides":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🚗 Ride Hailing")
    st.write("Choose a service to book your ride:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[![Uber](https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png)](https://www.uber.com/sa/ar/)", unsafe_allow_html=True)
        if st.button("Open Uber"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://www.uber.com/sa/ar/">', unsafe_allow_html=True)
    with col2:
        st.markdown("[![Careem](https://logos-world.net/wp-content/uploads/2022/03/Careem-Logo.png)](https://www.careem.com/)", unsafe_allow_html=True)
        if st.button("Open Careem"):
            st.markdown('<meta http-equiv="refresh" content="0; url=https://www.careem.com/">', unsafe_allow_html=True)
    st.info("Tap a logo above to open the app in your browser.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MOBILE RECHARGE MINI-APP ---
elif st.session_state["nav"] == "recharge":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("📱 Mobile Recharge")
    telco = st.selectbox("Select Operator", ["STC", "Mobily", "Zain"])
    amount = st.number_input("Amount (SAR)", min_value=10, max_value=500, step=10)
    if st.button("Recharge Now"):
        if amount > st.session_state["wallet_balance"]:
            st.error("Insufficient balance!")
        else:
            st.session_state["wallet_balance"] -= amount
            st.session_state["transactions"].insert(0, {
                "name": telco,
                "type": "Recharge",
                "amount": -amount,
                "date": "Now",
            })
            st.success(f"Recharged {amount} SAR for {telco}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- BILLS MINI-APP ---
elif st.session_state["nav"] == "bills":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🧾 Pay Bills")
    billers = ["Electricity", "Water", "Mobily", "STC", "Internet"]
    biller = st.selectbox("Biller", billers)
    amount = st.number_input("Amount (SAR)", min_value=1, max_value=10000, step=1)
    if st.button("Pay Bill"):
        if amount > st.session_state["wallet_balance"]:
            st.error("Insufficient balance!")
        else:
            st.session_state["wallet_balance"] -= amount
            st.session_state["transactions"].insert(0, {
                "name": biller,
                "type": "Bill Payment",
                "amount": -amount,
                "date": "Now",
            })
            st.success(f"Paid {amount} SAR to {biller}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SHOPPING MINI-APP (DEMO) ---
elif st.session_state["nav"] == "shopping":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🛍️ Shopping (Demo)")
    st.write("Shopping integration is coming soon. You can link Noon, Amazon.sa, Jarir, and more!")
    st.markdown('[Noon](https://www.noon.com/saudi-en/) | [Amazon.sa](https://www.amazon.sa/) | [Jarir](https://www.jarir.com/)', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- GOVERNMENT MINI-APP (DEMO) ---
elif st.session_state["nav"] == "gov":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🏛️ Government Services (Demo)")
    st.write("In the future, you’ll access Absher, Tawakkalna, and more here in one place!")
    st.markdown('[Absher](https://www.absher.sa/) | [Tawakkalna](https://ta.sdaia.gov.sa/)', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- REWARDS MINI-APP ---
elif st.session_state["nav"] == "rewards":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🎁 Rewards")
    st.markdown(f"🏅 Your Rewards Points: <b style='color:{PRIMARY}'>{st.session_state['reward_points']}</b>", unsafe_allow_html=True)
    st.info("Earn points by using any service! Soon you’ll redeem them for vouchers or discounts.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- PROFILE PAGE ---
elif st.session_state["nav"] == "profile":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("👤 My Profile")
    st.markdown(f"**Name:** {st.session_state['profile_name']}")
    st.markdown(f"**Mobile:** {st.session_state['profile_mobile']}")
    st.markdown("**Email:** user@email.com")
    if st.button("Edit Profile"):
        st.info("Profile editing coming soon!")
    st.markdown(" ")
    st.markdown("---")
    st.write("Contact Support | Privacy Policy | Version 1.0")
    st.markdown('</div>', unsafe_allow_html=True)
