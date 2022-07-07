This simple project is just to get quickly started on Windows.
Its just to bootstrap other python projects.  
Serves also as checklist for all tools.

Setting up stuff

------------------------

1. Initialize empty git repo  
    git init

2. Setup new python env:  
    python -m venv my_env  
    cd my_env/Scripts  
    activate  

3. install python requirements.txt (pip install -r requirements.txt)

4. Install make (installed via: choco install make)

------------------------

Testing the project:   

5. run make test  
    runs linter  
    runs pytest with coverage

6. run make format  
    runs auto-formatting

7. configure pre-commit yaml for hooks

