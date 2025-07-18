from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent  # ✅ New import

def main():
    print("👩‍🎓 Welcome to the Career Mentor Agent!")
    interests = input("What are your interests? 👉 ")

    # Step 1: Career Suggestion
    career_agent = CareerAgent()
    career = career_agent.suggest_career(interests)
    print(f"\n🌟 Based on your interests, a good career option is: **{career}**")

    # Step 2: Skill Roadmap
    skill_agent = SkillAgent()
    skills = skill_agent.show_skills(career)
    print("\n📘 Here's a skill roadmap for this career:")
    for i, skill in enumerate(skills, start=1):
        print(f"  {i}. {skill}")

    # ✅ Step 3: Job Suggestions
    job_agent = JobAgent()
    jobs = job_agent.show_jobs(career)
    print("\n💼 Here are some job opportunities you can explore:")
    for i, job in enumerate(jobs, start=1):
        print(f"  {i}. {job}")

if __name__ == "__main__":
    main()
