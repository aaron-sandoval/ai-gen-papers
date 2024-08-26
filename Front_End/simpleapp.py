import streamlit as st
import base64
from PIL import Image
from pathlib import Path

def main():
    # Set the page configuration
    st.set_page_config(page_title="AI Scientific Paper Generator", 
                    page_icon="🧠", 
                    layout="centered")

    # Set the title and subtitle of the landing page
    st.title("AI Generated Papers")
    st.subheader("Automating the creation of academic papers with AI")

    # st.sidebar.title("Navigation")
    # st.sidebar.button("Home", key="home_button")
    # st.sidebar.button("Generate Paper", key="generate_paper_button")

    # Add a header
    st.header("Introduction")

    # Add some text
    st.write("""
    Welcome to our AI-powered platform, where cutting-edge technology meets scientific research to automatically generate comprehensive and insightful academic papers.
    """)

    # Add an image to the page
    st.image(str(Path("Front_End")/"writing.jpg"), caption="research papers", use_column_width=True)

    # Add an input button
    # user_input = st.text_input("Enter your question:")

    # Display the input value
    # if user_input:
    #     st.write(f"Here is what we found for '{user_input}':")

    # Add navigation or interactive elements
    # if st.button("Generate Paper"):
    #     st.write("Paper generation process initiated...")

    # # Add a download button for the PDF file
    # def download_pdf(file_path):
    #     with open(file_path, "rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #     href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="pdf-test.pdf">Download PDF</a>'
    #     st.markdown(href, unsafe_allow_html=True)

    # download_pdf("Front_End/pdf-test.pdf")

    # st.markdown(
    #     """
    #     <style>
    #     .reportview-container {
    #         background: #f5f5f5;
    #     }
    #     .sidebar .sidebar-content {
    #         background-image: linear-gradient(#2e7bcf,#2e7bcf);
    #         color: white;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    # streamlit_app.py


    # Main Streamlit app starts here
    # st.write("Here goes your normal Streamlit app...")
    # st.button("Click me")

    def displayPDF(file):
        # Opening file from file path
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    # Display the PDF on the landing page
    displayPDF(Path("tex")/"with_figs"/"generated_paper_with_ref7_figs.pdf")

if __name__ == "__main__":
    main()