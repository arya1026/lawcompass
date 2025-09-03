# import streamlit as st

# st.title("LawCompass ⚖️")
# st.write("Welcome to the LawCompass app! 🚀")
# st.write("This will be your platform for browsing landmark criminal law cases.")
# import streamlit as st
# from PIL import Image

# # Set page config (title + favicon)
# st.set_page_config(
#     page_title="LawCompass ⚖️",
#     page_icon="assets/lawcompass logo.jpg",  # favicon
#     layout="centered"
# )

# # Load and show logo
# logo = Image.open("assets/lawcompass logo.jpg")
# st.image(logo, width=200)

# st.title("⚖️ Welcome to LawCompass")
# st.write("Browse landmark criminal law cases across the globe.")
import streamlit as st
from PIL import Image
import base64

# Page config
st.set_page_config(
    page_title="LawCompass ⚖️",
    page_icon="assets/lawcompass logo.jpg",
    layout="centered"
)

# Controls
st.sidebar.header("⚙️ Logo Controls")
size = st.sidebar.slider("Logo Size", 50, 400, 200)
speed = st.sidebar.slider("Rotation Speed (seconds per spin)", 1, 10, 5)
spin = st.sidebar.checkbox("Rotate Logo", True)

# Load logo
logo_path = "assets/lawcompass logo.jpg"
logo = Image.open(logo_path)

# Convert image to base64 for embedding in HTML
with open(logo_path, "rb") as f:
    data = base64.b64encode(f.read()).decode()

# Rotation CSS/HTML
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

# Display rotating logo
st.markdown(rotation_style, unsafe_allow_html=True)
st.markdown(f'<img src="data:image/png;base64,{data}" class="logo">', unsafe_allow_html=True)

# App title and intro
st.title("⚖️ Welcome to LawCompass")
st.write("Browse landmark criminal law cases across the globe.")
