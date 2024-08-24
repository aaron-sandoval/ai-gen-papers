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
st.image("https://via.placeholder.com/800x400.png?text=Welcome+to+My+App", caption="Welcome Image")

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