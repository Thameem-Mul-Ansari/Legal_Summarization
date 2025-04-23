import streamlit as st
from config import GROQ_API_KEY
from utils.pdf_processing import display_pdf_content
from utils.summary_generation import get_legal_summary
from utils.pdf_download import generate_pdf
import os
from styles import STYLE_CSS
import fitz
import io

st.set_page_config(
    page_title="VIDH-AI: Legal Summarization Tool",
    page_icon="assets/lingo.jpeg",
    layout="wide"
)

st.markdown(f"<style>{STYLE_CSS}</style>", unsafe_allow_html=True)

if not GROQ_API_KEY:
    st.error("GROQ API Key is not set. Please check your .env file.")
    st.stop()

with st.sidebar:
    st.image("assets/background.gif", use_container_width=True)
    st.subheader("Select Summary Type")

    uploaded_file = st.file_uploader("Upload your legal document (PDF)", type="pdf")

    # Sidebar buttons in a grid layout
    st.markdown('<div class="sidebar-grid">', unsafe_allow_html=True)
    narrative_button = st.button("Narrative Deposition Summary")
    page_line_button = st.button("Page-Line Deposition Summary")
    trial_summary_button = st.button("Trial Summary")
    trial_dailies_button = st.button("Trial Dailies Summary")
    arbitration_button = st.button("Arbitration Summary")
    personal_injury_button = st.button("Personal Injury Deposition Summary")
    medical_chronology_button = st.button("Medical Chronology Summary")
    medical_narrative_button = st.button("Medical Narrative Summary")
    hearing_summary_button = st.button("Hearing Summary")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h1 class='centered'>VIDH-AI: Legal Summarization Tool</h1>", unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    page_texts = []
    pdf_file.seek(0)  # Reset file pointer to the beginni# Convert the uploaded file to a BytesIO object
    pdf_file = io.BytesIO(uploaded_file.read())
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    for page in doc:
        page_texts.append(page.get_text("text"))  # Extract text from each page
    return page_texts

if uploaded_file:
    col1, spacer, col2 = st.columns([1, 0.2, 2])

    with col1:
        st.markdown("<h3 class='centered'>Uploaded PDF </h3>", unsafe_allow_html=True)
        display_pdf_content(uploaded_file) 
    with spacer:
        st.write("")

    if 'summary_response' not in st.session_state:
        st.session_state.summary_response = None
    if 'summary_type' not in st.session_state:
        st.session_state.summary_type = None

    with col2:
        st.markdown("<h3 class='centered'>Legal Summary</h3>", unsafe_allow_html=True)

        extracted_text = extract_text_from_pdf(uploaded_file)  # Extract text from PDF

        # Generate summaries based on button clicked
        if narrative_button:
            with st.spinner("Generating Narrative Deposition Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "narrative deposition")
                st.session_state.summary_type = "narrative deposition"

        elif page_line_button:
            with st.spinner("Generating Page-Line Deposition Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "page-to-page summary")
                st.session_state.summary_type = "page-line deposition"

        elif trial_summary_button:
            with st.spinner("Generating Trial Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "trial summary")
                st.session_state.summary_type = "trial"

        elif trial_dailies_button:
            with st.spinner("Generating Trial Dailies Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "trial dailies")
                st.session_state.summary_type = "trial dailies"

        elif arbitration_button:
            with st.spinner("Generating Arbitration Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "arbitration summary")
                st.session_state.summary_type = "arbitration"

        elif personal_injury_button:
            with st.spinner("Generating Personal Injury Deposition Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "personal injury deposition")
                st.session_state.summary_type = "personal injury deposition"

        elif medical_chronology_button:
            with st.spinner("Generating Medical Chronology Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "medical chronology")
                st.session_state.summary_type = "medical chronology"

        elif medical_narrative_button:
            with st.spinner("Generating Medical Narrative Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "medical narrative")
                st.session_state.summary_type = "medical narrative"

        elif hearing_summary_button:
            with st.spinner("Generating Hearing Summary..."):
                st.session_state.summary_response = get_legal_summary(extracted_text, "hearing summary")
                st.session_state.summary_type = "hearing"

        if st.session_state.summary_response:
            st.write(st.session_state.summary_response)

            # Generate the PDF file and display download button
            pdf_file = generate_pdf(st.session_state.summary_response)
            original_filename = os.path.splitext(uploaded_file.name)[0]
            summary_filename = f"{original_filename}_{st.session_state.summary_type.replace(' ', '_')}_summary.pdf"

            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name=summary_filename,
                mime="application/pdf"
            )

else:
    st.info("Please upload a PDF document to start.")
