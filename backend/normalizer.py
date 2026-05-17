def normalize_skills(skills):
    return list(set([s.strip().lower() for s in skills if s]))

def filter_skills(skills):
    bad_keywords = [
        "communication", "leadership", "team",
        "management", "engagement", "monitoring",
        "candidate", "interview", "proctoring",
        "mentorship", "adaptability", "learning"
    ]

    clean = []

    for s in skills:
        if not any(b in s.lower() for b in bad_keywords):
            if len(s.split()) <= 3:  # remove long phrases
                clean.append(s)

    return clean