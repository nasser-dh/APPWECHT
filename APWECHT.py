import streamlit as st
import random
import string
from datetime import datetime

# --- UI and Styling ---
BG = "#f6f8fa"
CARD = "#fff"
PRIMARY = "#1890ff"

st.set_page_config(page_title="Super Wallet", layout="centered")

st.markdown(
    f"""
    <style>
        .main {{background-color: {BG};}}
        .wallet-card {{
            background: {CARD};
            border-radius: 16px;
            padding: 24px 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 12px #e7eaf322;
        }}
        .icon-btn {{
            background: {PRIMARY};
            color: #fff !important;
            border: none;
            border-radius: 14px;
            padding: 12px 0;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
            margin-bottom: 12px;
        }}
        .chat-bubble-user {{
            background-color: #daf1ff;
            border-radius: 18px 18px 4px 18px;
            padding: 10px 16px;
            margin-bottom: 6px;
            align-self: flex-end;
            max-width: 80%;
        }}
        .chat-bubble-other {{
            background-color: #ededed;
            border-radius: 18px 18px 18px 4px;
            padding: 10px 16px;
            margin-bottom: 6px;
            align-self: flex-start;
            max-width: 80%;
        }}
        .chat-container {{
            display: flex;
            flex-direction: column;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Language Support ---
if "lang" not in st.session_state:
    st.session_state["lang"] = "English"

def _(en, ar):
    return en if st.session_state["lang"] == "English" else ar

if st.sidebar.button("🇸🇦 العربية" if st.session_state["lang"] == "English" else "🇺🇸 English"):
    st.session_state["lang"] = "Arabic" if st.session_state["lang"] == "English" else "English"

# --- Session State for Live Data ---
if "wallet_balance" not in st.session_state:
    st.session_state["wallet_balance"] = 3280
if "transactions" not in st.session_state:
    st.session_state["transactions"] = [
        {"name": "Zaid", "type": _("Send Money", "تحويل مالي"), "amount": -50, "date": _("1 min ago", "قبل دقيقة")},
        {"name": "Mobily", "type": _("Bill Paid", "فاتورة مدفوعة"), "amount": -115, "date": _("2 hr ago", "قبل ساعتين")},
        {"name": "Ahmad", "type": _("Received Money", "استلام مالي"), "amount": 200, "date": _("Today", "اليوم")},
    ]
if "reward_points" not in st.session_state:
    st.session_state["reward_points"] = 220

contacts = ["Ahmad", "Zaid", "Mona"]

# --- Mini-Apps/Services Section ---
mini_apps = {
    _("Food Delivery", "توصيل طعام"): "🍔",
    _("Shopping", "تسوق"): "🛍️",
    _("Transport", "مواصلات"): "🚗",
    _("Government Services", "خدمات حكومية"): "🏛️",
    _("Mobile Recharge", "شحن الجوال"): "📱",
    _("Chat", "محادثة"): "💬",
}

if "selected_mini_app" not in st.session_state:
    st.session_state["selected_mini_app"] = None

# --- Chat (WhatsApp-style) ---
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {"from": "other", "msg": _("Hi, how can I help you? 🤖", "مرحباً، كيف أستطيع مساعدتك؟ 🤖"), "time": "09:00"},
    ]
if "chat_input" not in st.session_state:
    st.session_state["chat_input"] = ""

# --- Sidebar Menu ---
menu = st.sidebar.radio(
    _("Go to", "انتقل إلى"),
    [
        _("Home", "الرئيسية"),
        _("Send Money", "إرسال"),
        _("Top Up", "شحن الرصيد"),
        _("QR Pay", "الدفع بالرمز"),
        _("Bill Pay", "سداد فاتورة"),
        _("Request Payment", "طلب دفعة"),
        _("Rewards", "مكافآت"),
        _("Profile", "الملف الشخصي"),
    ]
)

# --- Mini-App Handler ---
def show_mini_app():
    app = st.session_state["selected_mini_app"]
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.header(f"{mini_apps.get(app, '🚀')} {app}")
    # --- Chat Mini-App ---
    if app == _("Chat", "محادثة"):
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for chat in st.session_state["chat_history"]:
            bubble_class = "chat-bubble-user" if chat["from"] == "user" else "chat-bubble-other"
            st.markdown(
                f'<div class="{bubble_class}">{chat["msg"]}<span style="float:right;color:#aaa;font-size:11px;margin-left:10px;">{chat["time"]}</span></div>',
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)
        col_chat, col_send = st.columns([4, 1])
        with col_chat:
            chat_input = st.text_input(_("Type your message", "اكتب رسالتك هنا"), key="chat_input", label_visibility="collapsed")
        with col_send:
            if st.button("📤"):
                now = datetime.now().strftime("%H:%M")
                if chat_input.strip():
                    st.session_state["chat_history"].append({"from": "user", "msg": chat_input, "time": now})
                    st.session_state["chat_input"] = ""
                    # Simulate auto reply
                    st.session_state["chat_history"].append({
                        "from": "other",
                        "msg": _("Received! (This is a demo chat)", "تم الاستلام! (هذه محادثة تجريبية)"),
                        "time": now
                    })
        st.markdown(
            "<div style='height:20px;'></div>", unsafe_allow_html=True
        )
    # --- Food Mini-App ---
    elif app == _("Food Delivery", "توصيل طعام"):
        st.subheader(_("Order Food", "طلب طعام"))
        menu_items = [
            {"name": _("Burger", "برجر"), "price": 20},
            {"name": _("Pizza", "بيتزا"), "price": 30},
            {"name": _("Shawarma", "شاورما"), "price": 15},
            {"name": _("Salad", "سلطة"), "price": 10},
        ]
        food_choice = st.selectbox(_("Choose an item", "اختر صنفاً"), [f"{item['name']} - {item['price']} SAR" for item in menu_items])
        qty = st.number_input(_("Quantity", "الكمية"), min_value=1, max_value=10, step=1)
        if st.button(_("Order Now", "اطلب الآن")):
            item_name = food_choice.split(" - ")[0]
            price = int(food_choice.split(" - ")[1].split()[0])
            total = price * qty
            if total > st.session_state["wallet_balance"]:
                st.error(_("Insufficient balance!", "الرصيد غير كافٍ!"))
            else:
                st.session_state["wallet_balance"] -= total
                st.session_state["transactions"].insert(0, {
                    "name": item_name,
                    "type": _("Food Order", "طلب طعام"),
                    "amount": -total,
                    "date": _("Now", "الآن"),
                })
                st.session_state["reward_points"] += qty
                st.success(_(f"Ordered {qty} {item_name}(s) for {total} SAR!", f"تم طلب {qty} {item_name} بمبلغ {total} ر.س!"))
    # --- Transport Mini-App ---
    elif app == _("Transport", "مواصلات"):
        st.subheader(_("Choose a Transport App", "اختر تطبيق مواصلات"))
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("[![Uber](https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png)](https://www.uber.com/sa/ar/)", unsafe_allow_html=True)
            if st.button("Open Uber"):
                st.markdown('<meta http-equiv="refresh" content="0; url=https://www.uber.com/sa/ar/">', unsafe_allow_html=True)
        with col2:
            st.markdown("[![Careem](https://logos-world.net/wp-content/uploads/2022/03/Careem-Logo.png)](https://www.careem.com/)", unsafe_allow_html=True)
            if st.button("Open Careem"):
                st.markdown('<meta http-equiv="refresh" content="0; url=https://www.careem.com/">', unsafe_allow_html=True)
        st.info(_("Tap an icon above to open the app in your browser.", "اضغط على أيقونة لفتح التطبيق في المتصفح."))
    # --- Shopping, Gov, Mobile Recharge ---
    else:
        st.info(_("This mini-app is coming soon!", "هذا التطبيق المصغر قادم قريباً!"))
    if st.button(_("Back to Home", "عودة للرئيسية")):
        st.session_state["selected_mini_app"] = None
    st.markdown('</div>', unsafe_allow_html=True)

# ---- HOME ----
if menu == _("Home", "الرئيسية") and not st.session_state["selected_mini_app"]:
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Welcome, Ahmed! 👋", "مرحباً، أحمد! 👋"))
    st.subheader(f"{_('Wallet Balance', 'رصيد المحفظة')}: {st.session_state['wallet_balance']:,} SAR")
    st.markdown('</div>', unsafe_allow_html=True)

    # Action Buttons with Icons
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<button class="icon-btn">💸 {_("Send", "إرسال")}</button>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<button class="icon-btn">➕ {_("Top Up", "شحن")}</button>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<button class="icon-btn">🧾 {_("Pay", "سداد")}</button>', unsafe_allow_html=True)

    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.markdown(f"### { _('Recent Transactions', 'المعاملات الأخيرة') }")
    for t in st.session_state["transactions"]:
        color = "green" if t['amount'] > 0 else "red"
        st.write(
            f"**{t['name']}** — {t['type']} : "
            f"<span style='color:{color}'>{t['amount']} SAR</span> ({t['date']})",
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.info(f"🏅 {_('Rewards Points', 'نقاط المكافآت')}: {st.session_state['reward_points']}")

    # --- Mini-Apps Section ---
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.markdown("### 🚀 " + _("Services & Mini-Apps", "الخدمات والتطبيقات المصغرة"))
    cols = st.columns(len(mini_apps))
    for i, (app_name, emoji) in enumerate(mini_apps.items()):
        with cols[i]:
            if st.button(f"{emoji}\n{app_name}", key=f"mini_app_{i}"):
                st.session_state["selected_mini_app"] = app_name
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Show Mini-App if Selected ----
elif st.session_state["selected_mini_app"]:
    show_mini_app()

# ---- SEND MONEY ----
elif menu == _("Send Money", "إرسال"):
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Send Money", "إرسال الأموال"))
    recipient = st.selectbox(_("Select Recipient", "اختر المستلم"), contacts)
    amount = st.number_input(_("Amount (SAR)", "المبلغ (ر.س)"), min_value=1, step=1)
    message = st.text_input(_("Optional message", "رسالة اختيارية"))
    if st.button(_("Send", "إرسال")):
        if amount > st.session_state["wallet_balance"]:
            st.error(_("Insufficient balance!", "الرصيد غير كافٍ!"))
        else:
            st.session_state["wallet_balance"] -= amount
            st.session_state["transactions"].insert(0, {
                "name": recipient,
                "type": _("Send Money", "تحويل مالي"),
                "amount": -amount,
                "date": _("Now", "الآن"),
            })
            st.session_state["reward_points"] += 1
            st.success(_(f"{amount} SAR sent to {recipient}!", f"تم إرسال {amount} ر.س إلى {recipient}!"))
    st.markdown('</div>', unsafe_allow_html=True)

# ---- TOP UP ----
elif menu == _("Top Up", "شحن الرصيد"):
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Top Up", "شحن الرصيد"))
    topup = st.number_input(_("Amount to Add (SAR)", "المبلغ المراد شحنه (ر.س)"), min_value=1, step=1)
    if st.button(_("Add Funds", "شحن")):
        st.session_state["wallet_balance"] += topup
        st.session_state["transactions"].insert(0, {
            "name": _("Wallet Top Up", "شحن المحفظة"),
            "type": _("Top Up", "شحن"),
            "amount": topup,
            "date": _("Now", "الآن"),
        })
        st.success(_(f"Added {topup} SAR to your wallet.", f"تم شحن {topup} ر.س إلى محفظتك."))
    st.markdown('</div>', unsafe_allow_html=True)

# ---- QR PAY ----
elif menu == _("QR Pay", "الدفع بالرمز"):
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("QR Pay", "الدفع عبر الرمز"))
    st.write("🚧 " + _("Demo: QR Scan feature coming soon!", "عرض توضيحي: ميزة المسح قادمة قريباً!"))
    st.write(_("Show your QR or scan merchant QR to pay.", "اعرض رمزك أو امسح رمز التاجر للدفع."))
    st.markdown('</div>', unsafe_allow_html=True)

# ---- BILL PAY ----
elif menu == _("Bill Pay", "سداد فاتورة"):
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Bill Pay", "دفع الفواتير"))
    biller = st.selectbox(_("Select Biller", "اختر جهة الفاتورة"), ["Mobily", "STC", "Electricity"])
    bill_amount = st.number_input(_("Bill Amount (SAR)", "قيمة الفاتورة (ر.س)"), min_value=1, step=1)
    if st.button(_("Pay Bill", "سداد")):
        if bill_amount > st.session_state["wallet_balance"]:
            st.error(_("Insufficient balance!", "الرصيد غير كافٍ!"))
        else:
            st.session_state["wallet_balance"] -= bill_amount
            st.session_state["transactions"].insert(0, {
                "name": biller,
                "type": _("Bill Paid", "فاتورة مدفوعة"),
                "amount": -bill_amount,
                "date": _("Now", "الآن"),
            })
            st.session_state["reward_points"] += 2
            st.success(_(f"Bill of {bill_amount} SAR paid to {biller}!", f"تم سداد {bill_amount} ر.س إلى {biller}!"))
    st.markdown('</div>', unsafe_allow_html=True)

# ---- REQUEST PAYMENT (PAY LINK) ----
elif menu == _("Request Payment", "طلب دفعة"):
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Request Payment / Generate Pay Link", "طلب دفعة / إنشاء رابط دفع"))
    req_amount = st.number_input(_("Amount to Request (SAR)", "المبلغ المطلوب (ر.س)"), min_value=1, step=1, key="req_amt")
    req_desc = st.text_input(_("Description (optional)", "الوصف (اختياري)"), key="req_desc")
    if st.button(_("Generate Payment Link", "إنشاء رابط دفع")):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        pay_link = f"https://your-app-demo.streamlit.app/pay/{code}"
        st.success(_("Payment link generated!", "تم إنشاء رابط الدفع!"))
        st.code(pay_link)
        st.write(_("Copy and send this link to your friend.", "انسخ هذا الرابط وأرسله لصديقك."))
        st.info(_("This is a simulation. In production, this would process real payments.", "هذا عرض توضيحي فقط. في التطبيق الفعلي سيتم الدفع بشكل حقيقي."))
    st.markdown('</div>', unsafe_allow_html=True)

# ---- REWARDS ----
elif menu == _("Rewards", "مكافآت"):
    st.mark
