import streamlit as st
import os
from cover_letter import CoverLetterAI  

# App Styling & Config
st.set_page_config(page_title="AI Cover Letter Generator - By Piero Paialunga", page_icon="🦾", layout="centered")

# Custom CSS for UI Styling
st.markdown(
    """
    <style>
        .main { background-color: #f9f9f9; }
        .stTextArea textarea { font-size: 14px; }
        .stButton button { font-size: 16px; font-weight: bold; background-color: #4CAF50; color: white; border-radius: 8px; }
        .stButton button:hover { background-color: #45a049; }
        .stTextInput input { font-size: 14px; }
        .footer { font-size: 14px; text-align: center; padding-top: 20px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a Logo (Make sure "logo.png" is in the same directory)
st.image("app_images/logo.png")

# Title and Description
st.markdown("<h1 style='text-align: center;'>📄 AI Cover Letter Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Upload your resume and job description, and let AI craft a professional cover letter.</p>", unsafe_allow_html=True)

# API Key Input
st.subheader("🔑 Insert Your API Key")
st.markdown(
    "🔑 **You can generate your API key here.** "
    "[here](https://www.llama-api.com/) 🔗",
    unsafe_allow_html=True
)

api_key = st.text_input("Enter your API key", type="password")

# File Upload
st.subheader("📂 Let me know you!")
st.write("Upload a **.docx** or **.pdf** file containing your resume. The AI will profile it for you.")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])

if uploaded_file is not None and api_key:
    # Save uploaded file temporarily
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())

    # Process file with CoverLetterAI
    cover_letter_ai = CoverLetterAI(llm_api_key=api_key)  # Pass API key to backend
    cover_letter_ai.read_candidate_data(temp_file_path)

    # Remove temp file after processing (optional)
    os.remove(temp_file_path)

    # Display Extracted Resume Information
    st.subheader("🔍 AI is extracting your resume information")
    st.text_area("This is your profile overview", cover_letter_ai.profile_candidate(), height=300)

    # Job Description Input
    st.subheader("📌 Now tell me about your dream job")
    job_description = st.text_area("Copy paste the job description of the job that you like", "", height=200)

    # Generate Cover Letter
    if st.button("✍️ Generate Cover Letter"):
        cover_letter_ai.add_job_description(job_description)
        cover_letter = cover_letter_ai.write_cover_letter()
        st.subheader("🪄 Enjoy the magic")
        st.text_area("This is the AI-generated cover letter!", cover_letter, height=300)

elif uploaded_file is not None and not api_key:
    st.warning("⚠️ Please enter your API key before proceeding.")

# Footer with Credits
st.markdown(
    """
    <div class="footer">
        <p>Made by <b>Piero Paialunga</b> | <a href="https://piero-paialunga.medium.com/" target="_blank">View My Portfolio</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
