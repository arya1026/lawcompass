# import streamlit as st

# # --- Knowledge Book ---
# st.sidebar.title("📖 Knowledge Book")

# # Step 1: Select Continent
# continents = ["Asia", "Europe", "North America", "South America", "Africa", "Oceania"]
# continent = st.sidebar.selectbox("🌍 Select Continent", continents)

# # Step 2: Select Country
# countries = {
#     "Asia": ["India", "China", "Japan"],
#     "Europe": ["UK", "France", "Germany"],
#     "North America": ["USA", "Canada", "Mexico"],
#     "South America": ["Brazil", "Argentina", "Chile"],
#     "Africa": ["South Africa", "Nigeria", "Kenya"],
#     "Oceania": ["Australia", "New Zealand", "Fiji"]
# }
# country = st.sidebar.selectbox("🏳️ Select Country", countries[continent])

# # Step 3: Display Cases
# cases_db = {
#     "India": [
#         "Case 1: Kesavananda Bharati v. State of Kerala",
#         "Case 2: Maneka Gandhi v. Union of India",
#         "Case 3: State of Madras v. Champakam Dorairajan",
#         "Case 4: Indira Gandhi v. Raj Narain",
#         "Case 5: S.R. Bommai v. Union of India",
#         "Case 6: Navtej Singh Johar v. Union of India"
#     ],
#     "USA": [
#         "Case 1: Marbury v. Madison",
#         "Case 2: Brown v. Board of Education",
#         "Case 3: Miranda v. Arizona",
#         "Case 4: Roe v. Wade",
#         "Case 5: United States v. Nixon",
#         "Case 6: Obergefell v. Hodges"
#     ],
#     # ⚡ You can expand for other countries later
# }

# st.subheader(f"📍 {country} — Landmark Cases")
# if country in cases_db:
#     for case in cases_db[country]:
#         st.write(f"- {case}")
# else:
#     st.info("⚖️ Cases for this country will be added soon.")
# st.subheader("🔎 Search Landmark Cases")

# # Flatten cases_db into a single list
# all_cases = []
# for c_list in cases_db.values():
#     all_cases.extend(c_list)

# # Search input
# query = st.text_input("Enter case name")

# if query:
#     results = [case for case in all_cases if query.lower() in case.lower()]
#     if results:
#         st.success("✅ Search Results:")
#         for r in results:
#             st.write(f"- {r}")
#     else:
#         st.warning("❌ No matching cases found.")
import streamlit as st
from PIL import Image
import base64

# -------------------------------
# Branding & Page Config
# -------------------------------
st.set_page_config(
    page_title="LawCompass ⚖️",
    page_icon="assets/lawcompass_logo.jpg",
    layout="wide"
)

# Rotating logo controls
st.sidebar.header("⚙️ Logo Controls")
size = st.sidebar.slider("Logo Size", 50, 400, 200)
speed = st.sidebar.slider("Rotation Speed (seconds per spin)", 1, 10, 5)
spin = st.sidebar.checkbox("Rotate Logo", True)

# Convert logo for embedding
logo_path = "assets/lawcompass_logo.jpg"
with open(logo_path, "rb") as f:
    logo_data = base64.b64encode(f.read()).decode()

rotation_style = f"""
<style>
@keyframes spin {{
  0% {{ transform: rotate(0deg); }}
  100% {{ transform: rotate(360deg); }}
}}
.logo {{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: {size}px;
  animation: {'spin ' + str(speed) + 's linear infinite' if spin else 'none'};
}}
</style>
"""
st.markdown(rotation_style, unsafe_allow_html=True)
st.markdown(f'<img src="data:image/png;base64,{logo_data}" class="logo">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#003366;'>⚖️ LawCompass</h1>", unsafe_allow_html=True)

# -------------------------------
# Fake User Database
# -------------------------------
if "users" not in st.session_state:
    st.session_state["users"] = {"admin": "1234"}
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = None

def login():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid username or password.")

def signup():
    st.subheader("📝 Signup")
    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")
    if st.button("Create Account"):
        if new_user in st.session_state["users"]:
            st.error("Username already exists.")
        else:
            st.session_state["users"][new_user] = new_pass
            st.success("Account created! You can now log in.")

# -------------------------------
# Knowledge Book Data
# -------------------------------
cases_db = {
    "India": {
        "law_book": "The Constitution of India",
        "cases": [
            ("Kesavananda Bharati v. State of Kerala", "Basic structure doctrine"),
            ("Maneka Gandhi v. Union of India", "Expanded personal liberty"),
            ("Indira Gandhi v. Raj Narain", "Election dispute case"),
            ("Navtej Singh Johar v. Union of India", "Decriminalized homosexuality"),
            ("Vishaka v. State of Rajasthan", "Workplace harassment guidelines"),
            ("S.R. Bommai v. Union of India", "Federalism principles")
        ]
    },
    "USA": {
        "law_book": "United States Constitution",
        "cases": [
            ("Marbury v. Madison", "Established judicial review"),
            ("Brown v. Board of Education", "Ended school segregation"),
            ("Miranda v. Arizona", "Miranda rights established"),
            ("Roe v. Wade", "Abortion rights (later overturned)"),
            ("United States v. Nixon", "Executive privilege limited"),
            ("Obergefell v. Hodges", "Legalized same-sex marriage")
        ]
    },
    "UK": {
        "law_book": "Magna Carta & UK Common Law",
        "cases": [
            ("Donoghue v. Stevenson", "Established negligence"),
            ("R v. Dudley and Stephens", "Necessity is no defense to murder"),
            ("R v. Brown", "Consent and bodily harm"),
            ("Carlill v. Carbolic Smoke Ball Co.", "Contract law principles"),
            ("R v. R", "Marital rape illegal"),
            ("Miller v. Prime Minister", "Prorogation unlawful")
        ]
    },
    # Add France, South Africa, Brazil, Australia similarly...
}

articles = [
    ("The Evolution of Criminal Law", "How criminal law has shaped modern justice systems."),
    ("Digital Privacy in the Age of Surveillance", "Balancing security with fundamental rights."),
    ("International Law and Human Rights", "The global framework for protecting individuals."),
    ("Gender Justice and the Law", "Progress and challenges in achieving equality.")
]

national_laws = {
    "India": ["IPC 1860", "CrPC 1973", "Evidence Act 1872"],
    "USA": ["Civil Rights Act 1964", "Patriot Act 2001"],
    "UK": ["Human Rights Act 1998", "Equality Act 2010"]
}
international_laws = [
    "UN Charter",
    "Geneva Conventions",
    "Rome Statute of the ICC",
    "Universal Declaration of Human Rights"
]

# -------------------------------
# Chatbot Logic
# -------------------------------
def chatbot_response(user_input):
    user_input = user_input.lower()
    for country, data in cases_db.items():
        for case, desc in data["cases"]:
            if case.lower() in user_input:
                return f"📚 {case}: {desc}"
    if "international law" in user_input:
        return "🌍 International law governs relations between nations, including treaties, war, and human rights."
    return "🤖 Sorry, I don’t know that yet."

# -------------------------------
# Navigation
# -------------------------------
menu = ["Home", "Knowledge Book", "Articles", "Laws", "Chatbot", "Login", "Signup"]
choice = st.sidebar.radio("📂 Navigation", menu)

if choice == "Home":
    st.write("Welcome to **LawCompass ⚖️** — your portal to explore landmark cases, laws, and more.")

elif choice == "Login":
    login()

elif choice == "Signup":
    signup()

elif st.session_state["logged_in"]:  # Protected features
    if choice == "Knowledge Book":
        st.subheader("📖 Knowledge Book")
        continent = st.selectbox("🌍 Select Continent", ["Asia", "Europe", "North America"])
        if continent == "Asia":
            countries = ["India"]
        elif continent == "North America":
            countries = ["USA"]
        elif continent == "Europe":
            countries = ["UK"]
        else:
            countries = []
        country = st.selectbox("🏳️ Select Country", countries)
        if country in cases_db:
            st.write(f"**Law Book**: {cases_db[country]['law_book']}")
            for case, desc in cases_db[country]["cases"]:
                st.write(f"- **{case}** — {desc}")

        # Global Search
        st.subheader("🔎 Search Cases")
        query = st.text_input("Enter case name")
        if query:
            results = []
            for c_data in cases_db.values():
                for case, desc in c_data["cases"]:
                    if query.lower() in case.lower():
                        results.append((case, desc))
            if results:
                for case, desc in results:
                    st.success(f"**{case}** — {desc}")
            else:
                st.warning("No matching cases found.")

    elif choice == "Articles":
        st.subheader("📰 Legal Articles")
        for title, summary in articles:
            st.write(f"### {title}")
            st.write(summary)

    elif choice == "Laws":
        st.subheader("⚖️ National & International Laws")
        tab1, tab2 = st.tabs(["National Laws", "International Laws"])
        with tab1:
            for country, laws in national_laws.items():
                st.write(f"**{country}**: {', '.join(laws)}")
        with tab2:
            st.write(", ".join(international_laws))

    elif choice == "Chatbot":
        st.subheader("💬 Legal Chatbot")
        user_q = st.text_input("Ask me about a case or law")
        if st.button("Send"):
            st.write(chatbot_response(user_q))
else:
    st.warning("🔒 Please login to access features.")

