VidhAI Legal Summarization Tool
Overview
The VidhAI Legal Summarization Tool is an AI-powered application designed to streamline the summarization of complex legal documents. By leveraging advanced Natural Language Processing (NLP) techniques and powerful models like Llama 3.1 and Groq API, VidhAI provides tailored summaries for various legal contexts, enhancing productivity and reducing the time spent on manual document review.

Features
Automated Summarization: Generate concise summaries for legal documents, including depositions, trial records, medical chronologies, and arbitration casebooks.
Custom Summary Formats: Choose from predefined summary types such as Narrative Deposition, Trial Summary, and Medical Narrative.
User-Friendly Interface: Intuitive Streamlit-based web app for easy document uploads, summary generation, and downloads.
High-Quality Outputs: Utilizes advanced AI models to ensure accurate, context-specific summaries.
PDF Support: Upload legal documents in PDF format and download summaries as formatted PDF files.
Installation
To set up and run the VidhAI Legal Summarization Tool on your system:

Clone the Repository:

bash
Copy code
git clone https://github.com/your-repository/VidhAI.git
cd VidhAI
Install Dependencies:
Ensure you have Python 3.x installed. Install the required packages using:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the root directory and add your API keys:

plaintext
Copy code
GROQ_API_KEY=<your_groq_api_key>
Run the Application:
Launch the Streamlit app using:

bash
Copy code
streamlit run app.py
Access the Application:
Open your browser and navigate to the provided URL (default: http://localhost:8501).

Usage
Upload a PDF Document:
Drag and drop your legal document in PDF format into the upload area.
Select a Summary Type:
Choose from options like Narrative Deposition, Trial Summary, or Medical Chronology.
Generate the Summary:
Click the respective button to generate a concise, tailored summary.
Download the Summary:
Save the generated summary as a PDF for further use.
Project Structure
graphql
Copy code
VidhAI/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Required Python dependencies
├── styles.py               # Custom CSS for styling
├── config.py               # Configuration file for environment variables
├── utils/
│   ├── pdf_processing.py   # Functions for PDF text extraction
│   ├── pdf_download.py     # Functions for PDF generation and download
│   ├── summary_generation.py # Functions for AI-powered summarization
├── assets/                 # Images, icons, and other static assets
Key Technologies
Frontend: Streamlit for interactive web-based UI.
Backend: Python with LangChain and Groq API integration.
PDF Processing: PyMuPDF (fitz) for text extraction and FPDF for PDF generation.
AI Models: Llama 3.1 and Groq API for legal document summarization.
Future Enhancements
Multi-lingual support for legal documents in regional and international languages.
Predictive analytics for case outcomes based on historical data.
Enhanced collaboration features for team-based workflows.
Contributions
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
