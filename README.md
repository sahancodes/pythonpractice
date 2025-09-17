readme_md = """# Python Practice 🐍

This repository contains small Python exercises and practice projects.  
The goal is to build up Python skills step by step through coding challenges, notes, and tests.

---

## 📂 Project Structure

pythonpractice/
├── exercises/          # Individual exercises
│   ├── 01_basics/
│   │   ├── main.py
│   │   ├── test_main.py
│   │   └── notes.md
│   ├── 02_loops/
│   └── ...
├── utils/              # Reusable helper functions
├── data/               # Input/output data files
├── .gitignore
├── pyproject.toml       # Config for Black & Ruff
├── requirements.txt     # Python dependencies
└── README.md

---

## ⚙️ Setup Instructions

1. Clone the repo  
   git clone https://github.com/sahancodes/pythonpractice.git  
   cd pythonpractice

2. Create a virtual environment  
   python -m venv .venv

3. Activate it  
   - Windows (PowerShell): .\\.venv\\Scripts\\Activate.ps1  
   - macOS/Linux: source .venv/bin/activate

4. Install dependencies  
   pip install -r requirements.txt

---

## ▶️ How to Run an Exercise

Each exercise has its own folder (for example `exercises/01_basics`).  

Run directly:  
python exercises/01_basics/main.py  

Run tests:  
pytest exercises/01_basics

---

## 🛠️ Tools Used

- Python 3.x  
- pytest — for testing  
- Black — code formatter  
- Ruff — fast linter  

---

## 📌 Goals

- Practice Python through small, focused exercises.  
- Learn clean coding practices with tests, linting, and formatting.  
- Keep all work organized and version-controlled with Git & GitHub.  

---

## 🚀 Next Steps

- Add more exercises regularly.  
- Expand `utils/` with reusable functions.  
- Explore Jupyter notebooks for data science practice.  

---

👨‍💻 Author: [@sahancodes](https://github.com/sahancodes)
"""

# Save as README.md
output_path = "/mnt/data/README.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(readme_md)

output_path
