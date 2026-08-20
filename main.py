import pdfplumber

skills_list = [
    "python", "java", "sql", "machine learning", "deep learning",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "power bi", "tableau", "nlp", "computer vision", "aws",
    "azure", "docker", "git", "github", "mlops", "excel",
    "data visualization", "statistics", "communication"
]

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_skills(text, skills_list):
    text_lower = text.lower()
    found_skills = []
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)
    return found_skills

def calculate_match(resume_skills, jd_skills):
    matched_skills = set(resume_skills) & set(jd_skills)
    missing_skills = set(jd_skills) - set(resume_skills)
    match_percentage = (len(matched_skills) / len(jd_skills)) * 100
    return match_percentage, matched_skills, missing_skills

def analyze_resume(pdf_path, jd_text):
    resume_text = extract_text_from_pdf(pdf_path)
    resume_skills = extract_skills(resume_text, skills_list)
    jd_skills = extract_skills(jd_text, skills_list)
    match_percentage, matched, missing = calculate_match(resume_skills, jd_skills)
    return match_percentage, matched, missing

# Testing ke liye (jab isko seedha run karo)
if __name__ == "__main__":
    with open("data/job_description.txt", "r", encoding="utf-8") as file:
        jd_text = file.read()

    score, matched, missing = analyze_resume("data/resume.pdf", jd_text)

    print(f"Match Score: {score:.1f}%")
    print(f"Matched Skills: {list(matched)}")
    print(f"Missing Skills: {list(missing)}")