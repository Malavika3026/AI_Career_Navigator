from groq import Groq
import json
import re
from utils.config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def safe_json_parse(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except:
                pass
    return None


def fallback_extract(text):
    text = text.lower()

    common_skills = [
        "python", "java", "sql", "django", "fastapi",
        "machine learning", "ml", "nlp", "api", "rest",
        "data structures", "algorithms", "javascript"
    ]

    return list(set([s for s in common_skills if s in text]))


def extract_structured_data(text):

    prompt = f"""
Extract ONLY important job skills.

STRICT RULES:
- Include ONLY technical skills and core requirements
- Ignore company features, products, descriptions
- Ignore generic phrases (e.g., communication, leadership)
- Ignore long phrases
- Keep list SHORT (max 10–15 skills)

GOOD examples:
- python
- data structures
- api
- django
- sql

BAD examples:
- team collaboration
- candidate engagement
- cloud scalability (unless explicitly required)

Return JSON:
{{
 "skills": [],
 "experience_years": 0,
 "role": ""
}}

Text:
{text[:3000]}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content

        data = safe_json_parse(content)

        if not data or not data.get("skills"):
            raise ValueError("Bad extraction")

        return data

    except Exception as e:
        print("Extraction fallback used:", e)

        return {
            "skills": fallback_extract(text),
            "experience_years": 0,
            "role": ""
        }