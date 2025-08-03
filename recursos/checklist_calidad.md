# 📋 Lista de Verificación de Calidad - Código Python

> **Guía para estudiantes junior** - Checklist para escribir código Python profesional

## 🎯 Propósito de esta Lista

Esta lista te ayudará a revisar tu código antes de considerarlo "terminado". Un buen desarrollador **siempre revisa** su código antes de entregarlo, y esta guía te ayudará a desarrollar ese hábito profesional desde el primer día.

---

## 📝 CHECKLIST GENERAL DE CALIDAD

### 🏗️ **ESTRUCTURA Y ORGANIZACIÓN**

#### ✅ **Archivos y Nombres**

- [ ] El archivo tiene un nombre descriptivo y claro (ej: `calculadora_estudiantes.py`)
- [ ] El nombre usa snake_case (palabras separadas por guiones bajos)
- [ ] No hay espacios ni caracteres especiales en el nombre del archivo
- [ ] La extensión es `.py` para archivos Python

#### ✅ **Organización del Código**

- [ ] El código está organizado en funciones lógicas
- [ ] Cada función tiene una responsabilidad específica y clara
- [ ] Las funciones no son excesivamente largas (máximo 20-30 líneas)
- [ ] Hay una función `main()` que coordina el programa
- [ ] Se usa `if __name__ == "__main__":` al final del archivo

### 📚 **DOCUMENTACIÓN**

#### ✅ **Comentarios y Docstrings**

- [ ] El archivo tiene un docstring al inicio explicando qué hace el programa
- [ ] Cada función tiene un docstring explicando:
  - Qué hace la función
  - Qué parámetros recibe (Args)
  - Qué retorna (Returns)
- [ ] Los comentarios explican **POR QUÉ** se hace algo, no **QUÉ** se hace
- [ ] No hay código comentado innecesariamente (código "muerto")

#### ✅ **Ejemplo de Documentación Correcta**

```python
def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Args:
        calificaciones (list): Lista de números representando calificaciones

    Returns:
        float: Promedio de las calificaciones, 0 si la lista está vacía
    """
    if not calificaciones:  # Evitar división por cero
        return 0
    return sum(calificaciones) / len(calificaciones)
```

### 🎨 **ESTILO Y LEGIBILIDAD**

#### ✅ **Nomenclatura (Nombres)**

- [ ] Variables usan `snake_case`: `nombre_usuario`, `lista_estudiantes`
- [ ] Constantes usan `MAYUSCULAS`: `EDAD_MINIMA = 18`
- [ ] Funciones usan `snake_case`: `solicitar_nombre()`, `calcular_total()`
- [ ] Los nombres son descriptivos y claros (no `x`, `temp`, `data`)

#### ✅ **Espaciado y Formato**

- [ ] Hay líneas en blanco para separar secciones lógicas
- [ ] Los operadores tienen espacios: `a + b`, no `a+b`
- [ ] Hay espacio después de comas: `funcion(a, b, c)`
- [ ] La indentación es consistente (4 espacios por nivel)
- [ ] Las líneas no son excesivamente largas (máximo 80-100 caracteres)

#### ✅ **Ejemplo de Formato Correcto**

```python
# ✅ Correcto
def procesar_estudiante(nombre, edad, calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)

    if promedio >= 70:
        status = "Aprobado"
    else:
        status = "Reprobado"

    return {
        'nombre': nombre,
        'edad': edad,
        'promedio': promedio,
        'status': status
    }

# ❌ Incorrecto
def procesarestudiante(n,e,c):
    p=sum(c)/len(c)
    if p>=70:s="Aprobado"
    else:s="Reprobado"
    return {'nombre':n,'edad':e,'promedio':p,'status':s}
```

---

## 🔧 CHECKLIST TÉCNICO

### ⚡ **FUNCIONALIDAD**

#### ✅ **Validación de Entrada**

- [ ] Todas las entradas del usuario están validadas
- [ ] Se manejan casos donde el usuario ingresa datos incorrectos
- [ ] Hay mensajes claros cuando la entrada es inválida
- [ ] El programa no se "rompe" con entradas inesperadas

#### ✅ **Manejo de Errores**

- [ ] Se usa `try-except` para operaciones que pueden fallar
- [ ] Los mensajes de error son amigables y útiles para el usuario
- [ ] Se manejan errores específicos (no solo `Exception` genérico)
- [ ] El programa puede recuperarse de errores y continuar

#### ✅ **Ejemplo de Validación Correcta**

```python
def solicitar_edad():
    """Solicita edad con validación robusta"""
    while True:
        try:
            edad_input = input("Ingresa tu edad: ")
            edad = int(edad_input)

            if edad <= 0:
                print("❌ La edad debe ser positiva")
                continue

            if edad > 120:
                print("❌ Verifica la edad ingresada")
                continue

            return edad

        except ValueError:
            print("❌ Debes ingresar un número válido")
```

### 📊 **LÓGICA Y ALGORITMOS**

#### ✅ **Eficiencia Básica**

- [ ] No hay loops infinitos accidentales
- [ ] No se repiten cálculos innecesariamente
- [ ] Se usan las estructuras de datos apropiadas
- [ ] La lógica es clara y directa

#### ✅ **Casos Edge (Casos Límite)**

- [ ] Se manejan listas vacías
- [ ] Se maneja división por cero
- [ ] Se consideran valores extremos (muy grandes, muy pequeños)
- [ ] Se manejan strings vacíos o con solo espacios

---

## 🧪 CHECKLIST DE TESTING

### ✅ **Pruebas Manuales**

- [ ] He probado el programa con entradas válidas típicas
- [ ] He probado con entradas inválidas (texto donde espero números)
- [ ] He probado casos extremos (números muy grandes, listas vacías)
- [ ] He probado interrumpir el programa (Ctrl+C)

### ✅ **Casos de Prueba Básicos**

```python
# Ejemplo: Si tienes una función calcular_promedio()
# Deberías probar:

# Caso normal
promedio = calcular_promedio([85, 90, 78])  # Debería dar ~84.33

# Caso límite
promedio = calcular_promedio([])  # Debería manejar lista vacía

# Caso extremo
promedio = calcular_promedio([100, 0, 50])  # Valores extremos
```

---

## 🤖 CHECKLIST DE USO DE IA

### ✅ **Uso Responsable de IA**

- [ ] **Entiendo** todo el código que escribí (incluso si la IA ayudó)
- [ ] Puedo explicar **línea por línea** qué hace mi código
- [ ] He **validado** que las sugerencias de IA son correctas
- [ ] Documenté **cómo** usé IA en el desarrollo (en comentarios si es relevante)

### ✅ **Aprendizaje con IA**

- [ ] Usé IA para **explicar** conceptos, no solo para generar código
- [ ] Pregunté **por qué** una solución es mejor que otra
- [ ] Usé IA para **revisar** mi código y sugerir mejoras
- [ ] **Experimenté** con las sugerencias antes de implementarlas

---

## 🎯 CHECKLIST ESPECÍFICO POR TIPO DE PROYECTO

### 📊 **Programas con Entrada de Usuario**

- [ ] Valido que las entradas no estén vacías
- [ ] Manejo conversiones de tipo (str a int, etc.)
- [ ] Proporciono mensajes claros sobre qué se espera
- [ ] Permito al usuario reintentar en caso de error

### 🧮 **Calculadoras y Operaciones Matemáticas**

- [ ] Manejo división por cero
- [ ] Valido que los números estén en rangos esperados
- [ ] Redondeo resultados apropiadamente
- [ ] Muestro resultados en formato legible

### 📋 **Gestión de Listas/Datos**

- [ ] Manejo listas vacías apropiadamente
- [ ] Valido índices antes de acceder a elementos
- [ ] Proporciono feedback sobre el estado de los datos
- [ ] Permito búsqueda y filtrado cuando es relevante

---

## 🔍 PROCESO DE REVISIÓN PASO A PASO

### **Paso 1: Revisión Rápida (5 minutos)**

1. ¿El programa ejecuta sin errores?
2. ¿Hace lo que se supone que debe hacer?
3. ¿Los nombres de variables y funciones son claros?

### **Paso 2: Revisión de Calidad (10 minutos)**

1. Revisa cada ítem de este checklist
2. Lee el código como si fuera la primera vez
3. ¿Entiendes qué hace cada parte?

### **Paso 3: Revisión con IA (5 minutos)**

```
Prompt sugerido:
"Revisa este código Python y sugiere 3 mejoras específicas
para hacerlo más profesional y mantenible. Soy estudiante
principiante, explica cada sugerencia claramente.

[PEGAR CÓDIGO AQUÍ]"
```

### **Paso 4: Testing Final (5 minutos)**

1. Prueba el programa con datos normales
2. Prueba con datos incorrectos
3. Prueba casos extremos

---

## 💡 CONSEJOS PARA DESARROLLAR BUENOS HÁBITOS

### 🎯 **Para Estudiantes Junior**

1. **No te saltes la validación** - Siempre asume que el usuario hará algo inesperado
2. **Escribe primero, optimiza después** - Haz que funcione, luego hazlo bonito
3. **Documenta mientras escribes** - No lo dejes para después
4. **Prueba frecuentemente** - No escribas 100 líneas sin probar

### 🚀 **Para Desarrollar Profesionalismo**

1. **Trata cada ejercicio como un proyecto real**
2. **Piensa en quien va a leer tu código** (incluido tú en 6 meses)
3. **Busca feedback** de compañeros e instructores
4. **Mantén un portafolio** de tus mejores trabajos

---

## 📊 PLANTILLA DE AUTOEVALUACIÓN

```markdown
# AUTOEVALUACIÓN - [Nombre del Proyecto]

## ✅ Checklist Completado

- [ ] Estructura y organización
- [ ] Documentación
- [ ] Estilo y legibilidad
- [ ] Funcionalidad
- [ ] Manejo de errores
- [ ] Testing básico
- [ ] Uso responsable de IA

## 🎯 Aspectos Destacados

[¿Qué salió especialmente bien?]

## 🔧 Áreas de Mejora Identificadas

[¿Qué podrías mejorar la próxima vez?]

## 🤖 Uso de IA en este Proyecto

[¿Cómo te ayudó la IA? ¿Qué aprendiste?]

## 📈 Próximos Pasos

[¿Qué vas a aplicar en el siguiente proyecto?]
```

---

## 🏆 NIVELES DE CALIDAD

### 🌟 **Nivel Principiante** (Meta para primeras 3 clases)

- Código funciona correctamente
- Nombres de variables son descriptivos
- Hay validación básica de entrada
- Documentación mínima presente

### 🚀 **Nivel Intermedio** (Meta para clases 4-6)

- Código bien organizado en funciones
- Manejo robusto de errores
- Documentación completa
- Pruebas básicas realizadas

### 💎 **Nivel Avanzado** (Meta para clases 7-8)

- Código modular y reutilizable
- Excelente documentación y comentarios
- Testing comprehensivo
- Consideraciones de rendimiento y escalabilidad

---

**🎯 Recuerda: La calidad no se logra de un día para otro. Usa esta lista como guía para mejorar constantemente, no como una carga. ¡Cada pequeña mejora cuenta!**

_"El código se lee mucho más veces de las que se escribe. Escribe para el futuro tú que tendrá que entenderlo."_
