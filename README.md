# Python Workspace Documentation

## Project Overview

This workspace contains a variety of Python projects and modules, including:
- FastAPI web applications
- CRUD applications with SQLAlchemy
- Python basics, OOP, decorators, error handling, and more
- Practice scripts and educational code

---

## Directory Structure

```
python/
│
├── api_handling/
│   ├── API_handling.py
│   └── practice2.py
│
├── basic/
│   ├── chai.py
│   ├── data_types.py
│   ├── dict.py
│   ├── first.py
│   ├── list.py
│   ├── number.py
│   ├── q1.py ... q8.py
│   ├── string.py
│   └── tuple.py
│
├── decoratorss/
│   ├── debugging.py
│   └── timingfunction.py
│
├── error_handling/
│   ├── error_handle.py
│   └── youtube_manager.py
│
├── fastapi/
│   ├── main.py
│   └── blog/
│       ├── __init__.py
│       ├── blog.db
│       ├── database.py
│       ├── main.py
│       ├── models.py
│       ├── requirments.txt
│       └── blog-env/
│
├── functionsinpy/
│   ├── q1.py ... q10.py
│
├── lasttry/
│   ├── crudwithpylint/
│   │   ├── __pycache__/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── repository/
│   │   │   ├── student.py
│   │   │   └── user.py
│   │   ├── routers/
│   │   │   ├── authentication.py
│   │   │   ├── student.py
│   │   │   ├── user.py
│   │   │   └── __init__.py
│   │   ├── schemas.py
│   │   └── student.db
│   └── venv/
│
├── loops/
│   ├── q1.py ... q8.py
│
├── oops/
│   ├── carclass.py
│   ├── classwithmethod.py
│   ├── encapsulation.py
│   ├── inheritance.py
│   ├── last.py
│   ├── polymorphism.py
│   ├── staticmethod.py
│   └── tempCodeRunnerFile.py
│
├── pylintcrud/
│   └── student.db
│
├── scopes_closure/
│   └── scopes.py
│
├── virtual_env/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   ├── .lock
│   └── pyvenv.cfg
│
├── app.py
├── myfile.txt
├── requirment.txt
├── sqlite3.md
├── sqlite3.py
└── youtube.txt
```

---

## Folder & File Descriptions

### Top-Level Files
- **app.py**: Likely a main entry point or test script.
- **myfile.txt, youtube.txt**: Text files, possibly for notes or data.
- **requirment.txt**: (typo, should be `requirements.txt`) - lists Python dependencies.
- **sqlite3.md, sqlite3.py**: Markdown and Python files for SQLite3 usage.

### Major Folders

#### `api_handling/`
- Contains scripts for practicing API requests and handling.

#### `basic/`
- Contains scripts for basic Python concepts: data types, lists, dicts, strings, tuples, and simple exercises.

#### `decoratorss/`
- Contains scripts demonstrating Python decorators, debugging, and timing functions.

#### `error_handling/`
- Contains scripts for error handling and a YouTube manager example.

#### `fastapi/`
- Contains FastAPI projects.
  - **main.py**: A FastAPI app.
  - **blog/**: A subproject with its own database, models, and virtual environment.

#### `functionsinpy/`
- Contains scripts for practicing Python functions.

#### `lasttry/`
- Contains a more advanced CRUD project (`crudwithpylint`) with:
  - **models.py, database.py, schemas.py**: SQLAlchemy models, DB config, and Pydantic schemas.
  - **repository/**: Business logic for students and users.
  - **routers/**: FastAPI routers for authentication, students, and users.
  - **main.py**: FastAPI app entry point.
  - **venv/**: Virtual environment for this project.

#### `loops/`
- Contains scripts for practicing Python loops.

#### `oops/`
- Contains scripts for Object-Oriented Programming concepts: classes, inheritance, encapsulation, polymorphism, static methods, etc.

#### `pylintcrud/`
- Contains a SQLite database file, possibly for a CRUD project.

#### `scopes_closure/`
- Contains a script for Python scopes and closures.

#### `virtual_env/`
- A virtual environment for the workspace.

---

## How to Run

### For FastAPI Projects

1. **Activate the virtual environment** (if present):
   - Windows (cmd): `venv\Scripts\activate`
   - PowerShell: `venv\Scripts\Activate.ps1`
2. **Install dependencies**:
   ```
   pip install -r requirments.txt
   ```
3. **Run the FastAPI server**:
   ```
   uvicorn main:app --reload
   ```
4. **Access the API docs**:  
   Visit `http://127.0.0.1:8000/docs` in your browser.

### For Scripts

- Run any script with:
  ```
  python scriptname.py
  ```

---

## Virtual Environments

- **fastapi/blog/blog-env/**: Virtual environment for the FastAPI blog project.
- **lasttry/venv/**: Virtual environment for the CRUD project in `lasttry/crudwithpylint`.
- **virtual_env/**: General virtual environment for the workspace.

Activate the appropriate environment before running code in that project.

---

## Requirements

- Check `requirment.txt` or `requirments.txt` in each project for dependencies.
- Common dependencies include: `fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`.
