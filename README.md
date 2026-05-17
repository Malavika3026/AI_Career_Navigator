# AI Career Navigator 🚀

An AI-powered career intelligence platform that analyzes how well a candidate’s resume matches a job description (JD), identifies skill gaps, and generates a personalized 30-day learning roadmap using LLMs and semantic similarity.

---

# 📌 Features

## ✅ Resume Parsing
- Upload resume PDFs
- Extracts structured text from resumes

## ✅ Job Description Analysis
- Upload JD PDFs
- OR enter target role + company
- AI extracts important technical requirements

## ✅ Semantic Skill Matching
- Uses sentence embeddings + cosine similarity
- Matches skills based on meaning, not exact keywords

### Example
- REST API ↔ API Development
- OOP ↔ Object-Oriented Programming

## ✅ Match Score Generation
Provides:
- Overall compatibility score
- Matched skills
- Missing skills

## ✅ Explainable AI Evaluation
LLM explains:
- Why the score was given
- Strengths of candidate
- Skill gaps
- Final hiring verdict

## ✅ 30-Day Personalized Roadmap
Generates:
- Daily learning tasks
- Focused skill-building plan
- Beginner-friendly progression

---

# 🧠 Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI / ML
- Llama 3.1 8B Instant (via Groq)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Cosine Similarity

## NLP / Processing
- PyMuPDF
- scikit-learn
- NumPy

---

# 🏗️ Project Architecture

```text
Resume PDF
   ↓
Text Extraction
   ↓
LLM Skill Extraction
   ↓
Skill Normalization
   ↓
Semantic Matching
   ↓
AI Evaluation
   ↓
Roadmap Generation
```

---

# 📂 Project Structure

```text
ai_career_navigator/

├── app.py
│
├── backend/
│   ├── parser.py
│   ├── extractor.py
│   ├── matcher.py
│   ├── normalizer.py
│   ├── experience.py
│   ├── roadmap.py
│   ├── explainer.py
│   └── jd_generator.py
│
├── models/
│   └── embedding_model.py
│
├── data/
│   ├── job_skills.csv
│   └── job_postings.csv
│
├── utils/
│   ├── config.py
│   └── prompts.py
│
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/Malavika3026/AI-Career-Navigator.git
cd AI-Career-Navigator
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv career_env
career_env\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv career_env
source career_env/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧪 Example Workflow

1. Upload Resume PDF
2. Upload Job Description PDF
3. Click **Analyze**
4. View:
   - Match Score
   - Matched Skills
   - Missing Skills
   - AI Evaluation
   - Personalized Roadmap

---

# 📊 AI Concepts Used

- Semantic Similarity
- Sentence Embeddings
- Cosine Similarity
- NLP-based Skill Extraction
- Prompt Engineering
- Explainable AI
- Hybrid AI Systems

---

# 🚀 Future Improvements

- Resume improvement suggestions
- Best-fit role recommendations
- Interview preparation module
- Skill confidence scoring
- Interactive dashboards & charts

---

# 📸 Sample Output

## Match Analysis
- Match Score
- Matched Skills
- Missing Skills

## AI Evaluation
- Strengths
- Skill gaps
- Hiring verdict

## 30-Day Roadmap
- Daily learning tasks
- Personalized improvement plan

---

# 🛠️ Libraries Used

```text
streamlit
groq
sentence-transformers
scikit-learn
numpy
PyMuPDF
python-dotenv
```

---

# 📄 License

This project is for educational and portfolio purposes.

---

# 👩‍💻 Author

Malavika Nair
