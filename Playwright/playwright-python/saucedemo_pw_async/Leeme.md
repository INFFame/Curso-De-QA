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

# Instalar pytest report html
python -m pip install pytest-html

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


# OPTIMIZAR TESTS
- Hacerlos async completamente para utilizar autoesperas = Menor bloqueo, mejor concurrencia, menos overhead
- Instalar xdist para utilizar mas Procesos del SO usando asi mas nucleos del CPU, esto equivale a mayor rendimiento, divide los tests entre los workers y cada worker ejecuta su lote en paralelo 
se instala con el comando: 
    - pip install pytest-xdist
- pytest.ini optimizado para xdist y asyncio
    [pytest]
    addopts = -n auto --dist=loadscope -q
    asyncio_mode = auto

- Evitar xpath, utilizar css o id es un 30% mas rapido

- Dividir tests grandes en tests pequeños: mejor paralelismo, menos fallos encadenados
- Evitar uso de sleeps o esperas manuales

- Utilizar un Browser unico por sesión utilizando pytest.fixture(scope="session")
Un browser es el proceso real del navegador, por lo cual lanzar un browser por test es demasiado caro en tiempo + memoria.

- Utilizar Context por test
Un context es un perfil de navegador aislado que contiene Cookies, Storage, Sesión independientes
Es ideal para aislar tests, ejecutar en paralelo y simular usuarios distintos.

- Screenshots, trazas y video solo en errores (va dentro del fixture de context)
context.tracing.start(
    screenshots=True,
    snapshots=True
)

- Utilizar Page por test
una Page es una pestaña dentro del contexto, no arriesga mucho rendimiento pero lo mas optimo es usarla siempre que sea necesario solamente

- 1 fixture para browser: Se crea una sola vez por worker de xdist, 1 para context: Uno nuevo por test y 1 para page: Una página por test.

# REUTILIZAR CODIGO Y MANTENIBILIDAD
- Seguir los estándares de codificación: 
    - Escribe funciones que hagan una sola cosa y que puedas usar en más de un lugar sin repetir lógica duplicada.
- Funciones y módulos de uso: 
    - Mantén un estilo uniforme en nombres, estructura y formato para que otros (y tú mismo más adelante) puedan entender y reutilizar el código con facilidad.
- Aplicar los principios de diseño: 
    - No solo lo que hace, sino cómo y para qué se usa cada parte. Esto ayuda a otros (y a ti en el futuro) a ver inmediatamente dónde y cómo reutilizarlo.
- Redactar documentación y comentarios: 
    - Diseña tu código de forma que los módulos dependan de interfaces bien definidas y no de detalles internos, para poder reemplazar o extender partes fácilmente.
- Refactorizar y probar el código: 
    - Si ves patrones repetidos, abstrae esa lógica en librerías o módulos que puedan importarse desde diferentes partes de tu aplicación.
- Esto es lo que hay que tener en cuenta: 
    - Demasiada generalización anticipada puede complicar el código en lugar de ayudar. Reutiliza cuando tengas patrones claros, no por prematura abstracción.

- Define una estrategia clara de automatización
    - Automatiza con un objetivo claro (qué, por qué y para qué). Sin estrategia, la automatización se vuelve costosa e inútil.

- Diseña tests modulares y reutilizables
    - Código limpio, desacoplado y reutilizable (ej. Page Object Model). Esto reduce mantenimiento y errores.

- Ejecuta pruebas en paralelo
    - El paralelismo es clave para reducir tiempos de ejecución y escalar en CI/CD.

- Mantén pruebas estables y fáciles de mantener
    - Evita tests frágiles. Usa selectores estables y elimina pruebas obsoletas.



Las recomendaciones provienen de:

- Documentación oficial de Playwright:
    - Api y arquitectura de PW: https://playwright.dev/python/docs/api/class-browsercontext
    - Pytest: https://playwright.dev/python/docs/test-runners
    - Ejecutar tests con pytest: https://playwright.dev/python/docs/running-tests
- Documentación de pytest / xdist:
    - https://python.plainenglish.io/test-parallelization-using-python-and-pytest-2656a4555153
- Estandares de codificación:
    - https://www.linkedin.com/advice/0/you-want-write-reusable-code-whats-best-way-yf6mf?lang=es&originalSubdomain=es
- Mejores practicas de automatización: 
    - https://www.browserstack.com/guide/10-test-automation-best-practices 