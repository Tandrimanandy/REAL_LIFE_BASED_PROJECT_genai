# AI Product Description Generator

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_product_description(product_name, features):
    prompt = f"""
    You are an e-commerce product description writer.

    Product:
    {product_name}

    Features:
    {features}

    Write a professional product description.
    Requirements:
    - Start with a short introduction
    - Explain important features
    - Mention customer benefits
    - Use attractive but honest language
    - Do not invent specifications
    - Maximum 150 words
    """
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text

product_name = input("Enter product name: ")
features = input("Enter product features: ")

description = generate_product_description(product_name, features)

print("\nAI Generated Product Description:")
print(description)