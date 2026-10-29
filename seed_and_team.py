"""
Seed 20 random students into the database and generate 5 teams of 4.
Run: .venv/Scripts/python.exe seed_and_team.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from database import init_db, add_student, get_students, get_student
from algorithm import generate_teams, build_report, metrics

# ---------- 20 realistic student profiles ----------
STUDENTS = [
    {"student_id":"2025001","name":"Aarav Sharma","email":"aarav@college.edu","branch":"AI & ML","year":"3rd Year",
     "python":9,"cpp":6,"java":5,"machine_learning":8,"web_development":4,"sql":6,"uiux":3,"data_science":8,"cloud":5,
     "communication":7,"leadership":6,"teamwork":8,"problem_solving":9,
     "interests":"Artificial Intelligence, Machine Learning","preferred_role":"ML Developer","experience":"High"},

    {"student_id":"2025002","name":"Priya Patel","email":"priya@college.edu","branch":"CSE","year":"3rd Year",
     "python":7,"cpp":5,"java":8,"machine_learning":5,"web_development":9,"sql":7,"uiux":6,"data_science":4,"cloud":6,
     "communication":8,"leadership":5,"teamwork":9,"problem_solving":7,
     "interests":"Web Development, App Development","preferred_role":"Web Developer","experience":"Medium"},

    {"student_id":"2025003","name":"Rohan Mehta","email":"rohan@college.edu","branch":"AI & DS","year":"4th Year",
     "python":8,"cpp":4,"java":3,"machine_learning":9,"web_development":3,"sql":8,"uiux":2,"data_science":9,"cloud":7,
     "communication":6,"leadership":8,"teamwork":7,"problem_solving":9,
     "interests":"Data Science, Machine Learning","preferred_role":"Data Analyst","experience":"Expert"},

    {"student_id":"2025004","name":"Sneha Kulkarni","email":"sneha@college.edu","branch":"IT","year":"2nd Year",
     "python":5,"cpp":3,"java":6,"machine_learning":4,"web_development":8,"sql":5,"uiux":9,"data_science":3,"cloud":4,
     "communication":9,"leadership":4,"teamwork":8,"problem_solving":6,
     "interests":"Web Development, App Development","preferred_role":"UI/UX Designer","experience":"Beginner"},

    {"student_id":"2025005","name":"Vikram Singh","email":"vikram@college.edu","branch":"CSE","year":"4th Year",
     "python":7,"cpp":9,"java":7,"machine_learning":6,"web_development":5,"sql":9,"uiux":3,"data_science":5,"cloud":8,
     "communication":7,"leadership":9,"teamwork":7,"problem_solving":8,
     "interests":"Cloud, Cyber Security","preferred_role":"Database Developer","experience":"High"},

    {"student_id":"2025006","name":"Ananya Desai","email":"ananya@college.edu","branch":"AI & ML","year":"3rd Year",
     "python":8,"cpp":5,"java":4,"machine_learning":9,"web_development":6,"sql":5,"uiux":4,"data_science":8,"cloud":6,
     "communication":8,"leadership":7,"teamwork":9,"problem_solving":8,
     "interests":"Artificial Intelligence, Data Science","preferred_role":"ML Developer","experience":"Medium"},

    {"student_id":"2025007","name":"Karan Joshi","email":"karan@college.edu","branch":"CSE","year":"2nd Year",
     "python":6,"cpp":7,"java":6,"machine_learning":4,"web_development":7,"sql":6,"uiux":7,"data_science":3,"cloud":5,
     "communication":6,"leadership":5,"teamwork":7,"problem_solving":6,
     "interests":"Web Development, IoT","preferred_role":"Web Developer","experience":"Beginner"},

    {"student_id":"2025008","name":"Neha Tiwari","email":"neha@college.edu","branch":"AI & DS","year":"3rd Year",
     "python":9,"cpp":3,"java":4,"machine_learning":7,"web_development":5,"sql":9,"uiux":3,"data_science":9,"cloud":6,
     "communication":7,"leadership":6,"teamwork":8,"problem_solving":9,
     "interests":"Data Science, Machine Learning","preferred_role":"Data Analyst","experience":"High"},

    {"student_id":"2025009","name":"Arjun Reddy","email":"arjun@college.edu","branch":"ECE","year":"3rd Year",
     "python":5,"cpp":8,"java":6,"machine_learning":5,"web_development":4,"sql":5,"uiux":6,"data_science":4,"cloud":9,
     "communication":7,"leadership":6,"teamwork":7,"problem_solving":7,
     "interests":"IoT, Cloud, Robotics","preferred_role":"Team Member","experience":"Medium"},

    {"student_id":"2025010","name":"Pooja Nair","email":"pooja@college.edu","branch":"IT","year":"4th Year",
     "python":7,"cpp":4,"java":5,"machine_learning":6,"web_development":8,"sql":7,"uiux":8,"data_science":5,"cloud":5,
     "communication":9,"leadership":8,"teamwork":9,"problem_solving":7,
     "interests":"Web Development, App Development","preferred_role":"Team Leader","experience":"High"},

    {"student_id":"2025011","name":"Rahul Gupta","email":"rahul@college.edu","branch":"CSE","year":"2nd Year",
     "python":6,"cpp":6,"java":7,"machine_learning":4,"web_development":6,"sql":6,"uiux":5,"data_science":4,"cloud":5,
     "communication":6,"leadership":4,"teamwork":7,"problem_solving":6,
     "interests":"Web Development, Cyber Security","preferred_role":"Web Developer","experience":"Beginner"},

    {"student_id":"2025012","name":"Divya Menon","email":"divya@college.edu","branch":"AI & ML","year":"4th Year",
     "python":9,"cpp":5,"java":3,"machine_learning":9,"web_development":4,"sql":6,"uiux":4,"data_science":9,"cloud":7,
     "communication":8,"leadership":9,"teamwork":8,"problem_solving":9,
     "interests":"Artificial Intelligence, Machine Learning, Data Science","preferred_role":"Researcher","experience":"Expert"},

    {"student_id":"2025013","name":"Aditya Kumar","email":"aditya@college.edu","branch":"CSE","year":"3rd Year",
     "python":7,"cpp":8,"java":7,"machine_learning":5,"web_development":7,"sql":8,"uiux":4,"data_science":5,"cloud":7,
     "communication":7,"leadership":6,"teamwork":7,"problem_solving":8,
     "interests":"Cloud, Cyber Security","preferred_role":"Database Developer","experience":"Medium"},

    {"student_id":"2025014","name":"Ishita Shah","email":"ishita@college.edu","branch":"IT","year":"2nd Year",
     "python":4,"cpp":3,"java":5,"machine_learning":3,"web_development":7,"sql":4,"uiux":9,"data_science":3,"cloud":4,
     "communication":8,"leadership":5,"teamwork":8,"problem_solving":5,
     "interests":"Web Development, App Development","preferred_role":"UI/UX Designer","experience":"Beginner"},

    {"student_id":"2025015","name":"Siddharth Rao","email":"sid@college.edu","branch":"AI & DS","year":"4th Year",
     "python":8,"cpp":6,"java":4,"machine_learning":8,"web_development":5,"sql":7,"uiux":3,"data_science":9,"cloud":8,
     "communication":7,"leadership":7,"teamwork":8,"problem_solving":9,
     "interests":"Data Science, Artificial Intelligence, Cloud","preferred_role":"Data Analyst","experience":"Expert"},

    {"student_id":"2025016","name":"Meera Iyer","email":"meera@college.edu","branch":"CSE","year":"3rd Year",
     "python":6,"cpp":5,"java":8,"machine_learning":4,"web_development":9,"sql":6,"uiux":7,"data_science":4,"cloud":5,
     "communication":9,"leadership":6,"teamwork":9,"problem_solving":7,
     "interests":"Web Development, App Development","preferred_role":"Web Developer","experience":"Medium"},

    {"student_id":"2025017","name":"Tanmay Bhat","email":"tanmay@college.edu","branch":"ECE","year":"2nd Year",
     "python":5,"cpp":7,"java":5,"machine_learning":4,"web_development":4,"sql":5,"uiux":5,"data_science":4,"cloud":7,
     "communication":6,"leadership":5,"teamwork":6,"problem_solving":6,
     "interests":"IoT, Robotics, Cloud","preferred_role":"Team Member","experience":"Beginner"},

    {"student_id":"2025018","name":"Shreya Jain","email":"shreya@college.edu","branch":"AI & ML","year":"3rd Year",
     "python":8,"cpp":4,"java":3,"machine_learning":8,"web_development":5,"sql":5,"uiux":6,"data_science":7,"cloud":5,
     "communication":8,"leadership":7,"teamwork":8,"problem_solving":8,
     "interests":"Artificial Intelligence, Machine Learning","preferred_role":"ML Developer","experience":"Medium"},

    {"student_id":"2025019","name":"Nikhil Verma","email":"nikhil@college.edu","branch":"CSE","year":"4th Year",
     "python":7,"cpp":9,"java":8,"machine_learning":5,"web_development":6,"sql":8,"uiux":3,"data_science":5,"cloud":8,
     "communication":7,"leadership":8,"teamwork":7,"problem_solving":8,
     "interests":"Cyber Security, Cloud","preferred_role":"Database Developer","experience":"High"},

    {"student_id":"2025020","name":"Kavya Pillai","email":"kavya@college.edu","branch":"AI & DS","year":"2nd Year",
     "python":6,"cpp":3,"java":4,"machine_learning":6,"web_development":6,"sql":5,"uiux":7,"data_science":6,"cloud":4,
     "communication":8,"leadership":5,"teamwork":8,"problem_solving":7,
     "interests":"Data Science, Artificial Intelligence, App Development","preferred_role":"Data Analyst","experience":"Beginner"},
]

def main():
    init_db()

    # Insert students (skip if already exists)
    inserted = 0
    for s in STUDENTS:
        if not get_student(s["student_id"]):
            add_student(s)
            inserted += 1
            print(f"  Added: {s['name']} ({s['student_id']})")
        else:
            print(f"  Skipped (exists): {s['name']}")

    print(f"\n✅ Inserted {inserted} new students.")

    # Generate 5 teams of 4
    all_students = get_students()
    print(f"   Total students in DB: {len(all_students)}")

    teams, error = generate_teams(all_students, team_size=4, iterations=500, seed=42)
    if error:
        print(f"❌ Error: {error}")
        return

    # Print team report
    report = build_report(teams)
    print(f"\n🏆 Generated {len(teams)} teams:\n")
    for i, team in enumerate(teams, 1):
        m = metrics(team)
        print(f"━━━ Team {i} ━━━  Score: {m['Team Score']}/100  |  Coverage: {m['Skill Coverage']}%  |  Compatibility: {m['Compatibility']}%")
        for s in team:
            print(f"   • {s['name']:<20} {s['preferred_role']:<20} Exp: {s['experience']}")
        print()

    report.to_csv("team_report.csv", index=False)
    print("📄 Full report saved to team_report.csv")

if __name__ == "__main__":
    main()
