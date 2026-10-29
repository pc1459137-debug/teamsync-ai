import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("team_formation.db")
SKILLS = ["python", "cpp", "java", "machine_learning", "web_development", "sql", "uiux", "data_science", "cloud"]
SOFT = ["communication", "leadership", "teamwork", "problem_solving"]
COLUMNS = ["student_id", "name", "email", "branch", "year"] + SKILLS + SOFT + ["interests", "preferred_role", "experience"]

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY, name TEXT NOT NULL, email TEXT, branch TEXT, year TEXT,
        python INTEGER DEFAULT 5, cpp INTEGER DEFAULT 5, java INTEGER DEFAULT 5,
        machine_learning INTEGER DEFAULT 5, web_development INTEGER DEFAULT 5, sql INTEGER DEFAULT 5,
        uiux INTEGER DEFAULT 5, data_science INTEGER DEFAULT 5, cloud INTEGER DEFAULT 5,
        communication INTEGER DEFAULT 5, leadership INTEGER DEFAULT 5, teamwork INTEGER DEFAULT 5,
        problem_solving INTEGER DEFAULT 5, interests TEXT, preferred_role TEXT, experience TEXT)""")
    _seed_demo_data()

def _seed_demo_data():
    """Insert 20 demo students on first run if the table is empty."""
    with get_connection() as conn:
        count = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    if count > 0:
        return
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
    for s in STUDENTS:
        add_student(s)

def add_student(s):
    with get_connection() as conn:
        cols = ", ".join(COLUMNS)
        marks = ", ".join(["?"] * len(COLUMNS))
        conn.execute(f"INSERT INTO students ({cols}) VALUES ({marks})", [s.get(c, "") for c in COLUMNS])

def get_students():
    with get_connection() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM students ORDER BY name").fetchall()]

def get_student(sid):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM students WHERE student_id=?", (sid,)).fetchone()
        return dict(row) if row else None

def update_student(sid, s):
    fields = [c for c in COLUMNS if c != "student_id"]
    with get_connection() as conn:
        conn.execute(
            "UPDATE students SET " + ", ".join(f"{c}=?" for c in fields) + " WHERE student_id=?",
            [s.get(c, "") for c in fields] + [sid]
        )
