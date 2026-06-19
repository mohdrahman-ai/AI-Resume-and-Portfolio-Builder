import streamlit as st

st.title("AI Resume & Portfolio Builder")

name = st.text_input("Name")
education = st.text_area("Education")
skills = st.text_area("Skills")
projects = st.text_area("Projects")
certifications = st.text_area("Certifications")

if st.button("Generate Resume"):

   
    resume = f"""
# {name}

## Professional Summary
Motivated Computer Science student with skills in {skills}.

## Education
{education}

## Projects
{projects}

## Certifications
{certifications}

## About Me
Passionate about AI, Data Analytics, and problem solving.
"""

st.markdown(resume)

st.download_button(
    "Download Resume",
    resume,
    file_name="resume.txt"
)
if "python" in skills.lower():
    st.success("Recommended Role: Data Analyst / Python Developer")

if len(skills.split(",")) > 3:
    st.success("ATS Score: 85/100")
else:
    st.warning("ATS Score: 60/100 - Add more skills")