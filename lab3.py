# AI Meeting Summary Generator

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_meeting(meeting_text):
    prompt = f"""
    You are an AI meeting assistant.

    Analyze the following meeting transcript:
    {meeting_text}

    Generate the following:
    1. Meeting Summary
    2. Important Decisions
    3. Action Items
    4. Person Responsible

    Use simple and professional language.
    """
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text

meeting = """
Manager: We need to complete the website by Friday.
Developer: The login module is almost complete.
Tester: I will start testing on Thursday.
Manager: Please fix all critical bugs before Friday.
Developer: I will complete the remaining API work tomorrow.
"""

result = summarize_meeting(meeting)

print("\nAI Meeting Summary")
print("------------------")
print(result)