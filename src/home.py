# Home.py
# streamlit run src/home.py


import streamlit as st
from backend.utils import init_db, load_images_meta
import pkgutil, sys

# Page configuration
st.set_page_config(page_title="The detection Game — Home", layout="wide", initial_sidebar_state="collapsed")


# Initialize database and load data
init_db()

# Main content: title and subheading
st.markdown("<h1 style='text-align: center;'>Human or Machine?</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; max-width: 800px; margin: 0 auto; padding: 0 2rem;'>
<h3>Do you think you can spot the AI-generated artworks and beat our AI Detector</h3>

</div>
""", unsafe_allow_html=True)

# Simple styling
st.markdown("""
<style>

/* Background image - commented out for testing */
/*
.stApp {
    background-image: url("https://raw.githubusercontent.com/imanidris21/Detection-Game-v2/main/src/assets/home_bg.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
*/

/* Add overlay for better text readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.3);
    z-index: -1;
}

/* Force headings to be centered on all viewports */
div.block-container h1 {
    text-align: center !important;
    color: white !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    font-size: 4rem !important;
    font-weight: bold !important;
    margin-bottom: 1rem !important;
}

div.block-container h3 {
    text-align: center !important;
    color: white !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
    font-size: 1.5rem !important;
}



/* Button styling */
.stButton {
    display: flex !important;
    justify-content: center !important;
    margin-top: 2rem !important;
}
.stButton > button {
    background-color: black !important;
    color: white !important;
    border: 2px solid white !important;
    padding: 0.5rem 1.5rem !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
}
.stButton > button:hover {
    background-color: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
    border: 2px solid white !important;
}

/* Center align text in columns */
.stColumn {
    text-align: center !important;
}   

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    if st.button("Start the Game", type="primary", use_container_width=True):
        st.switch_page("pages/1_Take_the_Test.py")




