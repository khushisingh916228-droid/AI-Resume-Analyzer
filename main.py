import pdfplumber

skills_list = [
    "python", "java", "sql", "machine learning", "deep learning",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "power bi", "tableau", "nlp", "computer vision", "aws",
    "azure", "docker", "git", "github", "mlops", "excel",
    "data visualization", "statistics", "communication",
    "django", "flask", "api development", "react", "html", "css",
    "javascript", "responsive design",
    "data science", "data analytics", "analytics", "data analysis",
    "business analysis", "kubernetes", "linux", "spark",
    "generative ai", "llm", "prompt engineering", "cybersecurity",
    "product management", "agile", "figma", "testing"
]

def extract_text_from_pdf(pdf_path):
    """PDF se text nikalta hai. Corrupt/password-protected/scanned PDF ho to bhi crash nahi hota."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                except Exception:
                    continue
        return text
    except Exception:
        return ""

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

    if len(jd_skills) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(matched_skills) / len(jd_skills)) * 100

    return match_percentage, matched_skills, missing_skills

def generate_recommendation(score, missing_skills):
    """Rule-based recommendation (does NOT use Gemini, so no quota is consumed)."""
    if score >= 80:
        base = "Excellent match! Your skills strongly align with this job description."
    elif score >= 50:
        base = "Decent match, but a few important skills are still missing."
    else:
        base = "Match is quite low — there's a significant skill gap for this role."

    if missing_skills:
        top_missing = sorted(missing_skills)[:3]
        skill_text = ", ".join(s.title() for s in top_missing)
        base += f" Improving {skill_text} could boost your match score."
    else:
        base += " No missing skills — your resume is well-suited for this JD."

    return base

def analyze_resume(pdf_path, jd_text):
    resume_text = extract_text_from_pdf(pdf_path)

    if not resume_text.strip():
        return 0, set(), set(), []

    resume_skills = extract_skills(resume_text, skills_list)
    jd_skills = extract_skills(jd_text, skills_list)
    match_percentage, matched, missing = calculate_match(resume_skills, jd_skills)
    return match_percentage, matched, missing, resume_skills

if __name__ == "__main__":
    with open("data/job_description.txt", "r", encoding="utf-8") as file:
        jd_text = file.read()

    score, matched, missing, resume_skills = analyze_resume("data/resume.pdf", jd_text)

    print(f"Match Score: {score:.1f}%")
    print(f"Matched Skills: {list(matched)}")
    print(f"Missing Skills: {list(missing)}")
    print(f"All Resume Skills: {resume_skills}")