## � Consigna de la tarea

1. Clona el repositorio desde GitHub Classroom.
2. Crea y activa tu entorno virtual.
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Lee el README y la guía de calidad.
5. Completa y mejora el archivo `ejemplo_saludo_inteligente.py` siguiendo las buenas prácticas y sugerencias.
6. Escribe y/o mejora los tests en la carpeta `tests/` usando pytest.
7. Revisa tu código con flake8, pylint, pycodestyle y pydocstyle usando el Makefile.
8. Haz commit y push de tus cambios.
9. Verifica que el workflow de GitHub Actions pase correctamente.

---

## ✅ Checklist de entrega

- [ ] El programa funciona y cumple con la consigna.
- [ ] El código pasa los tests de pytest.
- [ ] El código está libre de errores de estilo y documentación (flake8, pylint, pycodestyle, pydocstyle).
- [ ] El README incluye tu reflexión y comentarios sobre la mejora implementada.
- [ ] El workflow de CI pasa sin errores.

---

---

## 🛠️ Uso del Makefile para calidad de código

Puedes automatizar la ejecución de herramientas de calidad y tests usando el archivo `Makefile`.

**Comandos principales:**

Solo necesitas el archivo `Makefile` en la raíz del proyecto. No es necesario crear archivos extra para usar estas herramientas, pero sí debes tener tus scripts y tests organizados en carpetas como `modulo_1_fundamentos/` y `tests/`.

**Ejemplo de uso:**

```
make test
make lint
make style
make clean
```

## 🖥️ Instalación de Chocolatey y Make en Windows

Para usar el Makefile en Windows, necesitas instalar Chocolatey y Make. Sigue estos pasos:

1. Abre PowerShell como administrador y ejecuta:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
2. Instala Make:
   ```cmd
   choco install make
   ```
3. Verifica que ambos comandos funcionen:
   ```cmd
   choco --version
   make --version
   ```
4. Si no funcionan, agrega manualmente la ruta `C:\ProgramData\chocolatey\bin` al PATH del sistema.

Consulta la guía completa en `setup_install_chocolatey_make.md` para más detalles y solución de problemas.

> **Programa Educativo Profesional** - Formación moderna de programadores Python con asistencia de IA

## 📋 Descripción del Programa

Este curso intensivo está diseñado para estudiantes **junior** que desean aprender programación Python moderna utilizando herramientas de **Inteligencia Artificial** como copiloto de desarrollo. El programa combina fundamentos sólidos con prácticas profesionales actuales, preparando a los estudiantes para el mercado laboral tech contemporáneo.

### 🎯 ¿Por qué este curso es diferente?

- **🤖 IA como herramienta educativa**: Aprende a programar **CON** inteligencia artificial, no **POR** ella
- **📈 Enfoque gradual**: Desde conceptos básicos hasta proyectos profesionales
- **💼 Orientación laboral**: Prácticas y proyectos del mundo real
- **🔧 Herramientas modernas**: VS Code, GitHub, pytest, y más
- **📚 Documentación profesional**: Cada línea de código explicada y justificada

## 🏗️ Estructura del Programa

### **MÓDULO 1: Fundamentos Modernos de Programación con Python e IA**

_Duración: 4 semanas | 8 clases_

En este módulo aprenderás el ecosistema moderno de Python, instalación y configuración de herramientas con IA como entorno de desarrollo principal. Dominarás la sintaxis básica, estructuras fundamentales y su uso en contextos reales, sentando las bases del pensamiento computacional profesional.

#### 📅 Cronograma de Clases:

| Clase | Tema                                      | Enfoque Principal              |
| ----- | ----------------------------------------- | ------------------------------ |
| **1** | 🛠️ Entorno profesional con IA y VS Code   | Configuración y primeros pasos |
| **2** | 📊 Variables, tipos de datos y operadores | Fundamentos con validación IA  |
| **3** | 🔄 Estructuras de control y lógica        | Decisiones y repeticiones      |
| **4** | 📝 Funciones y modularidad                | Código reutilizable y limpio   |
| **5** | 📋 Estructuras de datos fundamentales     | Listas, tuplas, diccionarios   |
| **6** | ⚠️ Manejo de errores y depuración         | Robustez con asistencia IA     |
| **7** | 📈 Proyecto integrador avanzado           | Sistema completo funcional     |
| **8** | 🎯 Tutoría final y optimización           | Revisión y mejora profesional  |

### **MÓDULO 2: Programación Orientada a Objetos (POO)**

_Próximamente - Clases, herencia, polimorfismo_

### **MÓDULO 3: Estructuras de Datos y Algoritmos**

_Próximamente - Optimización y pensamiento algorítmico_

### **MÓDULO 4: Archivos, APIs y Persistencia**

_Próximamente - Manejo de datos y conexiones externas_

## 🚀 Comenzando tu Viaje

### Prerrequisitos Mínimos

- 💻 Computadora con Windows, macOS o Linux
- 🌐 Conexión a internet estable
- 📚 Conocimientos básicos de computación (archivos, carpetas, instalación de software)
- 🎯 **Actitud de aprendizaje** y curiosidad por la programación
- ⏰ Dedicación de **8-10 horas semanales**

### Instalación Rápida

```bash
# 1. Clona este repositorio
git clone [URL-del-template]
cd python-junior-template

# 2. Sigue la guía de instalación completa
# Ver archivo: setup_instructions.md

# 3. Verifica tu instalación
python --version
code --version
```

## 🎓 Metodología de Aprendizaje

### 🔄 Ciclo de Aprendizaje por Clase:

1. **📖 Teoría** (20 min): Conceptos fundamentales explicados claramente
2. **💻 Práctica guiada** (40 min): Ejercicios con asistencia de IA
3. **🔧 Proyecto aplicado** (30 min): Implementación de conocimientos
4. **🔍 Revisión y optimización** (20 min): Mejora continua del código
5. **📝 Documentación** (10 min): Reflexión y consolidación

### 🤖 Uso Estratégico de Inteligencia Artificial:

#### ✅ **Qué SÍ hacer con IA:**

- Obtener explicaciones de conceptos difíciles
- Sugerir mejoras a tu código existente
- Generar casos de prueba para validar funciones
- Ayudar con documentación y comentarios
- Depurar errores y encontrar soluciones
- Explorar alternativas de implementación

#### ❌ **Qué NO hacer con IA:**

- Copiar código sin entenderlo
- Saltarse el proceso de aprendizaje
- Depender completamente de generación automática
- Evitar pensar por ti mismo
- Usar IA para hacer trampa en evaluaciones

### 📊 Sistema de Evaluación:

| Componente                 | Peso | Descripción                            |
| -------------------------- | ---- | -------------------------------------- |
| **Proyectos prácticos**    | 40%  | Sistemas funcionales desarrollados     |
| **Participación en clase** | 20%  | Ejercicios y actividades               |
| **Documentación**          | 20%  | Comentarios, README, reflexiones       |
| **Uso responsable de IA**  | 10%  | Aplicación estratégica de herramientas |
| **Presentación final**     | 10%  | Demostración de proyecto integrador    |

## 🛠️ Herramientas y Tecnologías

### Software Principal:

- **🐍 Python 3.9+**: Lenguaje de programación
- **💻 Visual Studio Code**: Editor/IDE principal
- **🤖 GitHub Copilot**: Asistente de código con IA
- **📱 Git & GitHub**: Control de versiones
- **🧪 pytest**: Framework de testing
- **📏 flake8 & pylint**: Herramientas de calidad de código
- **📚 Jupyter Notebooks**: Experimentación y aprendizaje

### Recursos de IA Recomendados:

- **GitHub Copilot**: Autocompletado inteligente
- **ChatGPT/Claude**: Explicaciones y consultas
- **Python Tutor**: Visualización de ejecución
- **Replit**: Entorno de desarrollo online

## 📚 Estructura de Archivos del Curso

```
python-junior-template/
├── 📄 README.md                     # Esta guía principal
├── ⚙️ setup_instructions.md         # Instalación paso a paso
├── 📦 requirements.txt              # Dependencias Python
├── 🚫 .gitignore                    # Configuración Git
├── 📁 modulo_1_fundamentos/         # Módulo 1 completo
│   ├── 📁 clase_1_entorno_profesional/
│   ├── 📁 clase_2_variables_tipos/
│   ├── 📁 clase_3_control_flujo/
│   ├── 📁 clase_4_funciones/
│   ├── 📁 clase_5_estructuras_datos/
│   ├── 📁 clase_6_manejo_errores/
│   ├── 📁 clase_7_proyecto_integrador/
│   └── 📁 clase_8_tutoria_final/
├── 📁 recursos/                     # Material de apoyo
│   ├── 📋 checklist_calidad.md      # Lista de verificación
│   ├── 🎯 presentaciones/           # Slides de las clases
│   └── 🤖 guias_ia/                 # Guías de uso de IA
└── 📁 .github/workflows/            # Automatización CI/CD
    └── 🔧 python-app.yml            # Testing automático
```

## 🎯 Objetivos de Aprendizaje por Módulo

### 📈 **Al completar el Módulo 1, podrás:**

- ✅ Configurar un entorno de desarrollo profesional
- ✅ Escribir programas Python estructurados y documentados
- ✅ Utilizar IA como herramienta de aprendizaje y productividad
- ✅ Manejar errores y depurar código efectivamente
- ✅ Crear proyectos funcionales con interfaces de usuario
- ✅ Trabajar con Git y GitHub para control de versiones
- ✅ Aplicar buenas prácticas de programación desde el inicio

### 🏆 **Competencias Profesionales Desarrolladas:**

- **Pensamiento computacional**: Descomposición de problemas complejos
- **Programación limpia**: Código legible, mantenible y documentado
- **Colaboración digital**: Trabajo con herramientas de desarrollo modernas
- **Aprendizaje continuo**: Autonomía para resolver problemas nuevos
- **Comunicación técnica**: Documentación y presentación de proyectos

## 🌟 Proyectos Destacados

Durante el curso desarrollarás varios proyectos prácticos:

### 🎯 **Proyecto Módulo 1**: Sistema de Gestión de Estudiantes

Un sistema completo con:

- Registro de estudiantes con validación
- Gestión de calificaciones por materias
- Reportes estadísticos automáticos
- Identificación de estudiantes en riesgo académico
- Interfaz de usuario intuitiva y colorida

### 📈 **Características del Proyecto:**

- **+500 líneas de código** bien documentadas
- **Validación robusta** de datos de entrada
- **Manejo profesional de errores**
- **Interfaz colorida** para mejor experiencia de usuario
- **Documentación completa** con manual de usuario
- **Testing automatizado** con pytest

## 👥 Comunidad de Aprendizaje

### 🤝 **Forma parte de nuestra comunidad:**

- **📱 Discord del curso**: Comunicación directa con compañeros
- **💬 Foros de discusión**: Resolución colaborativa de dudas
- **👨‍🏫 Horas de oficina**: Sesiones de tutoría personalizada
- **🎉 Eventos de networking**: Conexión con la industria tech

### 📢 **Canales de Comunicación:**

- **🚀 Anuncios importantes**: Email + Discord
- **❓ Dudas técnicas**: Foros especializados por tema
- **🔧 Problemas de configuración**: Canal de soporte técnico
- **💡 Proyectos e ideas**: Showcase de estudiantes

## 🏅 Certificación y Reconocimientos

### 🎓 **Al completar exitosamente:**

- **Certificado digital** de finalización del programa
- **Badge profesional** para LinkedIn y CV
- **Proyecto de portafolio** documentado en GitHub
- **Carta de recomendación** del instructor (estudiantes destacados)
- **Acceso al programa de mentorías** para graduados

### 📈 **Seguimiento Post-Graduación:**

- Invitación a **eventos de antiguos alumnos**
- Acceso a **bolsa de trabajo exclusiva**
- **Descuentos en cursos avanzados**
- **Red profesional** de contactos tech

## 📞 Contacto y Soporte

### 👨‍🏫 **Equipo Docente:**

- **Instructor Principal**: [Nombre del instructor]
- **Asistentes de Cátedra**: [Nombres de asistentes]
- **Soporte Técnico**: [Contacto soporte]

### 📧 **Canales de Contacto:**

- **Email oficial**: curso.python.ia@[institución]
- **Discord del curso**: [Enlace de invitación]
- **Horas de oficina**: Martes y Jueves 18:00-19:00

---

## 🚀 ¡Comienza tu Viaje de Programación Hoy!

> **"El mejor momento para aprender a programar fue hace 10 años. El segundo mejor momento es AHORA."**

### 📋 **Próximos Pasos:**

1. **📖 Lee** las instrucciones de configuración en `setup_instructions.md`
2. **⚙️ Configura** tu entorno de desarrollo siguiendo la guía
3. **✅ Verifica** que todo funcione correctamente
4. **🎯 Dirígete** a `modulo_1_fundamentos/clase_1_entorno_profesional/`
5. **🚀 ¡Empieza** tu primera clase!

### 🌟 **Recuerda:**

- La programación es una **habilidad práctica** - se aprende programando
- Los errores son **oportunidades de aprendizaje** - no te desanimes
- La IA es tu **copiloto**, pero tú eres el **piloto**
- La **consistencia** es más importante que la perfección
- **Disfruta el proceso** - ¡la programación es creativa y divertida!

---

**¡Bienvenido a tu nueva carrera en tecnología! 🎉**

_© 2025 - Curso Python Junior con IA. Todos los derechos reservados._
