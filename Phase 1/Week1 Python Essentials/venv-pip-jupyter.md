venv-pip-jupyter

Concise notes for learning venv, pip, and Jupyter.
Save as a reference; commands below are shell commands (not Python).

---

## venv (Python virtual env)

Purpose:

- Isolate project dependencies per-project
- Avoid global package conflicts

Create a virtual environment:
Unix / macOS:
python3 -m venv .venv
Windows (PowerShell):
python -m venv .venv
Windows (cmd.exe):
python -m venv .venv

Activate:
Unix / macOS:
source .venv/bin/activate
Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
Windows (cmd.exe):
.\.venv\Scripts\activate.bat

Deactivate:
deactivate

Tips:

- Use a consistent name (e.g., .venv) and add it to .gitignore
- Create virtualenv per project, not per task
- To use a different Python interpreter:
  python3.9 -m venv .venv

---

## pip (Python package manager)

Ensure pip is up-to-date:
python -m pip install --upgrade pip

Install packages:
pip install package_name
Install specific version:
pip install package_name==1.2.3
Install from requirements file:
pip install -r requirements.txt

Freeze current environment:
pip freeze > requirements.txt

Show installed packages:
pip list
Show details for a package:
pip show package_name

Uninstall a package:
pip uninstall package_name

Useful flags:
--user (install to user site when not using venv)
--upgrade (upgrade package)
--no-cache-dir (avoid cache)

Troubleshooting:

- If pip refers to wrong Python, use: python -m pip install ...
- For permission errors on system installs, prefer venv or use --user

---

## Jupyter (Notebooks & JupyterLab)

Install Jupyter (inside venv):
pip install jupyterlab # modern interface
pip install notebook # classic notebook

Start server:
jupyter lab
jupyter notebook

Open a specific port / no-browser:
jupyter lab --no-browser --port=8888

Create a kernel for a venv so Jupyter can use it:
python -m pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"

Converting notebooks:
jupyter nbconvert --to script notebook.ipynb
jupyter nbconvert --to html notebook.ipynb

Keyboard:

- In notebook: Esc then H shows help
- Shift+Enter runs current cell

Best practices:

- Keep notebooks for exploration; modularize code into .py files for reuse
- Use a kernel per project (ipykernel) tied to your venv
- Pin dependencies in requirements.txt for reproducibility
- Commit small notebooks diffs or clear outputs before committing

---

## Example workflow (quick)

1. Create venv:
   python -m venv .venv
2. Activate:
   source .venv/bin/activate # or Windows activate
3. Upgrade pip:
   python -m pip install --upgrade pip
4. Install essentials:
   pip install jupyterlab numpy pandas matplotlib
5. Add kernel for Jupyter:
   python -m ipykernel install --user --name=proj --display-name="Python (proj)"
6. Start Jupyter:
   jupyter lab

---

## Quick troubleshooting tips

- "module not found" in notebook: ensure kernel uses the same venv where package is installed.
- Permission errors: use venv or add --user.
- Virtual env activation fails on PowerShell: run 'Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser' (as admin if necessary).
- If pip installation fails with wheels: install build tools (on Windows, Visual Studio Build Tools) or use prebuilt wheels.

---

## Resources

- venv docs: https://docs.python.org/3/library/venv.html
- pip docs: https://pip.pypa.io/
- Jupyter: https://jupyter.org/

End of notes.
