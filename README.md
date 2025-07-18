# 💼 Career Mentor Agent

An intelligent multi-agent system that guides users in choosing a career path, learning the right skills, and discovering real-world job roles.

---

## 🤖 What It Does

This AI-powered system uses multiple agents to:
1. **Suggest a career path** based on user interests
2. **Show a skill roadmap** using a custom tool
3. **Provide job roles** based on the selected career

---

## 🧠 Agents Used

### 1. `CareerAgent`
- Takes user input (interests)
- Suggests a relevant career field

### 2. `SkillAgent`
- Uses the `get_career_roadmap()` tool
- Returns key skills needed for that career

### 3. `JobAgent`
- Uses the `get_job_roles()` tool
- Shows job roles, companies, and positions

---

## 🧰 Tools Used

### 🔧 `get_career_roadmap(career)`
Returns a list of skills for the selected career.

### 🔧 `get_job_roles(career)`
Returns a list of real-world job roles and companies hiring for that role.

---

## 🔁 Handoff Flow

User → CareerAgent → SkillAgent → JobAgent
Each agent passes context to the next agent smoothly.

---

## 📂 Project Structure
career-mentor-agent/
├── agents/
│ ├── career_agent.py
│ ├── skill_agent.py
│ └── job_agent.py
├── tools/
│ ├── career_roadmap.py
│ └── job_roles.py
├── main.py
├── requirements.txt
└── README.md

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt

Run the app:
python main.py

✨ Example Output

What are your interests? 👉 I love coding

🌟 Career Suggestion: Data Analyst
📘 Skill Roadmap:
  1. Learn Excel & SQL
  2. Master Python for Data
  3. Understand Data Visualization
  4. Build Dashboards

💼 Job Opportunities:
  1. Data Analyst at Daraz
  2. Junior Analyst at Airlift
  3. Excel Expert at K-Electric

👩‍💻 Made with ❤️ by Aliza Aleem
