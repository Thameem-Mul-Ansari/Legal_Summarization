# VidhAI Legal Summarization Tool

## Overview

The **VidhAI Legal Summarization Tool** is an AI-powered platform designed to simplify the summarization of complex legal documents. Built with cutting-edge AI models like **Llama 3.1** and **Groq API**, VidhAI generates custom, context-specific summaries to save time and enhance legal workflows.

## Features

- **Automated Summarization:** Process lengthy legal documents, including depositions, trial records, medical chronologies, and arbitration casebooks
- **Custom Summary Formats:** Choose tailored formats like Narrative Deposition, Trial Summary, or Medical Chronology
- **PDF Integration:** Upload documents in PDF format and download professionally formatted summaries
- **AI-Powered Summaries:** Leveraging Llama 3.1 for accurate, high-quality summaries
- **User-Friendly Interface:** Easy-to-use Streamlit-based app for streamlined document management

## Installation

Follow these steps to install and run the VidhAI tool locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository/VidhAI.git
cd VidhAI
```

### 2. Install Dependencies
Ensure Python 3.x is installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add your API key:
```plaintext
GROQ_API_KEY=<your_groq_api_key>
```

### 4. Run the Application
Launch the Streamlit application:
```bash
streamlit run app.py
```

### 5. Access the Application
Open your browser and navigate to `http://localhost:8501`

## Project Structure

```plaintext
VidhAI/
├── app.py                   # Main application file
├── requirements.txt         # List of dependencies
├── config.py               # Configuration for environment variables
├── styles.py              # Custom CSS styling
├── utils/
│   ├── pdf_processing.py   # PDF text extraction utilities
│   ├── pdf_download.py     # Functions for PDF generation and downloads
│   ├── summary_generation.py # LLM-powered summarization logic
├── assets/                 # Static assets like images or logos
```

## Key Technologies

- **Frontend:** Streamlit for creating the interactive web app
- **Backend:** Python-based processing using LangChain and Groq API integration
- **AI Models:** Llama 3.1 for generating high-quality legal document summaries
- **PDF Handling:** PyMuPDF (fitz) for text extraction and FPDF for generating PDFs

## Usage

1. **Upload a Document:** Drag and drop a PDF legal document into the upload area
2. **Choose Summary Type:** Select from predefined options like Narrative Deposition or Trial Summary
3. **Generate Summary:** Click the appropriate button to process the document and generate a summary
4. **Download Summary:** Save the generated summary as a PDF file

## Future Enhancements

- Multi-lingual support for summarizing legal documents in multiple languages
- Predictive analytics for case outcomes based on legal document data
- Improved customization of summary formats for specialized use cases

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add a new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries, reach out via:
- Email: thameemmulansaris@gmail.com
- GitHub: https://github.com/Thameem-Mul-Ansari
