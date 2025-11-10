# crear env
python -m venv .venv

# Activar en cmd
# Si te da error por políticas de ejecución, ejecuta la siguiente línea primero (afecta solo esta sesión)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
# Luego activa
.\.venv\Scripts\Activate

# Instalar Playwright
python -m pip install --upgrade pip
python -m pip install playwright

# Instalar navegadores de playwright
python -m playwright install

# Instalar pytest
python -m pip install pytest-playwright

# Ejecutar prueba con pytest
pytest --headed

# Ejecutar prueba indicando la url base 
pytest --headed --base-url https://www.saucedemo.com/

# Ejecutar prueba indicando el browser deseado
pytest --headed --base-url https://www.saucedemo.com/ --browser chromium --browser webkit --browser firefox

# Ejecutar prueba abriendo chrome directamente
pytest --headed --base-url https://www.saucedemo.com/ --browser-channel chrome

# Ejecutar prueba y hacer seguimiento a la prueba, estas se pueden ver en la url https://trace.playwright.dev/
pytest --headed --base-url https://www.saucedemo.com/ --tracing on

# Correr todo esto con pytest.ini y sus parametros
pytest

# Generar test automaticamente con recording, se le debe indicar una url
playwright codegen "www.example.com"

# Correr test seleccionado
pytest codegendemo.py

# Correr test con otro tipo de dispositivo
playwright codegen --device="iPhone 12" saucedemo.com

# Cambiar el viewport de la pantalla
playwright codegen --viewport-size=500,500 saucedemo.com

# Cambiar el color de scheme
playwright codegen --color-scheme=dark https://playwright.dev/docs/intro

# Cambiar idioma
playwright codegen --lang="it-IT" google.com

# Mostrar la traza
playwright show-trace carpeta/archivo.zip