# 📋 Lista de Verificación - Calidad de Código Python

## 🎯 Objetivo

Esta checklist garantiza que el código Python cumple con estándares profesionales de calidad, legibilidad y mantenibilidad.

---

## 📝 ESTRUCTURA Y ORGANIZACIÓN

### Organización de Archivos

- [ ] **Nombres de archivos descriptivos** usando snake_case
- [ ] **Estructura de carpetas lógica** y consistente
- [ ] **Separación de responsabilidades** en módulos diferentes
- [ ] **Archivo README.md** presente y completo
- [ ] **requirements.txt** con dependencias específicas

### Estructura de Código

- [ ] **Imports organizados** (estándar, terceros, locales)
- [ ] **Funciones de máximo 20-30 líneas** (principio de responsabilidad única)
- [ ] **Clases bien definidas** con propósito claro
- [ ] **Constantes en MAYÚSCULAS** al inicio del archivo
- [ ] **Variables globales minimizadas** o eliminadas

---

## 🎨 ESTILO Y FORMATO (PEP 8)

### Espaciado y Líneas

- [ ] **Máximo 79 caracteres por línea** (o 88 con Black)
- [ ] **Dos líneas en blanco** antes de definiciones de clase
- [ ] **Una línea en blanco** antes de definiciones de función
- [ ] **Espacios alrededor de operadores** (=, +, -, etc.)
- [ ] **Sin espacios en paréntesis** internos

### Convenciones de Nombres

- [ ] **Variables y funciones**: `snake_case`
- [ ] **Clases**: `PascalCase`
- [ ] **Constantes**: `UPPER_SNAKE_CASE`
- [ ] **Métodos privados**: `_leading_underscore`
- [ ] **Nombres descriptivos** que explican el propósito

### Strings y Comillas

- [ ] **Consistencia en comillas** (simples o dobles)
- [ ] **f-strings para interpolación** cuando sea posible
- [ ] **Strings multilínea** con triple comillas para documentación

---

## 📚 DOCUMENTACIÓN

### Docstrings

- [ ] **Todas las funciones públicas** tienen docstring
- [ ] **Todas las clases** tienen docstring descriptivo
- [ ] **Formato consistente** (Google, NumPy, o Sphinx style)
- [ ] **Descripción de parámetros** y tipos
- [ ] **Descripción de valor de retorno**

### Comentarios

- [ ] **Comentarios explican "por qué"**, no "qué"
- [ ] **Comentarios actualizados** con el código
- [ ] **Sin comentarios obvios** (evitar redundancia)
- [ ] **Comentarios complejos** bien explicados
- [ ] **TODO/FIXME** marcados para trabajo futuro

---

## 🛡️ VALIDACIONES Y MANEJO DE ERRORES

### Validación de Entrada

- [ ] **Validación de parámetros** en funciones públicas
- [ ] **Verificación de tipos** cuando sea necesario
- [ ] **Manejo de valores None** y vacíos
- [ ] **Validación de rangos** para números
- [ ] **Sanitización de strings** cuando sea apropiado

### Manejo de Excepciones

- [ ] **Try-except específicos** (evitar except genérico)
- [ ] **Logging de errores** cuando sea apropiado
- [ ] **Cleanup en bloques finally** si es necesario
- [ ] **Excepciones personalizadas** para errores específicos
- [ ] **Propagación adecuada** de excepciones

---

## ⚡ RENDIMIENTO Y EFICIENCIA

### Algoritmos y Estructuras

- [ ] **Complejidad algorítmica razonable** para el caso de uso
- [ ] **Estructuras de datos apropiadas** (list vs dict vs set)
- [ ] **Evitar bucles anidados** innecesarios
- [ ] **List comprehensions** cuando mejoren legibilidad
- [ ] **Generators** para secuencias grandes

### Optimizaciones

- [ ] **Avoid premature optimization** (legibilidad primero)
- [ ] **Reutilización de objetos** costosos cuando sea apropiado
- [ ] **Lazy loading** para recursos pesados
- [ ] **Caching** para cálculos repetitivos caros
- [ ] **Profiling realizado** si el rendimiento es crítico

---

## 🧪 TESTING Y VERIFICACIÓN

### Pruebas

- [ ] **Casos de prueba para funciones críticas**
- [ ] **Testing de casos edge** (valores límite)
- [ ] **Mocking de dependencias externas**
- [ ] **Cobertura de código** razonable (>80%)
- [ ] **Pruebas automatizadas** ejecutables

### Verificación Manual

- [ ] **Código ejecuta sin errores**
- [ ] **Casos de uso principales funcionan**
- [ ] **Manejo correcto de errores esperados**
- [ ] **UI/UX intuitiva** (si aplica)
- [ ] **Datos persistidos correctamente** (si aplica)

---

## 🔒 SEGURIDAD Y MEJORES PRÁCTICAS

### Seguridad Básica

- [ ] **Validación de entrada** para prevenir inyecciones
- [ ] **Secrets y passwords** no hardcoded
- [ ] **Manejo seguro de archivos** (paths, permisos)
- [ ] **Escape de HTML/SQL** cuando sea necesario
- [ ] **Logging sin información sensible**

### Mejores Prácticas

- [ ] **DRY (Don't Repeat Yourself)** - código no duplicado
- [ ] **KISS (Keep It Simple, Stupid)** - soluciones simples
- [ ] **YAGNI (You Aren't Gonna Need It)** - no sobre-ingeniería
- [ ] **Single Responsibility Principle** aplicado
- [ ] **Separation of Concerns** respetado

---

## 🤖 USO DE IA (GitHub Copilot, ChatGPT, etc.)

### Documentación de Uso

- [ ] **Documentar qué partes** fueron generadas por IA
- [ ] **Explicar el prompt** usado para generar código
- [ ] **Verificar y entender** todo código generado
- [ ] **Modificar código generado** para cumplir estándares
- [ ] **Agregar tests** para código generado por IA

### Validación de IA

- [ ] **Revisar lógica** de algoritmos generados
- [ ] **Verificar edge cases** no considerados por IA
- [ ] **Asegurar compatibilidad** con el resto del código
- [ ] **Confirmar estilo** consistente con el proyecto
- [ ] **Validar seguridad** del código generado

---

## 📊 MÉTRICAS DE CALIDAD

### Métricas Objetivas

- [ ] **Complejidad ciclomática** < 10 por función
- [ ] **Profundidad de anidación** < 4 niveles
- [ ] **Longitud de función** < 30 líneas
- [ ] **Número de parámetros** < 5 por función
- [ ] **Cohesión alta, acoplamiento bajo**

### Métricas Subjetivas

- [ ] **Código es fácil de leer** para otros desarrolladores
- [ ] **Intención del código es clara** sin documentación adicional
- [ ] **Modificaciones futuras** serían straightforward
- [ ] **Debugging sería manejable** en caso de errores
- [ ] **Código inspira confianza** en su correctitud

---

## ✅ CHECKLIST FINAL

### Pre-commit

- [ ] **Linter ejecutado** (pylint, flake8) sin errores críticos
- [ ] **Formatter aplicado** (black, autopep8)
- [ ] **Type checker** ejecutado (mypy) si se usan type hints
- [ ] **Tests pasando** al 100%
- [ ] **Documentación actualizada**

### Pre-review

- [ ] **Self-review completado**
- [ ] **Casos de uso manuales probados**
- [ ] **Performance acceptable** para casos de uso esperados
- [ ] **Backwards compatibility** preservada (si aplica)
- [ ] **Logs útiles** para debugging

### Pre-deployment

- [ ] **Dependencias documentadas** y versionadas
- [ ] **Configuración de entorno** documentada
- [ ] **Rollback plan** definido
- [ ] **Monitoring** considerado
- [ ] **Documentation** de usuario actualizada

---

## 🎯 SCORING

**Puntaje por sección:**

- Estructura y Organización: \_\_\_/5
- Estilo y Formato: \_\_\_/5
- Documentación: \_\_\_/5
- Validaciones y Errores: \_\_\_/5
- Rendimiento: \_\_\_/5
- Testing: \_\_\_/5
- Seguridad: \_\_\_/5
- Uso de IA: \_\_\_/5
- Métricas de Calidad: \_\_\_/5
- Checklist Final: \_\_\_/5

**TOTAL: \_\_\_/50**

### Calificación:

- **45-50**: Código de calidad profesional ⭐⭐⭐⭐⭐
- **40-44**: Muy buena calidad ⭐⭐⭐⭐
- **35-39**: Buena calidad ⭐⭐⭐
- **30-34**: Calidad aceptable ⭐⭐
- **<30**: Necesita mejoras significativas ⭐

---

**💡 Tip**: Usa esta checklist progresivamente. No es necesario cumplir todos los puntos desde el inicio, sino ir mejorando iterativamente la calidad del código.

**🚀 Objetivo**: El código debe ser tan claro que otro desarrollador (o tú en 6 meses) pueda entenderlo y modificarlo fácilmente.
