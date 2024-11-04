from fpdf import FPDF
import io

def generate_pdf(summary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary_text)
    
    pdf_output = io.BytesIO()
    pdf_content = pdf.output(dest="S").encode("latin1")
    pdf_output.write(pdf_content)
    pdf_output.seek(0)
    
    return pdf_output