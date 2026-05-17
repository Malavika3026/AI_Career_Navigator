from sklearn.metrics.pairwise import cosine_similarity
from models.embedding_model import get_embeddings

def match_skills(resume_skills, jd_skills):
    if not resume_skills or not jd_skills:
        return [], jd_skills, 0.4, {}

    res_emb = get_embeddings(resume_skills)
    jd_emb = get_embeddings(jd_skills)

    sim_matrix = cosine_similarity(res_emb, jd_emb)

    matched = set()
    sim_scores = {}

    for i, r in enumerate(resume_skills):
        best_score = 0
        best_match = None

        for j, j_skill in enumerate(jd_skills):
            score = sim_matrix[i][j]

            if score > best_score:
                best_score = score
                best_match = j_skill

        # 🔥 LOWER threshold
        if best_score > 0.5 and best_score < 0.95:
            matched.add(best_match)
            sim_scores[best_match] = round(float(best_score), 2)

    matched = list(matched)
    missing = [s for s in jd_skills if s not in matched]

    skill_score = len(matched) / max(len(jd_skills), 1)

    return matched, missing, skill_score, sim_scores