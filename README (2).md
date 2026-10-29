# TeamSync AI — Part 2 website-style frontend

This is a Streamlit app styled to look more like a modern website dashboard.

## Run from your current folder
Your current virtual environment is one level above the project folder:
`C:\Users\sumit\OneDrive\Desktop\minor\.venv`

1. Extract this ZIP.
2. Copy the files `app.py`, `database.py`, `algorithm.py`, `requirements.txt` into:
   `C:\Users\sumit\OneDrive\Desktop\minor`
   (Back up your existing files first if you want to preserve Part 1.)
3. In PowerShell, run these commands from `C:\Users\sumit\OneDrive\Desktop\minor`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

This avoids PowerShell's blocked script-activation issue.

## Features
- Website-style overview/dashboard
- Create, view, and edit student profiles
- Technical and soft-skill ratings
- Compatibility recommendations
- Team sizes 4, 5, or 6
- Balanced team formation and team scoring
- Role suggestions and CSV export

## Real multi-student usage
This version is a local prototype. Profiles are saved in SQLite on this computer. It can handle hundreds of records for a college demo, but it does not yet provide secure student logins or a shared cloud database for students on different devices. Those are needed before publishing it for a real college-wide signup.
