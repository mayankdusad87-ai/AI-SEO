from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from modules.prompt_engine import build_prompt

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# API CLIENT
# =========================================

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

# =========================================
# GENERATE SEO DATA
# =========================================

def generate_seo_data(project_data):

    prompt = build_prompt(project_data)

    response = client.chat.completions.create(
        model="grok-2-latest",
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
        temperature=0.7
    )

    result = response.choices[0].message.content

    return json.loads(result)
