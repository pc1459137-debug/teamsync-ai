import math, random
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = ["python","cpp","java","machine_learning","web_development","sql","uiux","data_science","cloud"]
SOFT = ["communication","leadership","teamwork","problem_solving"]
ROLE_SKILLS = {
    "ML Developer":["python","machine_learning","data_science"],
    "Web Developer":["python","web_development","sql"],
    "Data Analyst":["python","sql","data_science"],
    "UI/UX Designer":["uiux"], "Database Developer":["sql","cloud"],
    "Team Leader":["leadership","communication","teamwork"],
    "Researcher":["machine_learning","data_science","problem_solving"]
}
def num(x):
    try: return float(x)
    except (TypeError,ValueError): return 0.0
def experience_score(x):
    return {"none":1,"beginner":2.5,"medium":6,"high":8.5,"expert":10}.get(str(x).strip().lower(),5)
def strength(s):
    return .55*np.mean([num(s.get(c,0)) for c in SKILLS]) + .20*np.mean([num(s.get(c,0)) for c in SOFT]) + .25*experience_score(s.get("experience","None"))
def vector(s):
    return np.array([num(s.get(c,0)) for c in SKILLS+SOFT],dtype=float).reshape(1,-1)
def compatibility(a,b):
    sim=float(cosine_similarity(vector(a),vector(b))[0,0])
    va,vb=vector(a).ravel(),vector(b).ravel()
    aa,bb=set(np.argsort(va)[-3:]),set(np.argsort(vb)[-3:])
    return round(100*(.65*sim+.35*(1-len(aa&bb)/3)),1)
def metrics(team):
    if not team: return {"Average Strength":0,"Strength Variation":0,"Skill Coverage":0,"Compatibility":0,"Team Score":0}
    vals=np.array([strength(s) for s in team])
    coverage=100*np.mean([any(num(s.get(c,0))>=7 for s in team) for c in SKILLS])
    pairs=[compatibility(team[i],team[j]) for i in range(len(team)) for j in range(i+1,len(team))]
    comp=float(np.mean(pairs)) if pairs else 0
    balance=max(0,100-float(vals.std())*12)
    exp=np.mean([experience_score(s.get("experience","")) for s in team])*10
    teamwork=np.mean([num(s.get("teamwork",5)) for s in team])*10
    score=.35*balance+.25*coverage+.20*comp+.10*exp+.10*teamwork
    return {"Average Strength":round(float(vals.mean()),2),"Strength Variation":round(float(vals.std()),2),
            "Skill Coverage":round(float(coverage),1),"Compatibility":round(comp,1),"Team Score":round(float(score),1)}
def generate_teams(students,team_size=5,iterations=300,seed=42):
    if len(students)<2: return [],"Add at least 2 student profiles."
    if team_size not in (4,5,6): return [],"Choose team size 4, 5, or 6."
    people=[dict(s) for s in students]
    people.sort(key=strength,reverse=True)
    count=math.ceil(len(people)/team_size)
    teams=[[] for _ in range(count)]
    for i,s in enumerate(people):
        cycle,pos=i//count,i%count
        target=pos if cycle%2==0 else count-1-pos
        teams[target].append(s)
    rng=random.Random(seed)
    def objective(ts):
        avg=np.array([np.mean([strength(s) for s in t]) if t else 0 for t in ts])
        scores=np.array([metrics(t)["Team Score"] for t in ts])
        return .65*max(0,100-avg.std()*15)+.35*scores.mean()
    best=[list(t) for t in teams]; best_score=objective(best)
    for _ in range(iterations):
        if len(teams)<2: break
        a,b=rng.sample(range(len(teams)),2)
        if not teams[a] or not teams[b]: continue
        i,j=rng.randrange(len(teams[a])),rng.randrange(len(teams[b]))
        teams[a][i],teams[b][j]=teams[b][j],teams[a][i]
        score=objective(teams)
        if score>=best_score:
            best_score=score; best=[list(t) for t in teams]
        else: teams[a][i],teams[b][j]=teams[b][j],teams[a][i]
    return best,None
def assign_role(s):
    role=str(s.get("preferred_role","Team Member"))
    needed=ROLE_SKILLS.get(role,[])
    return role if not needed or np.mean([num(s.get(c,0)) for c in needed])>=4 else "Team Member"
def build_report(teams):
    rows=[]
    for i,team in enumerate(teams,1):
        score=metrics(team)["Team Score"]
        for s in team:
            rows.append({"Team":f"Team {i}","Student ID":s.get("student_id",""),"Name":s.get("name",""),
                         "Assigned Role":assign_role(s),"Experience":s.get("experience",""),
                         "Strength":round(strength(s),2),"Team Score":score})
    return pd.DataFrame(rows)
def recommend(students,sid,limit=5):
    target=next((s for s in students if str(s["student_id"])==str(sid)),None)
    if not target: return pd.DataFrame()
    rows=[]
    for s in students:
        if str(s["student_id"])!=str(sid):
            rows.append({"Student ID":s["student_id"],"Name":s["name"],"Compatibility (%)":compatibility(target,s),
                         "Experience":s.get("experience",""),"Preferred Role":s.get("preferred_role","")})
    return pd.DataFrame(rows).sort_values("Compatibility (%)",ascending=False).head(limit)
