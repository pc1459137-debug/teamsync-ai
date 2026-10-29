import streamlit as st
import pandas as pd
from database import init_db, add_student, update_student, get_students, get_student, SKILLS, SOFT
from algorithm import generate_teams, build_report, recommend, metrics

st.set_page_config(page_title="TeamSync AI", page_icon="🧩", layout="wide", initial_sidebar_state="expanded")
init_db()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--ink:#172033;--muted:#697386;--brand:#6558f5;--mint:#c9f7df;}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;}
.stApp{background:#f6f7fb;color:var(--ink);}
.block-container{max-width:1240px;padding-top:2rem;padding-bottom:3rem;}
h1,h2,h3{font-family:'Space Grotesk',sans-serif!important;color:#172033;}
[data-testid="stSidebar"]{background:#171b2e;}
[data-testid="stSidebar"] *{color:#f5f6ff!important;}
[data-testid="stSidebar"] [data-testid="stRadio"] label{background:#222741;border-radius:10px;padding:8px 12px;margin:4px 0;}
div.stButton>button,div.stFormSubmitButton>button{border-radius:10px;border:0;background:#6558f5;color:white;font-weight:700;padding:.65rem 1.1rem;}
div.stButton>button:hover,div.stFormSubmitButton>button:hover{background:#5144dc;color:white;}
[data-testid="stMetric"]{background:white;padding:18px;border:1px solid #e8eaf2;border-radius:16px;box-shadow:0 4px 14px #17203308;}
[data-testid="stDataFrame"]{border:1px solid #e8eaf2;border-radius:12px;overflow:hidden;}
.hero{background:linear-gradient(115deg,#191d34,#35306d 68%,#6558f5);border-radius:24px;padding:32px;color:white;margin-bottom:22px;}
.hero h1{color:white!important;font-size:2.35rem;margin:0 0 8px;}
.hero p{color:#e3e5ff;font-size:1rem;margin-bottom:0;}
.pill{display:inline-block;background:#c9f7df;color:#176342;border-radius:99px;padding:5px 11px;font-size:.8rem;font-weight:700;margin-bottom:12px;}
.section-card{background:white;border:1px solid #e8eaf2;border-radius:18px;padding:20px;margin:8px 0;}
.small-muted{color:#697386;font-size:.9rem;}
</style>
""", unsafe_allow_html=True)

if "teams" not in st.session_state:
    st.session_state.teams = None

menu = st.sidebar.radio("TEAMSYNC AI", [
    "🏠  Overview", "📝  Create profile", "👥  Students",
    "✏️  Edit profile", "🧠  Build teams", "✨  Match suggestions"
])
st.sidebar.markdown("---")
st.sidebar.caption("SMART TEAM FORMATION")
st.sidebar.caption("Skills • Experience • Balance")

students = get_students()

def profile_form(existing=None):
    e = existing or {}
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        sid = st.text_input("Student ID / PRN *", str(e.get("student_id", "")), disabled=bool(existing), placeholder="e.g. 202501110047")
        name = st.text_input("Full name *", str(e.get("name", "")), placeholder="Your name")
        email = st.text_input("College email", str(e.get("email", "")), placeholder="name@college.edu")
        branches = ["AI & ML", "CSE", "AI & DS", "IT", "ECE", "Other"]
        branch_now = e.get("branch", "AI & ML")
        branch = st.selectbox("Department", branches, index=branches.index(branch_now) if branch_now in branches else 0)
        years = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        year_now = e.get("year", "1st Year")
        year = st.selectbox("Academic year", years, index=years.index(year_now) if year_now in years else 0)
    with right:
        roles = ["ML Developer", "Web Developer", "Data Analyst", "UI/UX Designer", "Database Developer", "Team Leader", "Researcher", "Team Member"]
        role_now = e.get("preferred_role", "ML Developer")
        role = st.selectbox("Preferred project role", roles, index=roles.index(role_now) if role_now in roles else 0)
        choices = ["Artificial Intelligence", "Machine Learning", "Data Science", "Web Development", "App Development", "Cyber Security", "Cloud", "IoT"]
        old = [x.strip() for x in str(e.get("interests", "")).split(",") if x.strip()]
        interests = st.multiselect("Topics you want to work on", choices, default=[x for x in old if x in choices])
        exp_options = ["None", "Beginner", "Medium", "High", "Expert"]
        exp_now = e.get("experience", "None")
        experience = st.selectbox("Project experience", exp_options, index=exp_options.index(exp_now) if exp_now in exp_options else 0)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("### Technical skills")
    st.caption("Rate yourself honestly from 1 (learning) to 10 (confident).")
    labels = {"python": "Python", "cpp": "C++", "java": "Java", "machine_learning": "Machine learning",
              "web_development": "Web development", "sql": "SQL / databases", "uiux": "UI / UX design",
              "data_science": "Data science", "cloud": "Cloud computing"}
    tech = {}
    cols = st.columns(3)
    for i, k in enumerate(SKILLS):
        with cols[i % 3]:
            tech[k] = st.slider(labels[k], 1, 10, int(e.get(k, 5)), key=f"tech_{k}_{'edit' if existing else 'new'}")
    st.markdown("### Teamwork strengths")
    soft_labels = {"communication": "Communication", "leadership": "Leadership", "teamwork": "Teamwork", "problem_solving": "Problem solving"}
    soft = {}
    cols = st.columns(4)
    for i, k in enumerate(SOFT):
        with cols[i]:
            soft[k] = st.slider(soft_labels[k], 1, 10, int(e.get(k, 5)), key=f"soft_{k}_{'edit' if existing else 'new'}")
    return {"student_id": sid.strip(), "name": name.strip(), "email": email.strip(), "branch": branch, "year": year,
            **tech, **soft, "interests": ", ".join(interests), "preferred_role": role, "experience": experience}

if menu.startswith("🏠"):
    st.markdown("""
    <div class="hero">
      <span class="pill">AI-POWERED COLLABORATION</span>
      <h1>Build better teams.<br>Build better ideas.</h1>
      <p>TeamSync AI helps students find complementary teammates and creates balanced project teams from skills, experience and interests.</p>
    </div>
    """, unsafe_allow_html=True)
    a, b, c, d = st.columns(4)
    a.metric("Student profiles", len(students))
    b.metric("Team sizes", "4 / 5 / 6")
    b2 = len(st.session_state.teams or [])
    c.metric("Teams generated", b2)
    d.metric("Matching engine", "Ready")
    st.markdown("### Your project workspace")
    cards = st.columns(3)
    with cards[0]:
        st.markdown('<div class="section-card"><h3>01 · Create your profile</h3><p>Share your skills, interests, experience and preferred role.</p></div>', unsafe_allow_html=True)
    with cards[1]:
        st.markdown('<div class="section-card"><h3>02 · Discover matches</h3><p>Find students with compatible and complementary strengths.</p></div>', unsafe_allow_html=True)
    with cards[2]:
        st.markdown('<div class="section-card"><h3>03 · Form balanced teams</h3><p>Spread experienced and developing students across teams.</p></div>', unsafe_allow_html=True)
    st.markdown("### How it works")
    st.write("**Profile → Skill analysis → Compatibility → Balanced teams → Team report**")
    if len(students) == 0:
        st.info("Start by creating a profile. Profiles are saved in the local SQLite database.")

elif menu.startswith("📝"):
    st.markdown("## Create your student profile")
    st.write("A profile helps the matching engine understand what you can contribute and what you want to learn.")
    with st.form("new_profile"):
        data = profile_form()
        submit = st.form_submit_button("Save my profile", type="primary")
    if submit:
        if not data["student_id"] or not data["name"]:
            st.error("Student ID and full name are required.")
        else:
            try:
                add_student(data)
                st.success("Profile saved! You can now view students or generate teams.")
            except Exception as ex:
                st.error("Could not save profile. Check that the Student ID is unique. Details: " + str(ex))

elif menu.startswith("👥"):
    st.markdown("## Student directory")
    st.caption("Only share real student details with permission. This local demo has no login system.")
    if not students:
        st.info("No profiles yet. Create the first student profile.")
    else:
        search = st.text_input("Search by name, student ID, role or interest")
        filtered = [s for s in students if search.lower() in " ".join(str(s.get(k, "")) for k in ["name", "student_id", "preferred_role", "interests"]).lower()]
        st.write(f"Showing **{len(filtered)}** of **{len(students)}** students")
        st.dataframe(pd.DataFrame(filtered)[["student_id", "name", "branch", "year", "preferred_role", "experience", "interests"]], use_container_width=True, hide_index=True)

elif menu.startswith("✏️"):
    st.markdown("## Update your profile")
    if not students:
        st.info("No profiles available.")
    else:
        sid = st.selectbox("Choose student ID", [s["student_id"] for s in students])
        existing = get_student(sid)
        with st.form("edit_profile"):
            data = profile_form(existing)
            submit = st.form_submit_button("Update profile", type="primary")
        if submit:
            try:
                update_student(sid, data)
                st.success("Profile updated.")
            except Exception as ex:
                st.error("Update failed: " + str(ex))

elif menu.startswith("🧠"):
    st.markdown("## AI team builder")
    st.write("Choose a target team size. If the student count is not divisible by that size, the last teams may have fewer members.")
    if len(students) < 2:
        st.warning("Add at least 2 student profiles first.")
    else:
        x, y, z = st.columns(3)
        with x:
            team_size = st.selectbox("Members per team", [4, 5, 6], index=1)
        with y:
            iterations = st.slider("Balance optimization", 50, 1000, 300, 50)
        with z:
            seed = st.number_input("Random seed", 1, 99999, 42)
        st.caption(f"{len(students)} students currently available.")
        if st.button("Generate balanced teams", type="primary"):
            teams, error = generate_teams(students, team_size, int(iterations), int(seed))
            if error:
                st.error(error)
            else:
                st.session_state.teams = teams
                st.success(f"Generated {len(teams)} teams.")
        teams = st.session_state.teams
        if teams:
            team_metrics = []
            for i, t in enumerate(teams, 1):
                team_metrics.append({"Team": f"Team {i}", "Members": len(t), **metrics(t)})
            md = pd.DataFrame(team_metrics)
            a, b, c = st.columns(3)
            a.metric("Teams created", len(teams))
            b.metric("Average score", f"{md['Team Score'].mean():.1f}/100")
            c.metric("Team size range", f"{md['Members'].min()}–{md['Members'].max()}")
            st.dataframe(md, use_container_width=True, hide_index=True)
            st.markdown("### Team rosters")
            roster = build_report(teams)
            for tname in roster["Team"].unique():
                with st.expander(f"{tname} · {len(roster[roster.Team == tname])} members", expanded=True):
                    st.dataframe(roster[roster.Team == tname][["Student ID", "Name", "Assigned Role", "Experience", "Strength"]], use_container_width=True, hide_index=True)
            st.download_button("Download team report (CSV)", roster.to_csv(index=False).encode("utf-8"), "team_report.csv", "text/csv")

elif menu.startswith("✨"):
    st.markdown("## Teammate match suggestions")
    if len(students) < 2:
        st.info("At least two student profiles are needed.")
    else:
        sid = st.selectbox("Find matches for student", [s["student_id"] for s in students])
        limit = st.slider("Number of suggestions", 1, min(10, len(students) - 1), min(5, len(students) - 1))
        if st.button("Find compatible teammates", type="primary"):
            result = recommend(students, sid, limit)
            st.dataframe(result, use_container_width=True, hide_index=True)
            st.caption("Compatibility is an approximate score based on profile vectors and skill complementarity, not a guarantee of team success.")
