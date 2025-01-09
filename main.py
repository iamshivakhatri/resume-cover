import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from utils import clean_text
import pyperclip


def create_streamlit_app(llm, clean_text):
    st.set_page_config(
        layout="wide",
        page_title="Resume & Cover Letter Generator",
        page_icon="📧",
    )

    st.title("📧 Resume & Cover Letter Generator")
    st.sidebar.header("Options")

    # Create a radio button for selecting input type
    input_type = st.sidebar.radio(
        "Choose input type:",
        ("URL", "Job Description")
    )

    if input_type == "URL":
        url_input = st.text_input("Enter a URL:")
    elif input_type == "Job Description":
        job_description_input = st.text_area("Enter Job Description:")

    # Submit button placed below input fields
    if st.button("Submit"):
        try:
            if input_type == "URL":
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
            elif input_type == "Job Description":
                data = clean_text(job_description_input)



            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                email = llm.write_mail(job)
                resume_points = llm.resume_points(job)


                st.subheader("Resume Points")
                st.code(resume_points, language='markdown')

                st.subheader("Generated Email")
                st.code(email, language='markdown')

                

        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    create_streamlit_app(chain, clean_text)
