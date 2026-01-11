import re
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from sklearn.feature_extraction.text import CountVectorizer
from fpdf import FPDF

# -------------------------
# Helper Functions
# -------------------------
def clean_text(text):
    """Lowercase and remove special characters"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def extract_keywords(text):
    """Extract keywords from text using CountVectorizer"""
    text = clean_text(text)
    # Stop_words='english' removes common words like 'the', 'and', 'is'
    vectorizer = CountVectorizer(stop_words='english')
    try:
        vectorizer.fit_transform([text])
        return set(vectorizer.get_feature_names_out())
    except ValueError:
        return set()

def compare_skills(resume_keywords, jd_keywords):
    """Return matched and missing skills using Set logic"""
    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords.difference(resume_keywords)
    return matched, missing

def calculate_score(resume_keywords, jd_keywords):
    """Score based on keyword match percentage"""
    matched, _ = compare_skills(resume_keywords, jd_keywords)
    if not jd_keywords:
        return 0
    score = (len(matched) / len(jd_keywords)) * 100
    return round(score, 2)

def extract_pdf_text(pdf_path):
    """Extract text from PDF using PyMuPDF"""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def suggest_phrases(missing_skills):
    """Generate simple phrases to include missing skills"""
    return [f"- Highlight experience or projects involving {skill}" for skill in missing_skills]

# -------------------------
# PDF Report Generator
# -------------------------
class ResumeReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Resume Analysis Report", 0, 1, "C")
        self.ln(5)
    
    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1)
    
    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln(3)

def generate_pdf_report(score, matched, missing, suggestions, output_file="resume_report.pdf"):
    pdf = ResumeReport()
    pdf.add_page()
    
    pdf.section_title("Match Score")
    pdf.section_body(f"Your resume matches {score}% of the job description keywords.")
    
    pdf.section_title("Matched Skills")
    pdf.section_body(", ".join(matched) if matched else "None identified.")
    
    pdf.section_title("Missing Skills")
    pdf.section_body(", ".join(missing) if missing else "No missing skills found!")
    
    pdf.section_title("Suggested Phrases to Include")
    pdf.section_body("\n".join(suggestions) if suggestions else "Your resume looks well-optimized.")
    
    pdf.output(output_file)
    print(f"\n--- SUCCESS ---")
    print(f"PDF report generated: {output_file}")

# -------------------------
# Main Analysis Logic
# -------------------------
def analyze_resume_pdf(resume_pdf_path, job_description_text):
    print("Extracting text from PDF...")
    resume_text = extract_pdf_text(resume_pdf_path)
    
    print("Analyzing keywords...")
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_description_text)
    
    score = calculate_score(resume_keywords, jd_keywords)
    matched, missing = compare_skills(resume_keywords, jd_keywords)
    suggestions = suggest_phrases(missing)
    
    generate_pdf_report(score, matched, missing, suggestions)

# -------------------------
# Execution Block
# -------------------------
if __name__ == "__main__":
    # 1. Define the Job Description
    job_description = """
    Looking for a Python developer with experience in Django, Flask, REST APIs, 
    Pandas, NumPy, SQL, and JavaScript. Familiarity with front-end frameworks is a plus.
    """

    # 2. Setup the "Upload" window
    root = tk.Tk()
    root.withdraw() # Hide the tiny empty tkinter window
    root.attributes("-topmost", True) # Bring the file picker to the front

    print("Please select your resume PDF in the popup window...")
    
    # 3. Ask user to select file
    file_path = filedialog.askopenfilename(
        title="Select Your Resume PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    # 4. Run analysis if a file was chosen
    if file_path:
        analyze_resume_pdf(file_path, job_description)
    else:
        print("No file selected. Program cancelled.")