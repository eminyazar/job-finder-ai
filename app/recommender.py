job_database = {
    "python developer": [
        "python", "django", "fastapi", "flask", "sql", "rest api", "git", "linux"
    ],
    "data scientist": [
        "python", "machine learning", "deep learning", "data analysis", "sql",
        "data visualization", "pandas", "numpy", "scikit-learn", "tensorflow", "power bi"
    ],
    "frontend developer": [
        "javascript", "typescript", "react", "vue", "angular", "next.js", "html", "css", "tailwind"
    ],
    "backend developer": [
        "python", "django", "fastapi", "node.js", "java", "spring", "php", "laravel",
        "sql", "mysql", "mongodb", "docker", "linux", "rest api"
    ],
    "full stack developer": [
        "python", "django", "fastapi", "javascript", "react", "node.js",
        "sql", "docker", "linux", "rest api", "graphql", "git"
    ],
    "mobile developer": [
        "flutter", "kotlin", "swift", "react native", "firebase", "api", "rest api"
    ],
    "devops engineer": [
        "aws", "azure", "gcp", "docker", "kubernetes", "linux",
        "gitlab", "jenkins", "terraform", "cloud computing", "ci/cd"
    ],
    "cloud engineer": [
        "aws", "azure", "gcp", "docker", "kubernetes", "linux", "terraform", "cloud computing"
    ],
    "data engineer": [
        "python", "sql", "mysql", "postgresql", "mongodb", "aws",
        "etl", "big data", "linux", "data analysis", "cloud computing"
    ],
    "business analyst": [
        "excel", "sql", "power bi", "tableau", "data analysis", "communication", "problem solving", "agile", "scrum"
    ],
    "machine learning engineer": [
        "python", "machine learning", "deep learning", "tensorflow", "pytorch", "sql",
        "data analysis", "docker", "cloud computing"
    ],
    "project manager": [
        "agile", "scrum", "jira", "communication", "leadership", "problem solving", "english"
    ],
}

def recommend(skills):
    """
    Verilen becerilere dayalı iş önerileri yapar.
    
    :param skills: Kullanıcının CV'sinden çıkarılan beceriler
    :return: İlgili iş önerileri
    """
    recommended_jobs = []
    
    for job, required_skills in job_database.items():

        common_skills = set(skills) & set(required_skills)
        
        if len(common_skills) >= 2:
            recommended_jobs.append({
                "job": job,
                "common_skills": list(common_skills),
            })
    
    if not recommended_jobs:
        recommended_jobs.append({"job": "No matching jobs found", "common_skills": []})
    
    return recommended_jobs
