import streamlit as st
import random
import string

# --- UI and Styling ---
BG = "#f6f8fa"
CARD = "#fff"
PRIMARY = "#1890ff"

st.set_page_config(page_title="Wallet", layout="centered")

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

# ---- HOME ----
if menu == _("Home", "الرئيسية"):
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
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Rewards Center", "مركز المكافآت"))
    st.metric(_("Current Points", "النقاط الحالية"), st.session_state["reward_points"])
    st.write(_("Earn more points by paying bills, sending money, and using QR Pay.", "اكسب المزيد من النقاط عبر دفع الفواتير والتحويل والدفع بالرمز."))
    st.warning(_("Redeem feature coming soon!", "ميزة الاسترداد قادمة قريباً!"))
    st.markdown('</div>', unsafe_allow_html=True)

# ---- PROFILE ----
elif menu == _("Profile", "الملف الشخصي"):
    st.markdown('<div class="wallet-card">', unsafe_allow_html=True)
    st.title(_("Profile", "الملف الشخصي"))
    st.write(f"{_('Name', 'الاسم')}: Ahmed")
    st.write(f"{_('Phone', 'رقم الجوال')}: +966 5xxxxxxx")
    st.write(f"{_('Language', 'اللغة')}: {st.session_state['lang']}")
    st.write(f"{_('KYC Status', 'التحقق')}: {_('Verified', 'موثق')}")
    st.write(f"{_('For help, contact', 'للدعم تواصل عبر')}: support@superwallet.sa")
    st.markdown('</div>', unsafe_allow_html=True)
