# Homework 6: Getting Ready for Production

## Introduction

This project enhances an **interactive calculator** to be **production-ready** by integrating:

- **Continuous Integration (CI)** with GitHub Actions.
- **Environment Variables** to manage configuration securely.
- **Logging** for tracking application execution and debugging.

These improvements align with **DevOps principles** to automate testing, improve security, and enhance maintainability.

---

## Features Added in Homework 6

1. **GitHub Actions:** Automates running tests on each push or pull request to `main`.  
2. **Environment Variables:** Manages application configuration securely in a `.env` file.  
3. **Logging:** Implements structured logging to monitor operations, errors, and debugging information.

---

**Note**: `.env` is **ignored** by Git, so it won’t appear on GitHub.

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Satyabandi20/homework6
   cd homework6
   ```
2. **Create & activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Environment Variables

- Created  **`.env`**  
- format:
  ```bash
  ENV_NAME="development"
  LOG_LEVEL="INFO"
  ```
- The app code in `app/__init__.py` loads `.env` via `python-dotenv` and sets:
  ```python
  load_dotenv()
  self.env_name = os.getenv("ENV_NAME", "Production")
  ```
- The test `test_app.py::test_environment_loaded` ensures the environment variable is recognized.  
- On GitHub, the `ENV_NAME` is set in `.github/workflows/python-app.yml` under `env:` so that test doesn’t fail.

---

## Logging

- **Default** logs go to the console.  
- If `logging.conf` exists, a rotating file handler writes logs to `logs/app.log`.
- Example logs:
  ```
(venv) @Satyabandi20 ➜ /workspaces/homework6 (main) $ python main.py
2025-03-04 19:29:12,465 - __main__ - INFO - Environment: development
2025-03-04 19:29:12,466 - __main__ - INFO - Plugin commands loaded.
  ```

## GitHub Actions

- `.github/workflows/python-app.yml` defines a **CI pipeline**:
  ```yaml
  name: Python application
  on:
    push:
      branches: [ "main" ]
    pull_request:
      branches: [ "main" ]
  env:
    ENV_NAME: development
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
          uses: actions/setup-python@v3
          with:
            python-version: "3.10"
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        - name: Test with pytest --pylint
          run: |
            pytest
  ```
---