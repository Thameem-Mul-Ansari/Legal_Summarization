import os
import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
from langchain_groq import ChatGroq
from PIL import Image  # to convert PDF pages to images
from dotenv import load_dotenv  # Import to load .env files
from fpdf import FPDF  # Import to generate PDF files
import io  # Import io to use BytesIO for Streamlit download

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="VIDH-AI: Legal Summarization Tool",
    page_icon="lingo.jpeg",  # Replace with your image URL or path
    layout="wide"
)

# Check if GROQ_API_KEY is set
if not groq_api_key:
    st.error("GROQ API Key is not set. Please check your .env file.")
    st.stop()  # Stop the app if the API key is missing

# Modified function to extract text from each page as separate items
def extract_text_from_pdf(pdf_file):
    page_texts = []
    pdf_file.seek(0)  # Reset file pointer to the beginni# Convert the uploaded file to a BytesIO object
    pdf_file = io.BytesIO(uploaded_file.read())
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    for page in doc:
        page_texts.append(page.get_text("text"))  # Extract text from each page
    return page_texts

# Function to generate legal summary in third-person perspective with structured headings
def get_legal_summary(text, summary_type):
    # Define heading formats based on summary type
    summary_formats = {
        "narrative deposition": """
        **Case Information**
        - **Case Name & Number**
        - **Date Filed**
        - **Jurisdiction**
        - **Type of Proceeding**
        - **Court**
        - **Date of Judgment**
        
        **Parties and Representation**
        - **Complainant**
        - **Defendants**
        - **Counsel for Complainant**
        - **Counsel for Defendant**
        
        **Procedural History and Timeline of Key Events**
        
        **Key Documents, Evidence, and Exhibits**
        
        **Points of Interest**
        
        **Applicable Laws and Precedents**
        
        **Background and Case Details**
        
        **Legal Arguments**
        
        **Court’s Analysis and Findings**
        
        **Decision and Orders**
        
        **Significance of the Judgment**
        """,
        "medical chronology": """
        **Patient Information**
        - **Date of Incident/Injury**
        - **Primary Complaint or Diagnosis**
        
        **Timeline of Medical Events**
        - **Date**
        - **Provider/Facility**
        - **Medical Findings/Examinations**
        - **Treatments/Interventions**
        - **Significant Changes in Condition**
        - **Medications Prescribed**
        - **Relevant Lab Results/Imaging**
        - **Surgical Procedures**
        - **Ongoing or Future Care**
        - **Prognosis**
        
        **Summary of Key Medical Findings**
        """,
        "trial summary": """
        **Case Information**
        - **Case Name and Number**
        - **Jurisdiction**
        - **Judge**

        **Parties and Representation**
        - **Plaintiff(s)**
        - **Defendant(s)**
        - **Counsel for Plaintiff(s)**
        - **Counsel for Defendant(s)**

        **Pre-Trial Motions and Rulings**
        
        **Opening Statements**
        
        **Witnesses and Testimonies**
        
        **Evidence Presented**
        
        **Key Legal Arguments**
        
        **Closing Arguments**
        
        **Jury Instructions (if applicable)**
        
        **Verdict**
        
        **Post-Trial Motions**
        
        **Appeal (if applicable)**
        
        **Conclusion**
        """,
        # Other summary types go here with the same format...
    }

    # Select the format based on summary type
    headings = summary_formats.get(summary_type, "Please specify a valid summary type.")
    prompt = f"Summarize the following legal document from a third-person legal perspective, focusing on {summary_type}. Use the following format:\n\n{headings}\n\n{text}"
    
    summary_response = summarizer_llm.invoke(prompt)
    return summary_response.content

# Initialize the LLaMA models
extractor_llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    api_key=groq_api_key  # Pass the API key to the client
)
summarizer_llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    api_key=groq_api_key  # Pass the API key to the client
)

def generate_pdf(summary_response):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Adding the summary content
    pdf.multi_cell(0, 10, summary_response)

    # Use BytesIO to handle in-memory binary data for Streamlit download
    pdf_output = io.BytesIO()
    pdf_content = pdf.output(dest="S").encode("latin1")  # Get the PDF content as a bytes string

    # Write the PDF content to BytesIO buffer
    pdf_output.write(pdf_content)
    
    # Move cursor back to the start of the stream
    pdf_output.seek(0)
    
    return pdf_output

with st.sidebar:
    st.image("background.gif", use_column_width=True)  # Replace with your image path or URL
    st.subheader("Select Summary Type")

    uploaded_file = st.file_uploader("Upload your legal document (PDF)", type="pdf")

    # Custom CSS to style buttons
    st.markdown(
        """
        <style>
        .stButton > button {
            width: 90%;
            margin: 5px 0;  /* Add vertical margin between buttons */
            padding: 8px 0;  /* Add padding for better click area */
            border-radius: 8px;  /* Rounded corners for buttons */
            font-size: 14px;  /* Increase font size */
            font-weight: 500;
        }
        .sidebar-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
        }
        .sidebar-grid .stButton {
            flex: 1 1 48%;  /* Set width to 48% for two-column layout */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Wrap buttons in a div with class "sidebar-grid" for grid layout
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

# Initialize summary_response to None
summary_response = None
# Check if a PDF file has been uploaded
# Main content area with a title
# Main content area with a title
st.markdown("<h1 style='text-align: center;'>VIDH-AI: Legal Summarization Tool</h1>", unsafe_allow_html=True)

# Check if a PDF file has been uploaded
if uploaded_file:
    # Divide the page into two columns
    col1, col2 = st.columns([1, 2])  # Give the summary column more space

    # Custom CSS for centering, border styling, and clean display
    st.markdown(
        """
        <style>
        .centered {
            text-align: center;
        } 
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, spacer, col2 = st.columns([1, 0.2, 2])  # Adjust the middle value for more or less space

    # Column for displaying PDF content
    with col1:
        # Center-align header
        st.markdown("<h3 class='centered'>Uploaded PDF Content</h3>", unsafe_allow_html=True)

        # Display PDF content inside a bordered box
        st.markdown("<div class='pdf-box'>", unsafe_allow_html=True)
        
        # Process and display each page as an image inside the container
# Convert the uploaded file to a BytesIO object
        pdf_file = io.BytesIO(uploaded_file.read())
        doc = fitz.open(stream=pdf_file, filetype="pdf")
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))

            st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with spacer:
        st.write("") 

    if 'summary_response' not in st.session_state:
        st.session_state.summary_response = None
    if 'summary_type' not in st.session_state:
        st.session_state.summary_type = None

    with col2:
        # Center-align header
        st.markdown("<h3 class='centered'>Legal Summary</h3>", unsafe_allow_html=True)

        # Display summary output inside a bordered box
        st.markdown("<div class='summary-box'>", unsafe_allow_html=True)

        
        # Process the uploaded file and generate summary based on selected option
        with st.spinner('Extracting text from the uploaded document...'):
            extracted_text = extract_text_from_pdf(uploaded_file)

        # Generate summaries based on button clicked and store result in session_state
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

        # Display the summary stored in session_state, if available
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

        st.markdown("</div>", unsafe_allow_html=True)  # End of summary-box
 

else:
    st.info("Please upload a PDF document to start.")