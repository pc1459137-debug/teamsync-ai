# AI-Based Smart Team Formation System

## Part 1 — Student Profile & Registration

This is the first module of the project. It allows students to create and edit profiles containing technical skills, soft skills, interests, experience, and preferred roles.

## Features

- Student profile creation
- Technical skill ratings from 1–10
- Soft skill ratings from 1–10
- Project interest selection
- Preferred role selection
- Previous project experience
- SQLite database
- View registered profiles
- Edit profiles

## Requirements

- Python 3.10 or newer
- VS Code recommended

## Installation

Open the project folder in VS Code terminal:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run:

```bash
python -m streamlit run app.py
```

The browser should open the Streamlit application.

## Next Development Phase

The next version will add:

1. Student compatibility calculation
2. Cosine similarity
3. Recommended teammates
4. Complementary skill detection
5. Automatic team formation
6. Team role assignment
7. Team balance score
8. Admin dashboard
