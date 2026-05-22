from groq import Groq
from dotenv import load_dotenv
import os
import json

from modules.prompt_engine import build_prompt

# =========================================
# LOAD ENV
# =========================================

load_dotenv()

# =========================================
# GROQ CLIENT
# =========================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================================
# GENERATE SEO DATA
# =========================================

def generate_seo_data(project_data):

    prompt = build_prompt(project_data)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a real estate SEO expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    result = response.choices[0].message.content

    # Clean markdown JSON if returned
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)
