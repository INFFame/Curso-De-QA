@echo off

REM Crear venv
python -m venv venv

REM Activar venv
call venv\Scripts\activate

REM Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
python.exe -m pip install --upgrade pip

echo Entorno listo.