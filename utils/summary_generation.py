from langchain_groq import ChatGroq
from config import GROQ_API_KEY

extractor_llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    api_key=GROQ_API_KEY
)
summarizer_llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    api_key=GROQ_API_KEY
)

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