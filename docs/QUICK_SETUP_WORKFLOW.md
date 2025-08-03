# 🚀 Quick Setup - Workflow de Calidad Python

> **Guía rápida para implementar workflow de calidad en cualquier proyecto Python**

## ⚡ Setup en 5 minutos

### 1️⃣ **Archivos básicos necesarios:**

**requirements.txt:**

```txt
pytest==8.4.1
flake8
pylint
pycodestyle
pydocstyle
colorama==0.4.6
```

**Makefile:**

```makefile
.PHONY: help test lint style pep8 docstyle quality clean

help:
	@echo "make test     - Tests con pytest"
	@echo "make lint     - Análisis con pylint"
	@echo "make style    - Estilo con flake8"
	@echo "make pep8     - PEP 8 con pycodestyle"
	@echo "make docstyle - Docstrings con pydocstyle"
	@echo "make quality  - TODAS las verificaciones"
	@echo "make clean    - Limpiar archivos temp"

test:
	python -m pytest -v

lint:
	pylint src/

style:
	python -m flake8 . --exclude=.venv

pep8:
	python -m pycodestyle . --exclude=.venv

docstyle:
	python -m pydocstyle . --match='(?!test_).*\.py'

quality: lint style pep8 docstyle
	@echo "✅ Calidad verificada"

clean:
	@echo "🧹 Limpiando archivos temporales..."
	@if exist __pycache__ rmdir /s /q __pycache__ 2>nul || echo "No hay __pycache__ en raíz"
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d" 2>nul
	@del /s /q *.pyc 2>nul || echo "No hay archivos .pyc"
	@del /s /q *.pyo 2>nul || echo "No hay archivos .pyo"
	@del /s /q *~ 2>nul || echo "No hay archivos temporales ~"
	@echo "✅ Limpieza completada"
```

**setup.cfg:**

```ini
[pycodestyle]
max-line-length = 88
exclude = .venv,__pycache__,.git
ignore = E203,W503

[flake8]
max-line-length = 88
exclude = .venv,__pycache__,.git
ignore = E203,W503
```

**.pydocstyle:**

```ini
[pydocstyle]
match = (?!test_)(?!setup).*\.py
ignore = D213,D203,D212
```

### 2️⃣ **Comandos de instalación:**

```bash
# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
make help

# Ejecutar verificación completa
make quality
```

### 3️⃣ **Estructura de proyecto recomendada:**

```
mi-proyecto/
├── Makefile
├── requirements.txt
├── setup.cfg
├── .pydocstyle
├── src/
│   └── mi_modulo.py
└── tests/
    └── test_mi_modulo.py
```

## 🔧 **Uso diario:**

```bash
# Durante desarrollo
make style

# Antes de commit
make quality

# Solo tests
make test

# Limpiar
make clean
```

## 🌐 **GitHub Actions (.github/workflows/python.yml):**

```yaml
name: Python Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
        with:
          python-version: "3.12"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run quality checks
        run: make quality
      - name: Run tests
        run: make test
```

## 🎯 **Personalización rápida:**

### Para Django:

```makefile
lint:
	pylint --load-plugins pylint_django myapp/
```

### Para FastAPI:

```makefile
lint:
	pylint --disable=too-few-public-methods src/
```

### Solo para archivos modificados:

```makefile
lint-diff:
	git diff --name-only | grep "\.py$" | xargs pylint
```

## 🔍 **Resolución rápida de problemas:**

```bash
# Make no encontrado (Windows)
choco install make

# Módulos no encontrados
pip install --upgrade -r requirements.txt

# Error con comando clean en Windows
# Si ves: FIND: formato de parámetros incorrecto
# El Makefile ya está corregido para Windows

# Verificar configuración
python -m pylint --version
python -m flake8 --version
```

### 💡 **Nota sobre compatibilidad:**

Este Makefile está optimizado para **Windows** usando comandos nativos (`rmdir`, `del`).
Para Unix/Linux, reemplaza la sección `clean` con comandos `find` tradicionales.

---

**¡Listo! En 5 minutos tienes calidad profesional en tu proyecto Python 🐍✨**

_Para documentación completa: ver `docs/WORKFLOW_CALIDAD_CODIGO.md`_
