import streamlit as st

# --- Knowledge Book ---
st.sidebar.title("📖 Knowledge Book")

# Step 1: Select Continent
continents = ["Asia", "Europe", "North America", "South America", "Africa", "Oceania"]
continent = st.sidebar.selectbox("🌍 Select Continent", continents)

# Step 2: Select Country
countries = {
    "Asia": ["India", "China", "Japan"],
    "Europe": ["UK", "France", "Germany"],
    "North America": ["USA", "Canada", "Mexico"],
    "South America": ["Brazil", "Argentina", "Chile"],
    "Africa": ["South Africa", "Nigeria", "Kenya"],
    "Oceania": ["Australia", "New Zealand", "Fiji"]
}
country = st.sidebar.selectbox("🏳️ Select Country", countries[continent])

# Step 3: Display Cases
cases_db = {
    "India": [
        "Case 1: Kesavananda Bharati v. State of Kerala",
        "Case 2: Maneka Gandhi v. Union of India",
        "Case 3: State of Madras v. Champakam Dorairajan",
        "Case 4: Indira Gandhi v. Raj Narain",
        "Case 5: S.R. Bommai v. Union of India",
        "Case 6: Navtej Singh Johar v. Union of India"
    ],
    "USA": [
        "Case 1: Marbury v. Madison",
        "Case 2: Brown v. Board of Education",
        "Case 3: Miranda v. Arizona",
        "Case 4: Roe v. Wade",
        "Case 5: United States v. Nixon",
        "Case 6: Obergefell v. Hodges"
    ],
    # ⚡ You can expand for other countries later
}

st.subheader(f"📍 {country} — Landmark Cases")
if country in cases_db:
    for case in cases_db[country]:
        st.write(f"- {case}")
else:
    st.info("⚖️ Cases for this country will be added soon.")
