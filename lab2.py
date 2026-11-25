# AI Resume Improvement Assistant


import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_resume_summary(skills):
    prompt = f"""
    You are an expert resume writer.

    Student skills:
    {skills}

    Create a professional resume summary for a fresher.
    Requirements:
    - 4 to 5 sentences
    - Professional language
    - Suitable for an IT job
    - Do not exaggerate skills
    - Mention willingness to learn
    """
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text

skills = input("Enter your skills: ")
summary = generate_resume_summary(skills)

print("\nGenerated Resume Summary:")
print(summary)