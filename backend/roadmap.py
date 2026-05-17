from groq import Groq
from utils.config import GROQ_API_KEY, MODEL_NAME
from utils.prompts import ROADMAP_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def generate_roadmap(role, current_skills, missing_skills, experience):
    prompt = ROADMAP_PROMPT.format(
        role=role,
        current_skills=current_skills,
        missing_skills=missing_skills,
        experience=experience
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content