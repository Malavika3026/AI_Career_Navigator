from groq import Groq
from utils.config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def generate_jd(role, company=""):
    prompt = f"Generate a job description for {role} at {company}"

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content