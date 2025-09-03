# import streamlit as st

# st.title("LawCompass ⚖️")
# st.write("Welcome to the LawCompass app! 🚀")
# st.write("This will be your platform for browsing landmark criminal law cases.")
import streamlit as st
from PIL import Image

# Set page config (title + favicon)
st.set_page_config(
    page_title="LawCompass ⚖️",
    page_icon="assets/lawcompass logo.jpg",  # favicon
    layout="centered"
)

# Load and show logo
logo = Image.open("assets/lawcompass logo.jpg")
st.image(logo, width=200)

st.title("⚖️ Welcome to LawCompass")
st.write("Browse landmark criminal law cases across the globe.")
