import streamlit as st
from datetime import datetime

# ----- DESIGN -----
st.set_page_config(page_title="Saudi SuperApp", layout="wide", initial_sidebar_state="collapsed")
PRIMARY = "#009966"
BG = "#f7f8fa"
CARD = "#fff"

st.markdown(
    f"""
    <style>
        body, .main, .block-container {{
            background: {BG} !important;
        }}
        .wechat-card {{
            background: {CARD};
            border-radius: 18px;
            padding: 22px 18px 18px 18px;
            margin-bottom: 18px;
            box-shadow: 0 2px 10px #e2e5ea44;
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
        .app-link {{
            text-decoration:none !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----- APP STATE -----
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
if "profile_name" not in st.session_state:
    st.session_state["profile_name"] = "Ahmed"
if "profile_mobile" not in st.session_state:
    st.session_state["profile_mobile"] = "+9665xxxxxxx"

# ----- SERVICES -----
services = [
    {"name": "Chat & Social", "icon": "💬", "nav": "chat"},
    {"name": "Food & Delivery", "icon": "🍔", "nav": "food"},
    {"name": "Transport", "icon": "🚗", "nav": "rides"},
    {"name": "Banks", "icon": "🏦", "nav": "banks"},
    {"name": "Shopping", "icon": "🛍️", "nav": "shopping"},
    {"name": "Government", "icon": "🏛️", "nav": "gov"},
    {"name": "Recharge", "icon": "📱", "nav": "recharge"},
    {"name": "Bills", "icon": "🧾", "nav": "bills"},
    {"name": "Wallet", "icon": "💳", "nav": "wallet"},
    {"name": "Rewards", "icon": "🎁", "nav": "rewards"},
]

# ----- BOTTOM NAV -----
def bottom_nav():
    nav_labels = ["Home", "Chat", "Discover", "Wallet", "Profile"]
    nav_icons  = ["🏠",   "💬",  "🌐",       "💳",    "👤"]
    nav_keys   = ["home","chat","discover","wallet","profile"]
    cols = st.columns(5)
    for i, (lbl, icon, key) in enumerate(zip(nav_labels, nav_icons, nav_keys)):
        active = st.session_state["nav"] == key
        btn = cols[i].button(f"{icon}\n{lbl}", key=f"nav_{key}", use_container_width=True)
        if btn:
            st.session_state["nav"] = key
        if active:
            cols[i].markdown(f"<div style='height:3px;background:{PRIMARY};border-radius:2px;'></div>", unsafe_allow_html=True)
        else:
            cols[i].markdown(f"<div style='height:3px;'></div>", unsafe_allow_html=True)

# ----- HOME -----
if st.session_state["nav"] == "home":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:{PRIMARY};font-weight:700;margin-bottom:12px;'>🇸🇦 Saudi SuperApp</h2>", unsafe_allow_html=True)
    st.markdown(f"<b>Welcome, {st.session_state['profile_name']}!</b>")
    st.markdown(f"<span style='color:#444;font-size:18px;'>Balance:</span> <b style='color:{PRIMARY};font-size:22px'>{st.session_state['wallet_balance']:,} SAR</b>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.markdown("<b style='font-size:17px;'>Saudi Services & Apps</b><br>", unsafe_allow_html=True)
    ncols = 4
    cols = st.columns(ncols)
    for i, service in enumerate(services):
        with cols[i % ncols]:
            if st.button(f"{service['icon']}<br>{service['name']}", key=f"grid_{service['nav']}", help=f"Open {service['name']}", use_container_width=True):
                st.session_state["nav"] = service["nav"]
    st.markdown('</div>', unsafe_allow_html=True)

# ----- CHAT & SOCIAL -----
elif st.session_state["nav"] == "chat":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("💬 Chat & Social Apps")
    st.markdown("**Type a username or phone:**")
    username = st.text_input("Snap/Insta/X Username or Phone", key="user_social", placeholder="@username or +966...")
    st.markdown("**Quick links to social apps:**")
    social_apps = [
        {"name": "WhatsApp", "url": "https://wa.me/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"},
        {"name": "Snapchat", "url": "https://www.snapchat.com/add/", "logo": "https://upload.wikimedia.org/wikipedia/en/a/ad/Snapchat_logo.svg"},
        {"name": "X (Twitter)", "url": "https://x.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg"},
        {"name": "Instagram", "url": "https://instagram.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"},
        {"name": "Facebook", "url": "https://facebook.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"},
        {"name": "TikTok", "url": "https://www.tiktok.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/09/TikTok_logo.svg"},
        {"name": "Telegram", "url": "https://t.me/", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg"},
    ]
    s_cols = st.columns(len(social_apps))
    for i, app in enumerate(social_apps):
        with s_cols[i]:
            st.image(app["logo"], width=40)
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    if username.strip():
        st.success(f"You searched for: {username} (simulate profile lookup or open the social app)")
    st.info("You can enter a username/phone or tap a social app to open it.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- FOOD & DELIVERY -----
elif st.session_state["nav"] == "food":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🍔 Order Food / Saudi Delivery Apps")
    rest = st.text_input("Restaurant or Cuisine", key="food_rest", placeholder="e.g. AlBaik, Shawarma, Pizza")
    st.markdown("**Or open a delivery app:**")
    food_apps = [
        {"name": "HungerStation", "url": "https://hungerstation.com/", "logo": "https://seeklogo.com/images/H/hungerstation-logo-ACEE84CA6E-seeklogo.com.png"},
        {"name": "Jahez", "url": "https://www.jahez.net/", "logo": "https://seeklogo.com/images/J/jahez-logo-7A9CBE733C-seeklogo.com.png"},
        {"name": "Mrsool", "url": "https://www.mrsool.co/", "logo": "https://www.mrsool.co/images/mrsool_logo.svg"},
        {"name": "Talabat", "url": "https://www.talabat.com/saudi", "logo": "https://cdn.talabat.com/images/talabat-logo.png"},
        {"name": "ToYou", "url": "https://www.toyou.io/", "logo": "https://www.toyou.io/images/logo.svg"},
        {"name": "Shgardi", "url": "https://www.shgardi.app/", "logo": "https://www.shgardi.app/assets/images/logo/logo.svg"},
        {"name": "Nana", "url": "https://nana.sa/", "logo": "https://nana.sa/favicon.ico"},
    ]
    appcols = st.columns(len(food_apps))
    for i, app in enumerate(food_apps):
        with appcols[i]:
            st.image(app["logo"], width=60)
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    st.info("Type a restaurant/cuisine or click a delivery app to order.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- TRANSPORT -----
elif st.session_state["nav"] == "rides":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🚗 Ride Hailing / Transport")
    st.markdown("**Top transport and mobility apps in Saudi:**")
    ride_apps = [
        {"name": "Uber", "url": "https://www.uber.com/sa/ar/", "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png"},
        {"name": "Careem", "url": "https://www.careem.com/", "logo": "https://logos-world.net/wp-content/uploads/2022/03/Careem-Logo.png"},
        {"name": "Kaiian", "url": "https://www.kaiian.com/", "logo": "https://www.kaiian.com/img/logo.png"},
        {"name": "Saptco", "url": "https://www.saptco.com.sa/", "logo": "https://www.saptco.com.sa/images/logo.png"},
    ]
    ridecols = st.columns(len(ride_apps))
    for i, app in enumerate(ride_apps):
        with ridecols[i]:
            st.image(app["logo"], width=60)
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    st.info("Tap a transport app to book or order a ride.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- BANKS & WALLETS -----
elif st.session_state["nav"] == "banks":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🏦 Saudi Banks & Digital Wallets")
    st.markdown("**Major Banks in Saudi Arabia:**")
    banks = [
        {"name": "Al Rajhi", "url": "https://www.alrajhibank.com.sa/", "logo": "https://www.alrajhibank.com.sa/content/dam/arbah/brand-assets/logo-en.svg"},
        {"name": "SNB", "url": "https://www.alahli.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Saudi_National_Bank_Logo.svg"},
        {"name": "Riyad Bank", "url": "https://www.riyadbank.com/", "logo": "https://www.riyadbank.com/en/personal-banking/pages/images/riyad-bank-logo.svg"},
        {"name": "SABB", "url": "https://www.sabb.com/", "logo": "https://www.sabb.com/sites/sabb/icons/favicon.svg"},
        {"name": "Alinma", "url": "https://www.alinma.com/", "logo": "https://www.alinma.com/wps/wcm/connect/alinma/AlinmaBank/en/images/logo.png"},
        {"name": "Bank AlJazira", "url": "https://www.baj.com.sa/", "logo": "https://www.baj.com.sa/images/baj-logo.png"},
        {"name": "ANB", "url": "https://www.anb.com.sa/", "logo": "https://www.anb.com.sa/SiteCollectionImages/logo.png"},
    ]
    bank_cols = st.columns(len(banks))
    for i, bank in enumerate(banks):
        with bank_cols[i]:
            st.image(bank["logo"], width=60)
            st.markdown(f"[{bank['name']}]({bank['url']})", unsafe_allow_html=True)
    st.markdown("**Digital Wallets:**")
    wallets = [
        {"name": "STC Pay", "url": "https://www.stcpay.com.sa/", "logo": "https://www.stcpay.com.sa/themes/custom/stcpay/favicon.ico"},
        {"name": "Apple Pay", "url": "https://www.apple.com/apple-pay/", "logo": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"},
        {"name": "mada Pay", "url": "https://www.madapay.sa/", "logo": "https://www.madapay.sa/content/dam/madapay/logo.png"},
        {"name": "UrPay", "url": "https://www.urpay.com.sa/", "logo": "https://www.urpay.com.sa/assets/images/logo.svg"},
        {"name": "Tabby", "url": "https://tabby.ai/", "logo": "https://tabby.ai/favicon.ico"},
    ]
    wallet_cols = st.columns(len(wallets))
    for i, w in enumerate(wallets):
        with wallet_cols[i]:
            st.image(w["logo"], width=36)
            st.markdown(f"[{w['name']}]({w['url']})", unsafe_allow_html=True)
    st.info("Tap a bank or wallet to open their site/app.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- SHOPPING -----
elif st.session_state["nav"] == "shopping":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🛍️ Shopping in Saudi")
    st.markdown("**Top Saudi Shopping Apps & Stores:**")
    shops = [
        {"name": "Noon", "url": "https://www.noon.com/saudi-en/", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Noon.com_Logo.png"},
        {"name": "Amazon.sa", "url": "https://www.amazon.sa/", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"},
        {"name": "Jarir", "url": "https://www.jarir.com/", "logo": "https://www.jarir.com/images/jarir-logo-en.svg"},
        {"name": "SOUQ", "url": "https://saudi.souq.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Souq.com_logo.svg"},
        {"name": "Namshi", "url": "https://en-sa.namshi.com/", "logo": "https://cdn.namshi.com/assets/namshi_logo.svg"},
        {"name": "Extra", "url": "https://www.extra.com/", "logo": "https://www.extra.com/on/demandware.static/Sites-extra-SA-Site/-/default/dw9cf3e236/images/extra-logo.svg"},
        {"name": "Ounass", "url": "https://www.ounass.sa/", "logo": "https://www.ounass.sa/on/demandware.static/Sites-Ounass-Site/-/default/dw6e9dcd81/images/logo.svg"},
    ]
    shop_cols = st.columns(len(shops))
    for i, shop in enumerate(shops):
        with shop_cols[i]:
            st.image(shop["logo"], width=60)
            st.markdown(f"[{shop['name']}]({shop['url']})", unsafe_allow_html=True)
    st.info("Tap a store to open their website or app.")
    st.markdown('</div>', unsafe_allow_html=True)

# ----- GOVERNMENT -----
elif st.session_state["nav"] == "gov":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🏛️ Government Services in Saudi")
    gov_apps = [
        {"name": "Absher", "url": "https://www.absher.sa/", "logo": "https://www.absher.sa/images/absher_logo.png"},
        {"name": "Tawakkalna", "url": "https://ta.s
