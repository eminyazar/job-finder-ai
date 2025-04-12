from fastapi import FastAPI, UploadFile, File, HTTPException
from app import cv_parser, recommender
from io import BytesIO

app = FastAPI()

@app.post("/upload-cv/")
async def upload_cv(file: UploadFile):
    try:
        content = await file.read()
        
        file_content = BytesIO(content)
        
        # Skill extraction
        skills = cv_parser.extract_skills(file_content)
        
        jobs = recommender.recommend(skills)

        return {"skills": skills, "recommended_jobs": jobs}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
