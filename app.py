import streamlit as st
import sqlite3
import database

st.set_page_config(page_title="HR Recruiter Portal")
conn = sqlite3.connect("hr_portal.db")
cursor = conn.cursor()

st.title("HR Recruiter Portal")
st.write("Welcome to the HR Recruiter Portal!")

name = st.text_input("Candidate Name")
st.write("Your Name:", name)

email = st.text_input("Email")
st.write("Your Email:", email)

phone = st.text_input("Phone Number")
st.write("Your Phone Number:", phone)

if phone and not phone.isdigit():
    st.error("Phone Number should contain only digits.")

elif phone and len(phone) != 10:
    st.warning("Phone Number should be exactly 10 digits.")

skills = st.text_area("Skills")
st.write("Your Skills:", skills)

experience = st.selectbox("Experience", ["Fresher", "1-2 Years", "3-5 Years", "5+ Years"])
st.write("Experience:", experience)

resume = st.file_uploader("Upload Resume", type=["pdf", "docx"])
if resume is not None:
    st.write("Uploaded Resume:", resume.name)

if st.button("Submit"):

    cursor.execute("""
    INSERT INTO candidates(name, email, phone, skills, experience, resume)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        email,
        phone,
        skills,
        experience,
        resume.name if resume else ""
    ))

    conn.commit()

    st.success("Application Submitted Successfully!")
    st.write("### Candidate Details")
st.write("**Name:**", name)
st.write("**Email:**", email)
st.write("**Phone:**", phone)
st.write("**Skills:**", skills)
st.write("**Experience:**", experience)

if resume is not None:
    st.write("**Resume Uploaded:**", resume.name)

    st.write("---")
st.subheader("All Applications")
cursor.execute("SELECT * FROM candidates")
data = cursor.fetchall() 

for row in data:
    st.write("Name:", row[1])
    st.write("Email:", row[2])
    st.write("Phone:", row[3])
    st.write("Skills:", row[4])
    st.write("Experience:", row[5])
    st.write("Resume:", row[6])
    st.write("--------------------")
st.write("---")
st.subheader("Search Candidate")

search_name = st.text_input("Search Candidate by Name")

if st.button("Search"):

    cursor.execute(
        "SELECT * FROM candidates WHERE name=?",
        (search_name,)
    )

    result = cursor.fetchall()

    if result:
        for row in result:
            st.write("Name:", row[1])
            st.write("Email:", row[2])
            st.write("Phone:", row[3])
            st.write("Skills:", row[4])
            st.write("Experience:", row[5])
            st.write("Resume:", row[6])
            st.write("----------------------")
    else:
        st.error("Candidate Not Found")

        st.write("---")
st.subheader("Delete Candidate")

st.write("---")
st.subheader("Update Candidate Email")

update_name = st.text_input("Candidate Name", key="update_name")
new_email = st.text_input("New Email",  key="new_email")

if st.button("Update Email"):
    cursor.execute(
        "UPDATE candidates SET email=? WHERE name=?",
        (new_email, update_name)
    )
    conn.commit()
    st.success("Email Updated Successfully!")
delete_name = st.text_input("Enter Candidate Name to Delete")

if st.button("Delete"):
    cursor.execute("DELETE FROM candidates WHERE name=?", (delete_name,))
    conn.commit()
    st.success("Candidate Deleted Successfully!")

cursor.execute("SELECT * FROM candidates")
data = cursor.fetchall()

for row in data:
    st.write("Name:", row[1])
    st.write("Email:", row[2])
    st.write("Phone:", row[3])
    st.write("Skills:", row[4])
    st.write("Experience:", row[5])
    st.write("Resume:", row[6])
    st.write("----------------------")

st.write("---")
cursor.execute("SELECT COUNT(*) FROM candidates")
count = cursor.fetchone()[0]
st.write("### Total Applications:", count)
st.write("----")

st.subheader("Dashboard")
st.write("Total Candidates:", count)
st.write("HR Recruiter Portal is Working Successfully ✅")
st.write("----------------------------")
st.success("Project Completed Successfully 🎉")
st.write("---")
st.info("Developed by Sneha Gupta")