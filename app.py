import streamlit as st

st.set_page_config(page_title="HR Recruiter Portal")

st.title("HR Recruiter Portal")
st.write("Welcome to the HR Recruiter Portal!")

name = st.text_input("Candidate Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
skills = st.text_area("Skills")
experience = st.selectbox("Experience", ["Fresher", "1-2 Years", "3-5 Years", "5+ Years"])

resume = st.file_uploader("Upload Resume", type=["pdf", "docx"])
if st.button("Submit"):
    st.success("Application Submitted Successfully!")

    st.write("### Candidate Details")
    st.write("**Name:**", name)
    st.write("**Email:**", email)
    st.write("**Phone:**", phone)
    st.write("**Skills:**", skills)
    st.write("**Experience:**", experience)

    if resume is not None:
        st.write("Resume Uploaded:", resume.name)
