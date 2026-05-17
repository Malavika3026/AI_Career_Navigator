EXTRACTION_PROMPT = """
Extract structured information from the following text.

Return JSON with:
- skills (list)
- tools (list)
- experience_years (number if possible, else 0)
- role (string)

Text:
{input_text}
"""

ROADMAP_PROMPT = """
Create a 30-day roadmap.

Role: {role}
Current Skills: {current_skills}
Missing Skills: {missing_skills}
Experience Level: {experience}

IMPORTANT:
- Only 3 tasks per day
- Each task should take 1–2 hours
- Keep tasks simple and focused
- Avoid combining multiple topics in one task
- Only include skills directly missing from JD
- Avoid advanced tools (Dockers, Kubernetes, etc.)

3 tasks per day only.
"""