import openai
import json
from config import MODEL_NAME
from prompt_templates import recommend_prompt

def recommend_career(personality, skills):
    skill_str = ", ".join(skills)
    prompt = recommend_prompt.format(personality=personality, skills=skill_str)

    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
