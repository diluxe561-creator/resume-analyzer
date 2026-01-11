# AI RESUME OPTIMIZER & ATS CHECKER

An intelligent Python tool that uses Natural Language Processing (NLP) to compare a resume against a job description. It identifies missing keywords, calculates a match score, and generates a PDF optimization report.

---

## 🚀 KEY FEATURES
- PDF Text Extraction: Uses PyMuPDF (fitz) to read resume data accurately.
- Keyword Analysis: Utilizes Scikit-learn's CountVectorizer to identify professional skills and technical terms.
- GUI File Picker: Simple Tkinter interface to browse and select your resume.
- Match Scoring: Instant percentage-based score showing how well you fit the role.
- Strategy Report: Automatically generates a 'resume_report.pdf' with actionable suggestions and missing phrases.

---

## 🛠️ INSTALLATION

1. Ensure you have Python 3.x installed.
2. Install the required NLP and PDF processing libraries:
   pip install pymupdf scikit-learn fpdf

3. Run the application:
   python resume_optimizer.py

---

## 🖥️ HOW IT WORKS



1. EXTRACT: The script opens your PDF and converts the layout into clean, machine-readable text.
2. CLEAN: It removes "stop words" (like 'and', 'the', 'is') to focus only on high-value skills and nouns.
3. COMPARE: It performs a set-logic comparison between the Job Description keywords and your Resume keywords.
4. REPORT: It identifies exactly which skills are missing and tells you how to phrase them to pass ATS filters.

---

## 📝 WORKFLOW

1. Start the script. A file explorer window will appear.
2. Select your Resume (PDF format).
3. The script will analyze it against the embedded Job Description.
4. Check your project folder for 'resume_report.pdf' to see your results.

---

## 📁 SYSTEM REQUIREMENTS
- PyMuPDF (fitz): For reading PDFs.
- Scikit-learn: For keyword extraction and vectorization.
- Tkinter: For the file upload dialog (usually included with Python).
- FPDF: For generating the final report.

---

## 💡 PRO TIP
To change the job you are applying for, simply edit the 'job_description' variable inside the script with the new text from the job posting.

---

Optimize your path to the interview.
