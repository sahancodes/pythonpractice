#### Python Coding Practice 🐍

This repository contains Python practice exercises organized by topic.  
The goal is to improve skills step by step through algorithms, OOP, async programming, refactoring, and more.

---

## 📂 Project Structure

CODING_PRACTICE/
├── algorithm_challenges/ — coding challenge solutions
├── asyncio_sysprogram/ — async & system programming practice
├── datastructs_algorithms/ — data structures & algorithms
├── funcs_itertools/ — functions & itertools exercises
├── internals_bestpractices/ — Python internals & best practices
├── miniprojs/ — mini projects
├── oop/ — object-oriented programming exercises
├── python_fundamentals/ — basics & foundations
├── refactoring/ — refactoring exercises
├── test_performance/ — performance testing & benchmarking
├── .venv/ — virtual environment
├── .gitignore
├── pyproject.toml — Black & Ruff configuration
├── requirements.txt — dependencies
└── README.md — this file

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

## ▶️ How to Run

Each folder contains focused exercises or projects. For example:  

Run a script:  
python python_fundamentals/example.py  

Run tests:  
pytest algorithm_challenges

---

## 🛠️ Tools Used

- Python 3.x  
- pytest — for testing  
- Black — code formatter  
- Ruff — fast linter  

---

## 📌 Goals

- Practice Python across different areas (fundamentals → advanced).  
- Build reusable code and mini projects.  
- Learn clean coding practices with tests, linting, and formatting.  
- Explore performance testing, async, and Python internals.  

---

## 🚀 Next Steps

- Add more exercises regularly.  
- Expand `miniprojs/` into larger applications.  
- Continue experimenting with new Python features.  

---

👨‍💻 Author: [@sahancodes](https://github.com/sahancodes)
"""

# Save as README.md
output_path = "/mnt/data/README.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(readme_md)

output_path
