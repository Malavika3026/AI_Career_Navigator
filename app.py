import streamlit as st

# CACHE FUNCTIONS
@st.cache_data
def cached_extract(text):
    from backend.extractor import extract_structured_data
    return extract_structured_data(text)

@st.cache_data
def cached_match(resume_skills, jd_skills):
    from backend.matcher import match_skills
    return match_skills(resume_skills, jd_skills)

@st.cache_data
def cached_explain(resume_text, jd_text, matched, missing, score, user_exp, required_exp):
    from backend.explainer import generate_explanation
    return generate_explanation(resume_text, jd_text, matched, missing, score, user_exp, required_exp)

@st.cache_data
def cached_roadmap(role, skills, missing, exp):
    from backend.roadmap import generate_roadmap
    return generate_roadmap(role, skills, missing, exp)

from backend.parser import extract_text_from_pdf
from backend.extractor import extract_structured_data
from backend.normalizer import normalize_skills
from backend.matcher import match_skills
from backend.experience import extract_experience
from backend.roadmap import generate_roadmap
from backend.jd_generator import generate_jd
from backend.explainer import generate_explanation

# ---------------- UI ---------------- #
st.set_page_config(page_title="AI Career Navigator", layout="wide")

st.title("🚀 AI Career Navigator")

resume_file = st.file_uploader("📄 Upload Resume", type=["pdf"])
jd_file = st.file_uploader("📋 Upload JD", type=["pdf"])

role_input = st.text_input("🎯 Target Role")
company_input = st.text_input("🏢 Company (optional)")

# ---------------- MAIN ---------------- #
if st.button("🔍 Analyze"):

    if not resume_file:
        st.error("Upload resume first")
        st.stop()

    # ---------- Resume ---------- #
    resume_text = extract_text_from_pdf(resume_file)
    resume_data = cached_extract(resume_text)

    resume_skills = normalize_skills(resume_data.get("skills", []))
    user_exp = resume_data.get("experience_years", 0)

    # ---------- JD ---------- #
    if jd_file:
        jd_text = extract_text_from_pdf(jd_file)
    else:
        if not role_input:
            st.error("Upload JD or enter role")
            st.stop()
        jd_text = generate_jd(role_input, company_input)

    jd_data = extract_structured_data(jd_text)
    jd_skills = normalize_skills(jd_data.get("skills", []))

    required_exp = extract_experience(jd_text)

    # ---------- MATCHING ---------- #
    matched_skills, missing_skills, skill_score, sim_scores = cached_match(
    resume_skills, jd_skills)

    exp_score = min(user_exp / required_exp, 1) if required_exp else 1

    adjusted_skill_score = min(skill_score + 0.2, 1)  # boost for implicit skills
    final_score = (0.6 * adjusted_skill_score) + (0.4 * exp_score)

    # ---------- OUTPUT ---------- #
    st.header("📊 Match Score")
    st.metric("Score", f"{round(final_score * 100, 2)}%")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Skills")
        if matched_skills:
            for s in matched_skills:
                st.write(f"{s} ({sim_scores.get(s, '-')})")
        else:
            st.warning("No strong matches")

    with col2:
        st.subheader("❌ Missing Skills")
        st.write(", ".join(missing_skills) if missing_skills else "None")

    # ---------- EXPLANATION ---------- #
    st.header("🧠 AI Evaluation")

    with st.spinner("Analyzing..."):
        explanation = generate_explanation(
            resume_text,
            jd_text,
            matched_skills,
            missing_skills,
            final_score,
            user_exp,
            required_exp
        )

    st.write(explanation)

    # ---------- EXPERIENCE ---------- #
    st.header("📈 Experience")

    st.write(f"Your experience: {user_exp} years")
    st.write(f"Required: {required_exp} years")

    if user_exp < required_exp:
        st.warning("Experience gap detected")
    else:
        st.success("Experience matches")

    # ---------- ROADMAP ---------- #
    st.header("🗺️ Roadmap")

    with st.spinner("Generating roadmap..."):
        roadmap = generate_roadmap(
            role_input if role_input else jd_data.get("role", "target role"),
            resume_skills,
            missing_skills,
            user_exp
        )

    st.text(roadmap)