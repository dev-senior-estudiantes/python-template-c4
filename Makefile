.PHONY: help test lint style clean

.DEFAULT_GOAL := help

help:
	@echo "Comandos disponibles:"
	@echo "  make test   - Ejecuta los tests con pytest"
	@echo "  make lint   - Analiza el código con pylint"
	@echo "  make style  - Revisa el estilo con flake8"
	@echo "  make clean  - Elimina archivos temporales y caché"

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

# Ejecuta todos los tests

test:
	 python -m pytest -v

# Analiza el código con pylint
lint:
	pylint modulo_1_fundamentos/clase_1_entorno_prof/ejemplo_saludo_ai.py

# Revisa el estilo con flake8
style:
	python -m flake8 . --exclude=.venv
