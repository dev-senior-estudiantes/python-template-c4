.PHONY: help test lint style pep8 docstyle quality clean

.DEFAULT_GOAL := help

help:
	@echo "Comandos disponibles:"
	@echo "  make test        - Ejecuta los tests con pytest"
	@echo "  make lint        - Analiza el código con pylint"
	@echo "  make style       - Revisa el estilo con flake8"
	@echo "  make pep8        - Verifica estilo PEP 8 con pycodestyle"
	@echo "  make docstyle    - Verifica docstrings con pydocstyle"
	@echo "  make quality     - Ejecuta todas las verificaciones de calidad"
	@echo "  make clean       - Elimina archivos temporales y caché"

clean:
	@echo "🧹 Limpiando archivos temporales..."
	@if exist __pycache__ rmdir /s /q __pycache__ 2>nul || echo "No hay __pycache__ en raíz"
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d" 2>nul
	@del /s /q *.pyc 2>nul || echo "No hay archivos .pyc"
	@del /s /q *.pyo 2>nul || echo "No hay archivos .pyo"
	@del /s /q *~ 2>nul || echo "No hay archivos temporales ~"
	@echo "✅ Limpieza completada"

# Ejecuta todos los tests

test:
	 python -m pytest -v

# Analiza el código con pylint
lint:
	pylint modulo_1_fundamentos/clase_1_entorno_prof/ejemplo_saludo_ai.py

# Revisa el estilo con flake8
style:
	python -m flake8 . --exclude=.venv

# Verifica estilo PEP 8 con pycodestyle
pep8:
	python -m pycodestyle . --exclude=.venv

# Verifica docstrings con pydocstyle
docstyle:
	python -m pydocstyle . --match='(?!test_).*\.py'

# Ejecuta todas las verificaciones de calidad
quality: lint style pep8 docstyle
	@echo "✅ Todas las verificaciones de calidad completadas"
