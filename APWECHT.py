import streamlit as st

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
        .app-link {{
            text-decoration:none !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Session State for User Inputs ---
fields = [
    "alrajhi_user", "snb_user", "stcpay_phone", "snap_user", "insta_user",
    "wa_phone", "x_user", "jahez_phone", "mrsool_user", "hs_phone"
]
for f in fields:
    if f not in st.session_state:
        st.session_state[f] = ""

if "nav" not in st.session_state:
    st.session_state["nav"] = "wallet"

# ----- SERVICES -----
services = [
    {"name": "Wallet", "icon": "💳", "nav": "wallet"},
    {"name": "Food", "icon": "🍔", "nav": "food"},
    {"name": "Transport", "icon": "🚗", "nav": "rides"},
    {"name": "Social", "icon": "💬", "nav": "chat"},
    {"name": "Shopping", "icon": "🛍️", "nav": "shopping"},
    {"name": "Government", "icon": "🏛️", "nav": "gov"},
    {"name": "Bills", "icon": "🧾", "nav": "bills"},
    {"name": "Recharge", "icon": "📱", "nav": "recharge"},
]

def navbar():
    cols = st.columns(len(services))
    for i, service in enumerate(services):
        if cols[i].button(f"{service['icon']} {service['name']}", key=f"nav_{service['nav']}"):
            st.session_state["nav"] = service["nav"]

# ----- HEADER -----
st.markdown(f"<h2 style='color:{PRIMARY};font-weight:800'>🇸🇦 Saudi SuperApp</h2>", unsafe_allow_html=True)
st.write("Everything in one dashboard — fully personal for you.")

navbar()

# ----- PAGES -----
if st.session_state["nav"] == "wallet":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("💳 Wallet — Banks & Digital Wallets")
    st.markdown("**Major Banks in Saudi Arabia:**")
    banks = [
        {
            "name": "Al Rajhi",
            "url": "https://www.alrajhibank.com.sa/",
            "logo": "https://www.alrajhibank.com.sa/content/dam/arbah/brand-assets/logo-en.svg",
            "user_field": "alrajhi_user",
            "login_url": "https://www.alrajhibank.com.sa/wps/portal/alrajhibank/alarajhibank/!ut/p/z1/hY5LC4JAFEW_pQ_MfAVWR8QIqZzW5DEykmkTtQQK_vUeGiXkzJx3M9vYzUllEa6SxhI-jJATfpoWXs6pSwt9Jsynf8kODgLcsw74o6YZZyKyrINMPLNsXvL4T8Af6GBL-fAp7uGKxrNQGHJ5jAgSBcU0KFRkzpnH_gNZBcezYHAl5NwCKbLwGH6TYvRxzwWl7Lp13-8pjl_mnR5V8U3K6C8zY6H5b9Q!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/"
        },
        {
            "name": "SNB",
            "url": "https://www.alahli.com/",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Saudi_National_Bank_Logo.svg",
            "user_field": "snb_user",
            "login_url": "https://www.alahli.com/en-us/Pages/Login.aspx"
        },
        {
            "name": "STC Pay",
            "url": "https://www.stcpay.com.sa/",
            "logo": "https://www.stcpay.com.sa/themes/custom/stcpay/favicon.ico",
            "user_field": "stcpay_phone",
            "login_url": None
        },
        {
            "name": "Apple Pay",
            "url": "https://www.apple.com/apple-pay/",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
            "user_field": None,
            "login_url": None
        },
        {
            "name": "mada Pay",
            "url": "https://www.madapay.sa/",
            "logo": "https://www.madapay.sa/content/dam/madapay/logo.png",
            "user_field": None,
            "login_url": None
        },
    ]
    bank_cols = st.columns(len(banks))
    for i, bank in enumerate(banks):
        with bank_cols[i]:
            st.image(bank["logo"], width=60)
            if bank["user_field"] == "alrajhi_user":
                st.session_state["alrajhi_user"] = st.text_input("Al Rajhi username (optional)", st.session_state["alrajhi_user"], key="alrajhi_user")
                if st.session_state["alrajhi_user"]:
                    st.markdown(f"[🔗 Open Al Rajhi Login]( {bank['login_url']} )", unsafe_allow_html=True)
                    st.caption(f"Username: {st.session_state['alrajhi_user']}")
                else:
                    st.markdown(f"[Al Rajhi Main Site]({bank['url']})", unsafe_allow_html=True)
            elif bank["user_field"] == "snb_user":
                st.session_state["snb_user"] = st.text_input("SNB username (optional)", st.session_state["snb_user"], key="snb_user")
                if st.session_state["snb_user"]:
                    st.markdown(f"[🔗 SNB Login]({bank['login_url']})", unsafe_allow_html=True)
                    st.caption(f"Username: {st.session_state['snb_user']}")
                else:
                    st.markdown(f"[SNB Main Site]({bank['url']})", unsafe_allow_html=True)
            elif bank["user_field"] == "stcpay_phone":
                st.session_state["stcpay_phone"] = st.text_input("STC Pay phone for transfers", st.session_state["stcpay_phone"], key="stcpay_phone")
                if st.session_state["stcpay_phone"]:
                    st.markdown(f"Your STC Pay for friends: **{st.session_state['stcpay_phone']}**")
                st.markdown(f"[STC Pay App]({bank['url']})", unsafe_allow_html=True)
            else:
                st.markdown(f"[{bank['name']}]({bank['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "food":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🍔 Food — Restaurants & Delivery Apps")
    st.markdown("**Delivery Apps:**")
    food_apps = [
        {
            "name": "Jahez",
            "url": "https://www.jahez.net/",
            "logo": "https://seeklogo.com/images/J/jahez-logo-7A9CBE733C-seeklogo.com.png",
            "phone_field": "jahez_phone"
        },
        {
            "name": "HungerStation",
            "url": "https://hungerstation.com/",
            "logo": "https://seeklogo.com/images/H/hungerstation-logo-ACEE84CA6E-seeklogo.com.png",
            "phone_field": "hs_phone"
        },
        {
            "name": "Mrsool",
            "url": "https://www.mrsool.co/",
            "logo": "https://www.mrsool.co/images/mrsool_logo.svg",
            "user_field": "mrsool_user"
        },
        {
            "name": "Talabat",
            "url": "https://www.talabat.com/saudi",
            "logo": "https://cdn.talabat.com/images/talabat-logo.png",
            "phone_field": None
        },
        {
            "name": "ToYou",
            "url": "https://www.toyou.io/",
            "logo": "https://www.toyou.io/images/logo.svg",
            "phone_field": None
        },
    ]
    appcols = st.columns(len(food_apps))
    for i, app in enumerate(food_apps):
        with appcols[i]:
            st.image(app["logo"], width=60)
            if "phone_field" in app and app["phone_field"]:
                key = app["phone_field"]
                st.session_state[key] = st.text_input(f"{app['name']} phone (optional)", st.session_state[key], key=key)
                if st.session_state[key]:
                    st.markdown(f"Your {app['name']} phone: **{st.session_state[key]}**")
            elif "user_field" in app and app["user_field"]:
                key = app["user_field"]
                st.session_state[key] = st.text_input(f"{app['name']} username (optional)", st.session_state[key], key=key)
                if st.session_state[key]:
                    st.markdown(f"Your {app['name']} username: **{st.session_state[key]}**")
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    st.markdown("**Top Restaurants:**")
    rests = [
        {"name": "AlBaik", "url": "https://www.albaik.com/", "logo": "https://www.albaik.com/Content/images/albaik-logo.svg"},
        {"name": "Herfy", "url": "https://herfy.com/", "logo": ""},
        {"name": "Kudu", "url": "https://www.kudu.com.sa/", "logo": ""},
    ]
    rest_cols = st.columns(len(rests))
    for i, r in enumerate(rests):
        with rest_cols[i]:
            if r["logo"]: st.image(r["logo"], width=50)
            st.markdown(f"[{r['name']}]({r['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "rides":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🚗 Transport & Ride Apps")
    ride_apps = [
        {"name": "Uber", "url": "https://www.uber.com/sa/ar/", "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png"},
        {"name": "Careem", "url": "https://www.careem.com/", "logo": "https://logos-world.net/wp-content/uploads/2022/03/Careem-Logo.png"},
        {"name": "Kaiian", "url": "https://www.kaiian.com/", "logo": "https://www.kaiian.com/img/logo.png"},
    ]
    ridecols = st.columns(len(ride_apps))
    for i, app in enumerate(ride_apps):
        with ridecols[i]:
            st.image(app["logo"], width=60)
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "chat":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("💬 Social Apps & Chat (Personalized)")
    # WhatsApp link
    st.session_state["wa_phone"] = st.text_input("WhatsApp Phone (ex: 9665xxxxxxx)", st.session_state["wa_phone"], key="wa_phone")
    if st.session_state["wa_phone"]:
        wa_url = f"https://wa.me/{st.session_state['wa_phone']}"
    else:
        wa_url = "https://wa.me/"
    # Snapchat
    st.session_state["snap_user"] = st.text_input("Snapchat username", st.session_state["snap_user"], key="snap_user")
    if st.session_state["snap_user"]:
        snap_url = f"https://www.snapchat.com/add/{st.session_state['snap_user']}"
    else:
        snap_url = "https://www.snapchat.com/"
    # Instagram
    st.session_state["insta_user"] = st.text_input("Instagram username", st.session_state["insta_user"], key="insta_user")
    if st.session_state["insta_user"]:
        insta_url = f"https://instagram.com/{st.session_state['insta_user']}"
    else:
        insta_url = "https://instagram.com/"
    # X (Twitter)
    st.session_state["x_user"] = st.text_input("X (Twitter) username", st.session_state["x_user"], key="x_user")
    if st.session_state["x_user"]:
        x_url = f"https://x.com/{st.session_state['x_user']}"
    else:
        x_url = "https://x.com/"
    social_apps = [
        {"name": "WhatsApp", "url": wa_url, "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"},
        {"name": "Snapchat", "url": snap_url, "logo": "https://upload.wikimedia.org/wikipedia/en/a/ad/Snapchat_logo.svg"},
        {"name": "Instagram", "url": insta_url, "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"},
        {"name": "X (Twitter)", "url": x_url, "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg"},
        {"name": "Telegram", "url": "https://t.me/", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg"},
    ]
    s_cols = st.columns(len(social_apps))
    for i, app in enumerate(social_apps):
        with s_cols[i]:
            st.image(app["logo"], width=40)
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "shopping":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🛍️ Shopping in Saudi")
    shops = [
        {"name": "Noon", "url": "https://www.noon.com/saudi-en/", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Noon.com_Logo.png"},
        {"name": "Amazon.sa", "url": "https://www.amazon.sa/", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"},
        {"name": "Jarir", "url": "https://www.jarir.com/", "logo": "https://www.jarir.com/images/jarir-logo-en.svg"},
        {"name": "Namshi", "url": "https://en-sa.namshi.com/", "logo": "https://cdn.namshi.com/assets/namshi_logo.svg"},
    ]
    shop_cols = st.columns(len(shops))
    for i, shop in enumerate(shops):
        with shop_cols[i]:
            st.image(shop["logo"], width=60)
            st.markdown(f"[{shop['name']}]({shop['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "gov":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🏛️ Government Services in Saudi")
    gov_apps = [
        {"name": "Absher", "url": "https://www.absher.sa/", "logo": "https://www.absher.sa/images/absher_logo.png"},
        {"name": "Tawakkalna", "url": "https://ta.sdaia.gov.sa/", "logo": "https://ta.sdaia.gov.sa/favicon.ico"},
        {"name": "Najm", "url": "https://www.najm.sa/", "logo": "https://www.najm.sa/assets/images/logo.svg"},
        {"name": "Sehhaty", "url": "https://www.sehhaty.sa/", "logo": "https://www.sehhaty.sa/favicon.ico"},
    ]
    gov_cols = st.columns(len(gov_apps))
    for i, app in enumerate(gov_apps):
        with gov_cols[i]:
            st.image(app["logo"], width=60)
            st.markdown(f"[{app['name']}]({app['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "bills":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("🧾 Pay Bills")
    billers = [
        {"name": "Electricity", "url": "https://www.se.com.sa/"},
        {"name": "Water", "url": "https://www.nwc.com.sa/"},
        {"name": "Mobily", "url": "https://www.mobily.com.sa/"},
        {"name": "Internet", "url": "https://www.stc.com.sa/"},
    ]
    b_cols = st.columns(len(billers))
    for i, b in enumerate(billers):
        with b_cols[i]:
            st.markdown(f"[{b['name']}]({b['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state["nav"] == "recharge":
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader("📱 Mobile Recharge")
    telcos = [
        {"name": "STC", "url": "https://my.stc.com.sa/"},
        {"name": "Mobily", "url": "https://shop.mobily.com.sa/"},
        {"name": "Zain", "url": "https://www.sa.zain.com/"},
    ]
    t_cols = st.columns(len(telcos))
    for i, t in enumerate(telcos):
        with t_cols[i]:
            st.markdown(f"[{t['name']}]({t['url']})", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
