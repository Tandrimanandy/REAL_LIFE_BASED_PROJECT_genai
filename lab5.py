# AI Study Assistant

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def study_assistant(topic):
    prompt = f"""
    You are an AI study assistant for college students.

    Topic:
    {topic}

    Explain the topic using the following structure:
    1. Simple Definition
    2. Easy Explanation
    3. Real-Life Example
    4. Important Points
    5. Three Interview Questions with Answers

    Use beginner-friendly language.
    Avoid unnecessary technical complexity.
    """
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text

topic = input("Enter a topic: ")
result = study_assistant(topic)

print("\nAI Study Assistant")
print("==================")
print(result)