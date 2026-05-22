from groq import Groq
from dotenv import load_dotenv
import os
import json

from modules.prompt_engine import build_prompt

# =========================================
# LOAD ENV VARIABLES
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
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are an expert real estate SEO strategist."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
    )

    result = response.choices[0].message.content

    # Clean markdown JSON if model returns ```json
    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)
