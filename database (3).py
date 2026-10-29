import sqlite3
import random
from pathlib import Path

DB_PATH = Path(__file__).with_name("team_formation.db")
SKILLS = ["python","cpp","java","machine_learning","web_development","sql","uiux","data_science","cloud"]
SOFT = ["communication","leadership","teamwork","problem_solving"]
COLUMNS = ["student_id","name","email","branch","year"] + SKILLS + SOFT + ["interests","preferred_role","experience"]

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
        conn.execute("UPDATE students SET " + ", ".join(f"{c}=?" for c in fields) + " WHERE student_id=?",
                     [s.get(c, "") for c in fields] + [sid])


def seed_demo_students(force=False):
    """Insert fictional demo profiles. By default, seed only an empty database.
    With force=True, add any missing demo profiles without touching existing records.
    """
    existing = get_students()
    if existing and not force:
        return 0
    existing_ids = {str(s.get("student_id", "")) for s in existing}
    rng = random.Random(20261029)
    names = [
        "Aarav Patil", "Ananya Sharma", "Vivaan Kulkarni", "Isha Deshmukh",
        "Aditya Joshi", "Saanvi More", "Arjun Pawar", "Diya Shah",
        "Reyansh Jadhav", "Kavya Nair", "Atharv Shinde", "Myra Gupta",
        "Rudra Chavan", "Aditi Mehta", "Ishaan Bhosale", "Sara Khan",
        "Vedant Kale", "Riya Verma", "Omkar Gaikwad", "Neha Suryawanshi"
    ]
    roles = ["ML Developer", "Web Developer", "Data Analyst", "UI/UX Designer",
             "Database Developer", "Team Leader", "Researcher", "Team Member"]
    interests_pool = ["Artificial Intelligence", "Machine Learning", "Data Science",
                      "Web Development", "App Development", "Cyber Security", "Cloud", "IoT"]
    branches = ["AI & ML", "CSE", "AI & DS", "IT", "ECE"]
    experiences = ["None", "Beginner", "Medium", "High", "Expert"]
    inserted = 0
    for i, name in enumerate(names, start=1):
        demo_id = f"DEMO2026{i:03d}"
        if demo_id in existing_ids:
            continue
        profile = {
            "student_id": demo_id,
            "name": name,
            "email": f"student{i:02d}@example.edu",
            "branch": rng.choice(branches),
            "year": "2nd Year",
            "interests": ", ".join(rng.sample(interests_pool, k=rng.randint(2, 4))),
            "preferred_role": roles[(i - 1) % len(roles)],
            "experience": experiences[min(4, max(0, round(rng.gauss(2, 1.15))))],
        }
        # Give each student a distinct but plausible skills profile.
        for skill in SKILLS:
            profile[skill] = rng.randint(3, 10)
        for skill in SOFT:
            profile[skill] = rng.randint(4, 10)
        add_student(profile)
        inserted += 1
    return inserted
