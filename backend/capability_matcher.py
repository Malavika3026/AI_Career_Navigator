def extract_capabilities(text):
    text = text.lower()

    mapping = {
        "problem solving": ["problem", "analysis", "model", "ml", "algorithm"],
        "teamwork": ["team", "collaborate", "intern", "worked with"],
        "communication": ["communication", "presentation", "document"],
        "clean code": ["clean", "structured", "scalable", "maintainable"],
        "debugging": ["debug", "test", "fix", "error"],
    }

    detected = []

    for cap, keywords in mapping.items():
        for k in keywords:
            if k in text:
                detected.append(cap)
                break

    return list(set(detected))


def match_capabilities(resume_text, jd_text):
    resume_caps = extract_capabilities(resume_text)
    jd_caps = extract_capabilities(jd_text)

    matched = [c for c in jd_caps if c in resume_caps]

    score = len(matched) / len(jd_caps) if jd_caps else 1

    return matched, jd_caps, score