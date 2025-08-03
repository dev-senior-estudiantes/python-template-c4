# Clase 1: Preparando el entorno profesional con herramientas IA y Visual Studio Code>

**🎯 Objetivo**: Configurar un entorno de desarrollo moderno y asistido con IA para comenzar tu carrera como programador Python profesional.

## 📚 ¿Qué aprenderás hoy?Al final de esta clase podrás:

- ✅ **Configurar** un entorno de desarrollo profesional completo
- ✅ **Comprender** el rol del programador moderno y el uso de asistentes IA
- ✅ **Ejecutar** tu primer programa Python con buenas prácticas
- ✅ **Utilizar** herramientas de IA para mejorar tu código desde el primer día
- ✅ **Identificar** y resolver errores comunes con ayuda de IA

## 🎬 Introducción: El Programador Profesional del 2025

### 🚀 **¿Qué hace diferente a un programador profesional moderno?**

En 2025, un programador exitoso **NO** es alguien que memoriza sintaxis o escribe todo desde cero. Es alguien que:1.

**🧠 Piensa en soluciones**, no en código2.
**🤖 Usa IA estratégicamente** como copiloto, no como piloto automático3.
**📚 Documenta y comunica** efectivamente sus decisiones4.
**🔧 Mantiene código limpio** y reutilizable5.
**🌱 Aprende continuamente** y se adapta a nuevas herramientas

### 💡 **La IA como tu Copiloto de Desarrollo**Imagina que estás aprendiendo a manejar:-

**❌ Enfoque tradicional**: Memorizar cada botón del auto antes de encenderlo-

**✅ Enfoque moderno**: Aprender a manejar CON un copiloto experto que te guíaLa IA (como GitHub Copilot, ChatGPT, Claude) es tu **copiloto de programación**:

- Te sugiere código, pero **TÚ decides** si usarlo
- Te explica conceptos, pero **TÚ entiendes** la lógica
- Te ayuda a depurar, pero **TÚ aprendes** de los errores

## 🛠️ Configuración del Entorno (Repaso Práctico)

### ✅Verificación Rápida

- ¿Todo está instalado?\*\* Abre tu terminal/cmd y ejecuta estos comandos:

Ejecuta estos comandos en tu terminal/cmd para verificar la instalación:

```bash
# Verificar Python
python --version         # Debería mostrar: Python 3.11.x

# Verificar pip
pip --version            # Debería mostrar: pip 23.x.x from ...

# Verificar Git
git --version            # Debería mostrar: git version 2.x.x

# Verificar VS Code
code --version           # Debería mostrar la versión de VS Code
```

### 🔧Si algo no funciona:

**Usa IA** para diagnosticar: "Tengo este error: [pegar error], ¿cómo lo soluciono?"

## 🎯 Primera Ejecución: ¡Tu Primer Programa!

### 📝 Ejercicio: El Saludo Inteligente

Vamos a crear tu primer programa con validación de datos y mejoras asistidas por IA.

#### Paso 1: Crear el archivo

```bash
# En tu terminal, dentro de esta carpeta
code ejemplo_saludo_inteligente.py
```

#### Paso 2: Código inicial básico

```python
# ejemplo_saludo_inteligente.py
print("¡Hola, mundo!")
```

#### Paso 3: Ejecutar y verificar

```bash
python ejemplo_saludo_inteligente.py
```

¡Perfecto! Pero este código es muy básico. Vamos a mejorarlo profesionalmente.

#### Ejercicio extra: Saludo Personalizado con Validación

Abre el archivo `ejemplo_saludo_inteligente.py` y mejora el programa siguiendo la estructura y sugerencias del README.

Incluye:

- Solicitud y validación del nombre
- Solicitud y validación de la edad
- Saludo personalizado según la edad
- Manejo de errores básicos

Puedes usar el ejemplo de código que aparece en este README como referencia.

---

## 📝 Ejercicio Práctico de la Clase

### 🎯 Ejercicio Principal: Calculadora de Bienvenida

Crea un programa `calculadora_bienvenida.py` que:

1. Salude al usuario y solicite su nombre
2. Pida dos números con validación
3. Ofrezca 4 operaciones (suma, resta, multiplicación, división)
4. Muestre el resultado de forma profesional
5. Maneje errores como división por cero

#### Requisitos técnicos:

- Usar funciones para organizar el código
- Validar todas las entradas del usuario
- Manejar errores con try-except
- Incluir documentación (docstrings)
- Mostrar mensajes amigables y profesionales

#### Estructura sugerida:

```python
def solicitar_nombre():
    """Solicita y valida el nombre del usuario"""
    pass

def solicitar_numero(mensaje):
    """Solicita y valida un número del usuario"""
    pass

def mostrar_menu():
    """Muestra las opciones de operación"""
    pass

def realizar_operacion(num1, num2, operacion):
    """Realiza la operación matemática solicitada"""
    pass

def main():
    """Función principal del programa"""
    pass

if __name__ == "__main__":
    main()
```

    print("=" * 50)

# Clase 1: Preparando el entorno profesional con herramientas IA y Visual Studio Code

````
Soy un estudiante principiante de Python.
¿Puedes revisar este código y sugerir 3 mejoras específicas
que lo hagan más profesional? Explica cada mejora de forma simple.

1. Elige **UNA** sugerencia de la IA
2. Implementa el cambio **entendiendo** qué hace
3. Ejecuta el programa para verificar que funciona
4. Documenta qué cambio hiciste y por qué

#### **Paso 3: Reflexión**

Escribe en comentarios:

```python
"""
MEJORA IMPLEMENTADA:
- ¿Qué cambié?
- ¿Qué aprendí en el proceso?
"""

### 🚨 **Errores que verás frecuentemente:**

#### **1. SyntaxError - Error de Sintaxis**

```python
# Código con error:
print("Hola mundo"  # Falta paréntesis de cierre

# Error que verás:
# SyntaxError: unexpected EOF while parsing
````

**🤖 Cómo usar IA para solucionarlo:**

```
Prompt: "Tengo este SyntaxError en Python: [pegar error completo].
¿Qué significa y cómo lo arreglo?"
```

#### **2. NameError - Variable no definida**

```python
# Código con error:
print(nombre)  # Variable 'nombre' no está definida

# Error que verás:
# NameError: name 'nombre' is not defined
```

#### **3. TypeError - Tipo de dato incorrecto**

```python
# Código con error:
edad = "25"
print(edad + 5)  # No se puede sumar string + int

# Error que verás:
# TypeError: can only concatenate str (not "int") to str
```

#### **4. IndentationError - Indentación incorrecta**

```python
# Código con error:
def mi_funcion():
print("Hola")  # Falta indentación

# Error que verás:
# IndentationError: expected an indented block
```

### 🛠️ **Estrategias para depurar con IA:**

1. **Lee el error completo** - no solo la primera línea
2. **Copia el error exacto** al consultar con IA
3. **Incluye el código** que causó el error
4. **Pregunta específicamente** qué significa y cómo solucionarlo
5. **Implementa la solución** entendiendo el por qué

## 📝 Ejercicios Prácticos de la Clase

### 🎯 **Ejercicio Principal: Calculadora de Bienvenida**

Crea un programa `calculadora_bienvenida.py` que:

1. **Salude al usuario** y solicite su nombre
2. **Pida dos números** con validación
3. **Ofrezca 4 operaciones** (suma, resta, multiplicación, división)
4. **Muestre el resultado** de forma profesional
5. **Maneje errores** como división por cero

#### **Requisitos técnicos:**

- ✅ Usar funciones para organizar el código
- ✅ Validar todas las entradas del usuario
- ✅ Manejar errores con try-except
- ✅ Incluir documentación (docstrings)
- ✅ Mostrar mensajes amigables y profesionales

#### **Estructura sugerida:**

```python
def solicitar_nombre():
    """Solicita y valida el nombre del usuario"""
    pass

def solicitar_numero(mensaje):
    """Solicita y valida un número del usuario"""
    pass

def mostrar_menu():
    """Muestra las opciones de operación"""
    pass

def realizar_operacion(num1, num2, operacion):
    """Realiza la operación matemática solicitada"""
    pass

def main():
    """Función principal del programa"""
    pass

if __name__ == "__main__":
    main()
```

### 🤖 **Cómo usar IA para este ejercicio:**

#### **Prompt de ayuda inicial:**

```
Soy un estudiante principiante de Python. Necesito crear una calculadora
simple que pida nombre del usuario, dos números, y haga operaciones básicas.
¿Puedes explicarme la estructura general y qué funciones necesito?
NO escribas el código completo, solo guíame con la lógica.
```

#### **Prompt para validación:**

```
¿Cómo puedo validar que el usuario ingrese un número válido en Python?
Necesito manejar casos como texto en lugar de números, números negativos, etc.
Explícame con un ejemplo simple.
```

#### **Prompt para depuración:**

```
Mi código tiene este error: [pegar error]
Este es el código que lo causa: [pegar código]
¿Qué está mal y cómo lo soluciono? Soy principiante, explica de forma simple.
```

## 🎯 Objetivos de Aprendizaje - Autoevaluación

Al final de esta clase, deberías poder responder:

### 📚 **Conceptos:**

- [ ] ¿Qué es un entorno de desarrollo y por qué es importante?
- [ ] ¿Cuál es la diferencia entre usar IA como "copiloto" vs "piloto automático"?
- [ ] ¿Qué son las funciones y por qué organizan mejor el código?
- [ ] ¿Por qué es importante validar las entradas del usuario?

### 💻 **Habilidades Prácticas:**

- [ ] ¿Puedes crear un archivo Python y ejecutarlo desde terminal?
- [ ] ¿Puedes identificar y corregir errores básicos de sintaxis?
- [ ] ¿Puedes usar IA para obtener ayuda sin copiar ciegamente?
- [ ] ¿Puedes escribir funciones simples con documentación?

### 🔧 **Herramientas:**

- [ ] ¿VS Code está configurado y funcionando correctamente?
- [ ] ¿Puedes usar el autocompletado y sugerencias?
- [ ] ¿Git está instalado y configurado con tu identidad?
- [ ] ¿Sabes cómo ejecutar Python desde la terminal?

## 📚 Recursos Adicionales para Estudio

### 🔗 **Enlaces Recomendados:**

- **Python.org Tutorial**: https://docs.python.org/3/tutorial/
- **Real Python Beginner**: https://realpython.com/python-first-steps/
- **VS Code Python Setup**: https://code.visualstudio.com/docs/python/python-tutorial

### 📖 **Para leer esta semana:**

- **PEP 8 - Style Guide**: https://peps.python.org/pep-0008/ (solo introducción)
- **Python Naming Conventions**: Cómo nombrar variables y funciones

### 🤖 **Prompts útiles para IA:**

```
"Explícame [concepto] en Python como si fuera un principiante"
"¿Cuáles son las mejores prácticas para [tema específico]?"
"Tengo este error: [error]. ¿Qué significa y cómo lo soluciono?"
"¿Cómo puedo mejorar este código para que sea más profesional?"
```

## 🎉 ¡Felicitaciones!

Has completado tu primera clase del curso Python con IA.

### 🚀 **Lo que lograste hoy:**

- ✅ Configuraste un entorno de desarrollo profesional
- ✅ Escribiste tu primer programa Python con buenas prácticas
- ✅ Aprendiste a usar IA como herramienta de aprendizaje
- ✅ Implementaste validación básica de datos
- ✅ Manejaste errores comunes de programación

### 📈 **Próximos pasos:**

1. **Practica** los ejercicios adicionales
2. **Experimenta** con el código - rompe cosas y arregla errores
3. **Documenta** tus aprendizajes en comentarios
4. **Prepárate** para la Clase 2: Variables, tipos de datos y operadores

### 💡 **Consejo de tu instructor:**

> _"La programación se aprende programando. No tengas miedo de experimentar,
> cometer errores, y hacer preguntas. La IA está aquí para ayudarte,
> pero tú eres quien debe entender y tomar las decisiones."_

---

**🎯 Siguiente clase:** `clase_2_variables_tipos/` - Variables, tipos de datos y operadores con validación asistida por IA.

**📝 Para la próxima clase:** Trae dudas específicas sobre lo que practicaste hoy. ¡Nos vemos en la Clase 2!
