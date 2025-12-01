@echo off

REM Crear venv
python -m venv venv

REM Activar venv
call venv\Scripts\activate

REM Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
python.exe -m pip install --upgrade pip

REM Crear carpeta de tests
if not exist "tests" (
    mkdir tests
)

REM Crear pytest.ini si no existe
if not exist "pytest.ini" (
    echo [pytest]>pytest.ini
    echo addopts = --disable-warnings -s>>pytest.ini
    echo testpaths = tests>>pytest.ini
    echo python_files = test_*.py>>pytest.ini
)

REM Crear gitignore si no existe
if not exist ".gitignore" (
    echo venv/>.gitignore
    echo __pycache__/>>.gitignore
    echo *.pyc>>.gitignore
    echo .pytest_cache/>>.gitignore
    echo .vscode/>>.gitignore
)

echo Entorno listo.