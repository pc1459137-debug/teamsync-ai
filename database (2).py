import sqlite3
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
