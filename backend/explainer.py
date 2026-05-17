from groq import Groq
from utils.config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_explanation(
    resume_text,
    jd_text,
    matched_skills,
    missing_skills,
    score,
    user_exp,
    required_exp
):

######################################################
#    prompt = f"""
#You are an expert AI career assistant.

#Analyze how well a candidate matches a job.

#--- CANDIDATE RESUME ---
#{resume_text[:2000]}

#--- JOB DESCRIPTION ---
#{jd_text[:2000]}

#--- MATCH DATA ---
#Matched Skills: {matched_skills}
#Missing Skills: {missing_skills}
#Match Score: {round(score*100,2)}%
#Candidate Experience: {user_exp} years
#Required Experience: {required_exp} years

#--- TASK ---
#Provide a structured analysis:

#1. Why this score was given (technical reasoning)
#2. Strengths of the candidate
#3. Critical skill gaps (especially domain-specific)
#4. Experience gap analysis
#5. Final verdict: Strong Fit / Moderate Fit / Weak Fit

#Keep it concise, realistic, and professional.
#"""
##########################################################
    prompt = f"""
You are an expert recruiter.

IMPORTANT:
- Infer skills from projects and experience
- Do NOT rely only on explicit keywords

Examples:
- ML project → problem solving, machine learning
- Django project → backend development, APIs
- Internship → teamwork, collaboration

DATA:
Resume:
{resume_text[:1500]}

JD:
{jd_text[:1500]}

Matched Skills: {matched_skills}
Missing Skills: {missing_skills}

TASK:
1. Correct wrong missing skills
2. Identify implicit skills
3. Explain real match quality
4. Give final verdict

Be realistic, not generic.
Do NOT assume skills, interests, or technologies unless clearly supported by resume or JD.
Do NOT speculate.
Only use evidence.
"""
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Explanation generation failed: {str(e)}"