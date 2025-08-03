import streamlit as st

st.set_page_config(page_title="Saudi SuperApp (Secure MVP)", layout="wide")

# -------- STATE --------
if "connected" not in st.session_state:
    st.session_state["connected"] = {
        "bank": False,
        "food": False,
        "social": False,
        "delivery": False,
        "privacy": True, # True = hide details from others
        "requests": [],
        "approved": [],
    }
if "user_bank" not in st.session_state:
    st.session_state["user_bank"] = None
if "user_social" not in st.session_state:
    st.session_state["user_social"] = None
if "user_food" not in st.session_state:
    st.session_state["user_food"] = None
if "user_delivery" not in st.session_state:
    st.session_state["user_delivery"] = None
if "pending_request" not in st.session_state:
    st.session_state["pending_request"] = None

# ---------- HEADER ----------
st.markdown("""
    <h2 style='color:#009966;font-weight:800'>🇸🇦 Saudi SuperApp — Secure Prototype</h2>
    <span style='color:gray;font-size:16px'>All your accounts, all your apps — one private, secure dashboard.<br>Nothing is shared with contacts unless you approve!</span>
    <hr>
""", unsafe_allow_html=True)

# ---------- PRIVACY -----------
col_priv, col_stat = st.columns([2,1])
with col_priv:
    st.write("🔒 **Privacy Settings**")
    privacy = st.toggle("Hide my account details from others (default: ON)", value=st.session_state["connected"]["privacy"])
    st.session_state["connected"]["privacy"] = privacy

with col_stat:
    st.markdown("**Status:**")
    for service in ["bank", "food", "social", "delivery"]:
        connected = st.session_state["connected"][service]
        emoji = "✅" if connected else "❌"
        st.write(f"{emoji} {service.capitalize()}")

# ---------- ACCOUNT CONNECTION ----------
st.markdown("### 👤 Connect Your Accounts")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.subheader("🏦 Bank")
    if not st.session_state["connected"]["bank"]:
        bank = st.selectbox("Choose your Bank", ["--Select--","Al Rajhi","SNB","Riyad","SABB","Alinma"])
        user_id = st.text_input("Bank Username", key="bank_id")
        if st.button("Connect Bank"):
            if bank != "--Select--" and user_id:
                st.session_state["connected"]["bank"] = True
                st.session_state["user_bank"] = {"bank":bank,"id":user_id}
                st.success("Bank account connected!")
            else:
                st.error("Please select a bank and enter username")
    else:
        st.success(f"Connected: {st.session_state['user_bank']['bank']} (ID: {st.session_state['user_bank']['id']})")

with c2:
    st.subheader("🍔 Food & Delivery")
    if not st.session_state["connected"]["food"]:
        fav = st.text_input("Fav Restaurant (for demo)", key="food_id")
        if st.button("Connect Food", key="foodbtn"):
            if fav:
                st.session_state["connected"]["food"] = True
                st.session_state["user_food"] = fav
                st.success("Food account connected!")
            else:
                st.error("Please enter your favorite")
    else:
        st.success(f"Connected: {st.session_state['user_food']}")

with c3:
    st.subheader("💬 Social Media")
    if not st.session_state["connected"]["social"]:
        handle = st.text_input("Social Username (Snap/Insta)", key="soc_id")
        if st.button("Connect Social", key="socbtn"):
            if handle:
                st.session_state["connected"]["social"] = True
                st.session_state["user_social"] = handle
                st.success("Social account connected!")
            else:
                st.error("Please enter a username")
    else:
        st.success(f"Connected: {st.session_state['user_social']}")

with c4:
    st.subheader("🚗 Delivery App")
    if not st.session_state["connected"]["delivery"]:
        app = st.selectbox("Select Delivery", ["--Select--","HungerStation","Jahez","Mrsool"])
        if st.button("Connect Delivery", key="delbtn"):
            if app != "--Select--":
                st.session_state["connected"]["delivery"] = True
                st.session_state["user_delivery"] = app
                st.success("Delivery app connected!")
            else:
                st.error("Please choose a delivery app")
    else:
        st.success(f"Connected: {st.session_state['user_delivery']}")

st.divider()

# -------------- SIMULATED CONTACT REQUESTS (privacy system) --------------
st.markdown("### 🤝 Contact Requests")
st.write("If a contact wants to see your accounts, their request appears here. You must approve to share!")

if st.session_state["pending_request"] is None:
    name = st.text_input("Contact Name (simulate request)", key="cname")
    if st.button("Simulate Contact Request"):
        if name:
            st.session_state["pending_request"] = name
            st.session_state["connected"]["requests"].append(name)
            st.info(f"{name} wants access to your accounts!")
else:
    name = st.session_state["pending_request"]
    st.warning(f"{name} requests access to your connected accounts!")
    colA, colB = st.columns(2)
    with colA:
        if st.button("Approve"):
            st.session_state["connected"]["approved"].append(name)
            st.success(f"Approved {name}!")
            st.session_state["pending_request"] = None
    with colB:
        if st.button("Reject"):
            st.info("Request rejected.")
            st.session_state["pending_request"] = None

if st.session_state["connected"]["approved"]:
    st.success("Approved contacts: " + ", ".join(st.session_state["connected"]["approved"]))

# ------------- DASHBOARD: SEE YOUR LINKED SERVICES -------------
st.markdown("### 📱 My Apps & Accounts Dashboard")
for service, label, icon in [
    ("bank","Bank","🏦"),
    ("food","Food","🍔"),
    ("delivery","Delivery","🚗"),
    ("social","Social","💬"),
]:
    connected = st.session_state["connected"][service]
    info = None
    if connected:
        if service=="bank":
            info = f"**{st.session_state['user_bank']['bank']}** (ID: {st.session_state['user_bank']['id']})"
        elif service=="food":
            info = f"Fav: {st.session_state['user_food']}"
        elif service=="delivery":
            info = f"{st.session_state['user_delivery']}"
        elif service=="social":
            info = f"@{st.session_state['user_social']}"
    else:
        info = "*Not Connected*"

    # PRIVACY CHECK: hide info if privacy is ON and not you
    show = not st.session_state["connected"]["privacy"]
    if show or service=="social":  # Always show your own socials
        st.markdown(f"{icon} **{label}**: {info}")
    else:
        st.markdown(f"{icon} **{label}**: <span style='color:gray'>Hidden (private)</span>", unsafe_allow_html=True)

st.info("When privacy is ON, contacts cannot see your accounts unless you approve their request.")

# ----------------- SIMULATED INTEGRATION LINKS -----------------
st.markdown("### 🌟 Integrated Apps Quick Access")
cols = st.columns(4)
with cols[0]:
    if st.session_state["connected"]["bank"]:
        st.link_button("Go to Bank", "https://www.alrajhibank.com.sa/")
    else:
        st.button("Go to Bank", disabled=True)
with cols[1]:
    if st.session_state["connected"]["food"]:
        st.link_button("Order Food", "https://hungerstation.com/")
    else:
        st.button("Order Food", disabled=True)
with cols[2]:
    if st.session_state["connected"]["delivery"]:
        st.link_button("Book Delivery", "https://www.mrsool.co/")
    else:
        st.button("Book Delivery", disabled=True)
with cols[3]:
    if st.session_state["connected"]["social"]:
        st.link_button("Open Social", "https://www.snapchat.com/add/")
    else:
        st.button("Open Social", disabled=True)

st.caption("Links work only after you connect and approve. In production, you would authenticate and open your real account/app.")

