# AI Customer Support Reply Generator

import os
from dotenv import load_dotenv
from google import genai

# 1. Load API key and initialize client
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Define the generator function
def generate_reply(complaint):
    prompt = f"""
    You are a professional customer support executive.

    Customer complaint:
    {complaint}

    Write a polite and professional response.
    The response should:
    - Apologize for the inconvenience
    - Acknowledge the problem
    - Offer a reasonable solution
    - Be friendly
    - Be less than 100 words
    """
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text

# 3. Get user input and print the result
complaint = input("Enter customer complaint: ")
reply = generate_reply(complaint)

print("\nAI Generated Response:")
print(reply)
