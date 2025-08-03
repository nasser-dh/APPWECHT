import streamlit as st

st.set_page_config(page_title="Saudi SuperApp", layout="wide")
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
        .locked-btn {{
            opacity: 0.4 !important;
            pointer-events: none;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- App State ----
if "connections" not in st.session_state:
    st.session_state["connections"] = {
        "bank": False,
        "food": False,
        "social": False,
        "delivery": False
    }
if "privacy" not in st.session_state:
    st.session_state["privacy"] = True

def connection_modal(service):
    st.session_state["show_modal"] = service

if "show_modal" not in st.session_state:
    st.session_state["show_modal"] = None

# ---- HEADER ----
st.markdown(f"<h2 style='color:{PRIMARY};font-weight:800'>🇸🇦 Saudi SuperApp</h2>", unsafe_allow_html=True)
st.write("All your Saudi accounts, food, banks, delivery, social — in one beautiful, private dashboard.")

# ---- Privacy ----
st.markdown("**🔒 Privacy**")
st.session_state["privacy"] = st.toggle(
    "Hide my account details from contacts (default: ON)",
    value=st.session_state["privacy"]
)

st.divider()

# ---- Home Card ----
st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
st.markdown(f"<b style='font-size:18px;'>Saudi Services & Apps</b><br>", unsafe_allow_html=True)

services = [
    {"name": "Bank", "icon": "🏦", "nav": "bank"},
    {"name": "Food", "icon": "🍔", "nav": "food"},
    {"name": "Social", "icon": "💬", "nav": "social"},
    {"name": "Delivery", "icon": "🚗", "nav": "delivery"},
    {"name": "Shopping", "icon": "🛍️", "nav": "shop"},
    {"name": "Government", "icon": "🏛️", "nav": "gov"},
    {"name": "Recharge", "icon": "📱", "nav": "recharge"},
    {"name": "Bills", "icon": "🧾", "nav": "bills"},
    {"name": "Wallet", "icon": "💳", "nav": "wallet"},
]
cols = st.columns(4)
for i, service in enumerate(services):
    nav = service["nav"]
    icon = service["icon"]
    label = service["name"]
    # Connection required for key services
    locked = nav in ["bank", "food", "social", "delivery"] and not st.session_state["connections"][nav]
    btn_style = "locked-btn" if locked else ""
    if locked:
        if cols[i % 4].button(f"{icon} {label}\n🔒 Connect", key=f"btn_{nav}"):
            st.session_state["show_modal"] = nav
    else:
        if cols[i % 4].button(f"{icon} {label}", key=f"btn_{nav}"):
            st.session_state["show_modal"] = nav
st.markdown('</div>', unsafe_allow_html=True)

# ---- Connection Modals ----
if st.session_state["show_modal"]:
    nav = st.session_state["show_modal"]
    with st.popover(f"Connect your {nav.capitalize()} Account", use_container_width=True):
        st.markdown(f"### {services[[s['nav'] for s in services].index(nav)]['icon']} Connect {nav.capitalize()}")
        if not st.session_state["connections"][nav]:
            if nav == "bank":
                bank = st.selectbox("Choose Bank", ["--Select--", "Al Rajhi", "SNB", "Riyad", "SABB", "Alinma"])
                user = st.text_input("Bank User Name")
                if st.button("Connect Bank"):
                    if bank != "--Select--" and user:
                        st.session_state["connections"]["bank"] = True
                        st.success("Connected!")
                        st.session_state["show_modal"] = None
                    else:
                        st.error("Select your bank and enter username.")
            elif nav == "food":
                fav = st.text_input("Favorite Restaurant or App")
                if st.button("Connect Food"):
                    if fav:
                        st.session_state["connections"]["food"] = True
                        st.success("Connected!")
                        st.session_state["show_modal"] = None
                    else:
                        st.error("Enter your favorite!")
            elif nav == "social":
                handle = st.text_input("Snap/Insta/X Username")
                if st.button("Connect Social"):
                    if handle:
                        st.session_state["connections"]["social"] = True
                        st.success("Connected!")
                        st.session_state["show_modal"] = None
                    else:
                        st.error("Enter username!")
            elif nav == "delivery":
                app = st.selectbox("Delivery App", ["--Select--", "HungerStation", "Jahez", "Mrsool"])
                if st.button("Connect Delivery"):
                    if app != "--Select--":
                        st.session_state["connections"]["delivery"] = True
                        st.success("Connected!")
                        st.session_state["show_modal"] = None
                    else:
                        st.error("Select delivery app!")
        else:
            st.success("Already connected!")
            if st.button("Disconnect"):
                st.session_state["connections"][nav] = False
                st.session_state["show_modal"] = None
        if st.button("Close", key="close_modal"):
            st.session_state["show_modal"] = None

# ---- Section Cards (Only if connected) ----
def section_card(title, links):
    st.markdown('<div class="wechat-card">', unsafe_allow_html=True)
    st.subheader(title)
    c = st.columns(len(links))
    for i, app in enumerate(links):
        with c[i]:
            st.image(app.get("logo", ""), width=48) if app.get("logo") else None
            # If the section is "locked" and privacy ON, show disabled
            if st.session_state["privacy"] and not st.session_state["connections"].get(app.get("nav", ""), True):
                st.button(f"{app['name']}", disabled=True)
            else:
                st.markdown(f"<a class='app-link' href='{app['url']}' target='_blank'>{app['name']}</a>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if all(st.session_state["connections"].values()):
    # All key services connected: show everything!
    # BANK
    section_card("🏦 My Banks & Wallets", [
        {"name": "Al Rajhi", "url": "https://www.alrajhibank.com.sa/", "logo": "https://www.alrajhibank.com.sa/content/dam/arbah/brand-assets/logo-en.svg"},
        {"name": "STC Pay", "url": "https://www.stcpay.com.sa/", "logo": "https://www.stcpay.com.sa/themes/custom/stcpay/favicon.ico"},
        {"name": "mada Pay", "url": "https://www.madapay.sa/", "logo": "https://www.madapay.sa/content/dam/madapay/logo.png"},
    ])
    # FOOD
    section_card("🍔 My Food Apps", [
        {"name": "HungerStation", "url": "https://hungerstation.com/", "logo": "https://seeklogo.com/images/H/hungerstation-logo-ACEE84CA6E-seeklogo.com.png"},
        {"name": "Jahez", "url": "https://www.jahez.net/", "logo": "https://seeklogo.com/images/J/jahez-logo-7A9CBE733C-seeklogo.com.png"},
        {"name": "Mrsool", "url": "https://www.mrsool.co/", "logo": "https://www.mrsool.co/images/mrsool_logo.svg"},
    ])
    # SOCIAL
    section_card("💬 My Social Apps", [
        {"name": "WhatsApp", "url": "https://wa.me/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"},
        {"name": "Snapchat", "url": "https://www.snapchat.com/add/", "logo": "https://upload.wikimedia.org/wikipedia/en/a/ad/Snapchat_logo.svg"},
        {"name": "Instagram", "url": "https://instagram.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"},
        {"name": "X (Twitter)", "url": "https://x.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg"},
    ])
    # DELIVERY
    section_card("🚗 My Delivery Apps", [
        {"name": "Uber", "url": "https://www.uber.com/sa/ar/", "logo": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png"},
        {"name": "Careem", "url": "https://www.careem.com/", "logo": "https://logos-world.net/wp-content/uploads/2022/03/Careem-Logo.png"},
    ])

# Shopping, Government, Recharge, Bills, Wallet are always open (no connect needed)
section_card("🛍️ Shopping", [
    {"name": "Noon", "url": "https://www.noon.com/saudi-en/", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Noon.com_Logo.png"},
    {"name": "Amazon.sa", "url": "https://www.amazon.sa/", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"},
    {"name": "Jarir", "url": "https://www.jarir.com/", "logo": "https://www.jarir.com/images/jarir-logo-en.svg"},
])
section_card("🏛️ Government", [
    {"name": "Absher", "url": "https://www.absher.sa/", "logo": "https://www.absher.sa/images/absher_logo.png"},
    {"name": "Tawakkalna", "url": "https://ta.sdaia.gov.sa/", "logo": "https://ta.sdaia.gov.sa/favicon.ico"},
    {"name": "Najm", "url": "https://www.najm.sa/", "logo": "https://www.najm.sa/assets/images/logo.svg"},
])
section_card("📱 Recharge", [
    {"name": "STC", "url": "https://my.stc.com.sa/", "logo": ""},
    {"name": "Mobily", "url": "https://shop.mobily.com.sa/", "logo": ""},
    {"name": "Zain", "url": "https://www.sa.zain.com/", "logo": ""},
])
section_card("🧾 Bills", [
    {"name": "Electricity", "url": "https://www.se.com.sa/", "logo": ""},
    {"name": "Water", "url": "https://www.nwc.com.sa/", "logo": ""},
])
section_card("💳 Wallet", [
    {"name": "Apple Pay", "url": "https://www.apple.com/apple-pay/", "logo": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"},
    {"name": "mada Pay", "url": "https://www.madapay.sa/", "logo": "https://www.madapay.sa/content/dam/madapay/logo.png"},
])
