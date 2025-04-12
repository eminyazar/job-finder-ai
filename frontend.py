import streamlit as st
import requests

# FastAPI backend API URL
API_URL = "http://localhost:8000/upload-cv/"

# Page setup
st.set_page_config(page_title="CV Analyzer & Job Recommendation System", layout="centered")
st.title("📄 CV Analyzer & Job Recommendation System")
st.markdown("Upload your CV to analyze your skills and receive job suggestions based on your profile.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload Your CV (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success(f"✅ Uploaded file: {uploaded_file.name}")

    # Read file content
    file_content = uploaded_file.getvalue()

    try:
        # Send to backend API
        with st.spinner("🔍 Analyzing your CV..."):
            response = requests.post(API_URL, files={"file": uploaded_file})
        
        # Handle response
        if response.status_code == 200:
            data = response.json()

            # Extracted skills
            st.markdown("### 🧠 Extracted Skills")
            st.markdown(", ".join(data["skills"]))

            # Recommended jobs
            st.markdown("### 💼 Recommended Jobs with LinkedIn Search Links")

            for job in data["recommended_jobs"]:
                job_title = job["job"].title()
                common_skills = ", ".join(job["common_skills"])
                linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={job_title.replace(' ', '%20')}"
                
                with st.container():
                    st.markdown(f"""
                    <div style='padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-bottom: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                        <h5 style='margin: 0;'>{job_title}</h5>
                        <p style='margin: 5px 0;'><b>Matching Skills:</b> {common_skills}</p>
                        <a href="{linkedin_url}" target="_blank">🔗 Search on LinkedIn</a>
                    </div>
                    """, unsafe_allow_html=True)

        else:
            st.error(f"❌ Server returned an error: {response.status_code}")

    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {e}")
