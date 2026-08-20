import streamlit as st
from main import analyze_resume

st.title("🎯 AI Resume Analyzer")
st.write("Apna resume upload karo aur job description paste karo — match score turant milega!")

uploaded_file = st.file_uploader("Resume upload karo (PDF)", type="pdf")
jd_text = st.text_area("Job Description paste karo yahan")

if st.button("Analyze"):
    if uploaded_file and jd_text:
        with open("data/temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        score, matched, missing = analyze_resume("data/temp_resume.pdf", jd_text)

        st.subheader(f"Match Score: {score:.1f}%")
        st.progress(score / 100)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ Matched Skills")
            if matched:
                for skill in sorted(matched):
                    st.markdown(f"- {skill.title()}")
            else:
                st.write("Koi match nahi mila")

        with col2:
            st.markdown("### ❌ Missing Skills")
            if missing:
                for skill in sorted(missing):
                    st.markdown(f"- {skill.title()}")
            else:
                st.write("Sab skills match ho gayi! 🎉")
    else:
        st.warning("Please resume upload karo aur JD bhi paste karo!")
        