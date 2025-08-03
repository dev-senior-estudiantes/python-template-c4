# Guía de Uso: Pytest, Flake8 y Pylint

Esta guía explica cómo instalar, ejecutar e interpretar los resultados de las principales herramientas de calidad de código usadas en este curso: **pytest**, **flake8** y **pylint**.

---

## 1. Pytest

**¿Qué es?**
Pytest es una herramienta para ejecutar tests automáticos en Python. Permite validar que tu código funciona correctamente.

**Instalación:**

```
pip install pytest
```

**Uso básico:**

- Ubica tus archivos de test en la carpeta `tests/` y nómbralos como `test_*.py`.
- Ejecuta todos los tests con:

```
pytest
```

- Para ver más detalles:

```
pytest -v
```

**Interpretación:**

- ✅ Verde: El test pasó correctamente.
- ❌ Rojo: El test falló. Lee el mensaje para entender el error.

---

## 2. Flake8

**¿Qué es?**
Flake8 revisa el estilo y la sintaxis de tu código según las recomendaciones de Python (PEP8).

**Instalación:**

```
pip install flake8
```

**Uso básico:**

- Ejecuta en la raíz del proyecto:

```
flake8 .
```

- Para revisar un solo archivo:

```
flake8 ruta/al/archivo.py
```

**Interpretación:**

- Muestra advertencias y errores de estilo (líneas largas, espacios, nombres, etc).
- Corrige los problemas para mantener tu código limpio y profesional.

---

## 3. Pylint

---

## 4. Pycodestyle

**¿Qué es?**
Revisa que tu código cumpla con el estilo PEP8 (espacios, indentación, longitud de línea, etc).

**Instalación:**

```
pip install pycodestyle
```

**Uso básico:**

- Ejecuta en la raíz del proyecto:

```
pycodestyle .
```

- Para revisar un solo archivo:

```
pycodestyle ruta/al/archivo.py
```

**Interpretación:**

- Muestra advertencias y errores de estilo.
- Corrige los problemas para mantener tu código profesional.

---

## 5. Pydocstyle

**¿Qué es?**
Verifica que tus funciones, clases y módulos tengan docstrings y sigan las convenciones recomendadas.

**Instalación:**

```
pip install pydocstyle
```

**Uso básico:**

- Ejecuta en la raíz del proyecto:

```
pydocstyle .
```

- Para revisar un solo archivo:

```
pydocstyle ruta/al/archivo.py
```

**Interpretación:**

- Muestra advertencias si faltan docstrings o no cumplen el formato.
- Corrige los problemas para mejorar la documentación de tu código.

**¿Qué es?**
Pylint analiza tu código y da una puntuación de calidad, además de sugerencias para mejorarlo.

**Instalación:**

```
pip install pylint
```

**Uso básico:**

- Ejecuta en la raíz del proyecto:

```
pylint modulo_1_fundamentos/clase_1_entorno_profesional/ejemplo_saludo_inteligente.py
```

- Puedes revisar cualquier archivo `.py`.

**Interpretación:**

- Muestra advertencias, errores y una puntuación final.
- Lee los mensajes y corrige los problemas para mejorar la calidad.

---

## Recomendaciones Generales

- Ejecuta estas herramientas antes de entregar tu código.
- Corrige los errores y advertencias para aprender buenas prácticas.
- Usa los reportes para mejorar tu código y entender los estándares profesionales.

---

**¿Dudas?**
Consulta la documentación oficial:

- [Pytest](https://docs.pytest.org/en/stable/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Pylint](https://pylint.pycqa.org/en/latest/)

¡Usa estas herramientas para convertirte en un programador profesional!
