# 🎯 AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions, calculates a match score, and identifies missing skills — helping job seekers optimize their resumes for specific roles.

## 🚀 Features

- 📄 Extracts text from PDF resumes (multi-page support)
- 🔍 NLP-based skill matching between resume and job description
- 📊 Match score calculation with visual progress bar
- ✅ Highlights matched skills
- ❌ Identifies missing skills for improvement
- 🌐 Interactive web interface built with Streamlit

## 🛠️ Tech Stack

- **Python** — Core language
- **pdfplumber** — PDF text extraction
- **pandas** — Data handling
- **scikit-learn** — Text processing utilities
- **Streamlit** — Web app framework

## 📸 Screenshots

*(<img width="998" height="874" alt="Ai Resume" src="https://github.com/user-attachments/assets/2876f9bf-9fcb-45c5-966e-6a4a320cff41" />
)*

## ⚙️ How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/khushisingh916228-droid/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

4. Run the app
```bash
streamlit run app.py
```

5. Open your browser at `http://localhost:8501`

## 📁 Project Structure
AI-Resume-Analyzer/
├── main.py # Core logic (PDF parsing, skill matching)
├── app.py # Streamlit web interface
├── requirements.txt # Python dependencies
└── data/ # Sample resume and job description

## 🔮 Future Improvements

- Support for DOCX resumes
- Advanced NLP using sentence-transformers
- ATS formatting compatibility checker
- Multilingual support

## 👩‍💻 Author

**Khushi Kumari**
- GitHub: [@khushisingh916228-droid](https://github.com/khushisingh916228-droid)
- LinkedIn: [khushi-kumari](https://linkedin.com/in/khushi-kumari-1a1308401)
