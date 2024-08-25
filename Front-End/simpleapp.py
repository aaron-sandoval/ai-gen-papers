import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(page_title="AI Scientific Paper Generator", 
                   page_icon="🧠", 
                   layout="centered")

# Set the title and subtitle of the landing page
st.title("AI Generated Papers")
st.subheader("Automating the creation of academic papers with AI")

st.sidebar.title("Navigation")
st.sidebar.button("Home", key="home_button")
st.sidebar.button("Generate Paper", key="generate_paper_button")

# Add a header
st.header("Introduction")

# Add some text
st.write("""
Welcome to our AI-powered platform, where cutting-edge technology meets scientific research to automatically generate comprehensive and insightful academic papers.
""")

# Add an image
st.image("writing.jpg", caption="research papers", use_column_width=True)

# Add an input button
user_input = st.text_input("Enter your question:")

# Display the input value
if user_input:
	st.write(f"Here is what we found for '{user_input}':")

# Add navigation or interactive elements
if st.button("Generate Paper"):
    st.write("Paper generation process initiated...")

st.markdown(
    """
    <style>
    .reportview-container {
        background: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# streamlit_app.py

import hmac
import streamlit as st


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

# Main Streamlit app starts here
st.write("Here goes your normal Streamlit app...")
st.button("Click me")