from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Make sure .env file is set correctly.")

client = OpenAI(api_key=api_key)

def generate_project_script(project_data, language="English"):
    prompt = f"""
You are an AI real estate assistant. Generate a professional and engaging video script in {language}
for a real estate project using the details below:

Project Title: {project_data.get('Project Title', 'N/A')}
Location: {project_data.get('Location', 'N/A')}
Price: {project_data.get('Price', 'N/A')}
BHK Type: {project_data.get('BHK Type', 'N/A')}
Amenities: {', '.join(project_data.get('Amenities', [])) if isinstance(project_data.get('Amenities'), list) else project_data.get('Amenities')}

Make it sound like a YouTube video narrator. Add an intro, describe the project, highlight its features and end with a strong closing.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # <-- use this
        messages=[
            {"role": "system", "content": "You are a real estate video narrator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
