# 🛠️ Instrucciones de Configuración del Entorno> **Guía completa para estudiantes junior** - Configuración paso a paso del entorno de desarrollo moderno con Python e IA## 📋 Prerrequisitos del Sistema### 💻 **Requisitos Mínimos:**- **Sistema Operativo**: Windows 10+, macOS 10.14+, o Linux Ubuntu 18.04+- **RAM**: 4GB mínimo (8GB recomendado)- **Espacio en disco**: 5GB libres- **Conexión a internet**: Estable para descargas y herramientas IA- **Cuenta GitHub**: Gratuita (crear en github.com)### 🎯 **Lo que instalaremos:**1. Python 3.9+ (lenguaje de programación)2. Visual Studio Code (editor de código)3. Git (control de versiones)4. Extensiones de VS Code para Python5. GitHub Copilot (asistente IA)6. Herramientas de calidad de código---## 🐍 PASO 1: Instalación de Python### **Windows:**1. Ve a [python.org/downloads](https://python.org/downloads)2. Descarga **Python 3.11** (versión estable más reciente)3. **⚠️ IMPORTANTE**: Marca "Add Python to PATH" durante la instalación4. Ejecuta el instalador como **administrador**5. Verifica la instalación: `cmd   python --version   pip --version   `### **macOS:**`bash# Opción 1: Descarga desde python.org (recomendado para principiantes)# Ve a python.org/downloads y descarga el instalador# Opción 2: Usando Homebrew (si ya lo tienes)brew install python@3.11`### **Linux (Ubuntu/Debian):**`bash# Actualizar sistemasudo apt updatesudo apt upgrade# Instalar Python y pipsudo apt install python3.11 python3.11-pip python3.11-venv# Crear alias para facilitar usoecho 'alias python=python3.11' >> ~/.bashrcecho 'alias pip=pip3' >> ~/.bashrcsource ~/.bashrc`### ✅ **Verificación Python:**`bashpython --version  # Debe mostrar Python 3.11.xpip --version      # Debe mostrar pip con Python 3.11`---## 📝 PASO 2: Instalación de Visual Studio Code### **Todas las plataformas:**1. Ve a [code.visualstudio.com](https://code.visualstudio.com)2. Descarga la versión para tu sistema operativo3. Instala con configuración predeterminada4. Abre VS Code y verifica que funcione### **Configuración inicial recomendada:**1. **Tema**: File → Preferences → Color Theme → "Dark+ (default dark)"2. **Tamaño de fuente**: Settings → Font Size → 143. **Auto-guardado**: Settings → Auto Save → "afterDelay"---## 🔧 PASO 3: Instalación de Git### **Windows:**1. Descarga desde [git-scm.com](https://git-scm.com/download/win)2. Instala con opciones predeterminadas3. **⚠️ IMPORTANTE**: Selecciona "Git from the command line and also from 3rd-party software"### **macOS:**`bash# Opción 1: Descarga desde git-scm.com# Opción 2: Usando Homebrewbrew install git# Opción 3: Instalar Xcode Command Line Toolsxcode-select --install`### **Linux:**`bash# Ubuntu/Debiansudo apt install git# CentOS/RHELsudo yum install git`### ⚙️ **Configuración inicial de Git:**`bash# Configurar tu identidad (OBLIGATORIO)git config --global user.name "Tu Nombre Completo"git config --global user.email "tu.email@ejemplo.com"# Configuraciones adicionales recomendadasgit config --global init.defaultBranch maingit config --global core.autocrlf true  # Solo Windowsgit config --global core.autocrlf input  # macOS/Linux`### ✅ **Verificación Git:**`bashgit --versiongit config --list`---## 🔌 PASO 4: Instalación de Extensiones de VS Code### **Extensiones OBLIGATORIAS:**#### **1. Python Extension Pack**- Abre VS Code- Presiona `Ctrl+Shift+X` (Cmd+Shift+X en Mac)- Busca "Python Extension Pack"- Instala la extensión oficial de Microsoft#### **2. GitHub Copilot (Asistente IA)**- Busca "GitHub Copilot"- Instala la extensión oficial- **Nota**: Requiere suscripción de GitHub Pro/estudiante (gratuita para estudiantes)#### **3. Extensiones adicionales recomendadas:**`- Python Docstring Generator- Python Test Explorer- Git Graph- Auto Rename Tag- Bracket Pair Colorizer- Error Lens- Material Icon Theme`### **Configuración de Python en VS Code:**1. Abre VS Code2. Presiona `Ctrl+Shift+P` → "Python: Select Interpreter"3. Selecciona la versión de Python 3.11 que instalaste4. Crea un archivo test.py y escribe: `python   print("¡Hola, VS Code!")   `5. Presiona F5 para ejecutar---## 🐙 PASO 5: Configuración de GitHub### **Crear cuenta GitHub (si no tienes):**1. Ve a [github.com](https://github.com)2. Crea una cuenta gratuita3. Verifica tu email4. **Para estudiantes**: Solicita [GitHub Student Pack](https://education.github.com/pack) para beneficios adicionales### **Configuración de autenticación:**#### **Opción 1: GitHub CLI (recomendado)**`bash# Instalar GitHub CLI# Windows: Descarga desde cli.github.com# macOS: brew install gh# Linux: Consulta cli.github.com/manual/installation# Autenticarsegh auth login# Sigue las instrucciones interactivas`#### **Opción 2: SSH Keys (alternativo)**`bash# Generar nueva SSH keyssh-keygen -t ed25519 -C "tu.email@ejemplo.com"# Agregar a ssh-agenteval "$(ssh-agent -s)"ssh-add ~/.ssh/id_ed25519# Copiar clave públicacat ~/.ssh/id_ed25519.pub# Pega el contenido en GitHub → Settings → SSH Keys`### ✅ **Verificación GitHub:**`bashgh auth status# ossh -T git@github.com`---## 📦 PASO 6: Configuración del Entorno Virtual### **Crear entorno virtual del proyecto:**`bash# Navegar al directorio del cursocd python-junior-template# Crear entorno virtualpython -m venv .venv# Activar entorno virtual# Windows:.venv\Scripts\activate# macOS/Linux:source .venv/bin/activate# Verificar activación (debe aparecer (.venv) en el prompt)which python  # macOS/Linuxwhere python   # Windows`### **Instalar dependencias del curso:**`bash# Con el entorno virtual activadopip install --upgrade pippip install -r requirements.txt# Verificar instalaciónpip list`---## 🧪 PASO 7: Configuración de Herramientas de Calidad### **Instalar herramientas de testing y linting:**```bash# Estas ya están en requirements.txt, pero por separado serían:pip install pytest flake8 pylint black autopep8

````

### **Configurar VS Code para usar estas herramientas:**

#### **settings.json del workspace:**
Crea `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": ["."],
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
````

---

## 🤖 PASO 8: Configuración de GitHub Copilot

### **Activar GitHub Copilot:**

1. **Para estudiantes**:

   - Aplica a [GitHub Education](https://education.github.com/)
   - GitHub Copilot es gratuito para estudiantes verificados

2. **Suscripción regular**:
   - Ve a [github.com/features/copilot](https://github.com/features/copilot)
   - Suscríbete al plan mensual

### **Configuración en VS Code:**

1. Instala la extensión "GitHub Copilot"
2. Presiona `Ctrl+Shift+P` → "GitHub Copilot: Sign In"
3. Auténticate con tu cuenta GitHub
4. ✅ Deberías ver el ícono de Copilot en la barra de estado

### **Configuración recomendada de Copilot:**

```json
// Agregar a settings.json
{
  "github.copilot.enable": {
    "python": true,
    "plaintext": false,
    "markdown": true
  },
  "github.copilot.advanced": {
    "listCount": 5,
    "inlineSuggestCount": 3
  }
}
```

---

## ✅ PASO 9: Verificación Completa del Entorno

### **Script de verificación:**

Crea y ejecuta `verificar_entorno.py`:

```python
#!/usr/bin/env python3
"""
Script de verificación del entorno de desarrollo
Curso: Python Junior con IA
"""

import sys
import subprocess
import importlib

def verificar_python():
    """Verifica la versión de Python"""
    version = sys.version_info
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")

    if version.major == 3 and version.minor >= 9:
        print("   ✅ Versión de Python correcta")
        return True
    else:
        print("   ❌ Necesitas Python 3.9 o superior")
        return False

def verificar_paquetes():
    """Verifica que los paquetes estén instalados"""
    paquetes_requeridos = [
        'pytest', 'flake8', 'pylint', 'black',
        'requests', 'colorama', 'tabulate'
    ]

    todos_instalados = True

    for paquete in paquetes_requeridos:
        try:
            importlib.import_module(paquete)
            print(f"   ✅ {paquete} instalado")
        except ImportError:
            print(f"   ❌ {paquete} NO instalado")
            todos_instalados = False

    return todos_instalados

def verificar_git():
    """Verifica que Git esté configurado"""
    try:
        result = subprocess.run(['git', '--version'],
                              capture_output=True, text=True)
        print(f"✅ {result.stdout.strip()}")

        # Verificar configuración
        name = subprocess.run(['git', 'config', 'user.name'],
                            capture_output=True, text=True)
        email = subprocess.run(['git', 'config', 'user.email'],
                             capture_output=True, text=True)

        if name.stdout.strip() and email.stdout.strip():
            print(f"   ✅ Configurado como: {name.stdout.strip()} <{email.stdout.strip()}>")
            return True
        else:
            print("   ❌ Git no está configurado correctamente")
            return False

    except FileNotFoundError:
        print("❌ Git no está instalado")
        return False

def main():
    """Función principal de verificación"""
    print("🔍 VERIFICANDO ENTORNO DE DESARROLLO")
    print("=" * 50)

    verificaciones = [
        ("Python", verificar_python()),
        ("Paquetes Python", verificar_paquetes()),
        ("Git", verificar_git())
    ]

    print("\n📊 RESUMEN:")
    print("-" * 30)

    todas_correctas = True
    for nombre, resultado in verificaciones:
        status = "✅ OK" if resultado else "❌ ERROR"
        print(f"{nombre:.<20} {status}")
        if not resultado:
            todas_correctas = False

    print("\n" + "=" * 50)
    if todas_correctas:
        print("🎉 ¡ENTORNO CONFIGURADO CORRECTAMENTE!")
        print("🚀 ¡Estás listo para empezar el curso!")
    else:
        print("⚠️  Hay problemas que resolver antes de continuar")
        print("📖 Revisa las instrucciones de instalación")

if __name__ == "__main__":
    main()
```

### **Ejecutar verificación:**

```bash
python verificar_entorno.py
```

---

## 🎯 PASO 10: Configuración del Workspace del Curso

### **Clonar el repositorio del curso:**

```bash
# Si es tu primer día
git clone [URL-del-repositorio]
cd python-junior-template

# Crear tu rama personal
git checkout -b mi-progreso-[tu-nombre]
git push -u origin mi-progreso-[tu-nombre]
```

### **Estructura recomendada de carpetas:**

```
Documentos/
└── Cursos/
    └── Python-IA/
        ├── python-junior-template/  # Repositorio del curso
        ├── mis-proyectos/          # Tus experimentos personales
        └── recursos-extra/         # Materiales adicionales
```

### **Configurar VS Code Workspace:**

1. Abre VS Code
2. File → Open Workspace from File
3. Selecciona `python-junior-template.code-workspace`
4. ¡Todo debería estar configurado automáticamente!

---

## 🔧 Solución de Problemas Comunes

### **❌ Python no se reconoce en CMD/Terminal**

**Solución Windows:**

```cmd
# Agregar Python al PATH manualmente
# Panel de Control → Sistema → Variables de entorno
# Agregar: C:\Users\[usuario]\AppData\Local\Programs\Python\Python311\
```

### **❌ VS Code no encuentra el intérprete de Python**

**Solución:**

1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Si no aparece, clickea "Enter interpreter path..."
3. Navega a tu instalación de Python

### **❌ Error de permisos al instalar paquetes**

**Solución:**

```bash
# Usar --user flag
pip install --user nombre-paquete

# O ejecutar como administrador (Windows)
# Botón derecho en CMD → "Ejecutar como administrador"
```

### **❌ GitHub Copilot no funciona**

**Solución:**

1. Verifica tu suscripción en github.com/settings/copilot
2. Sign out y sign in nuevamente en VS Code
3. Reinicia VS Code completamente

### **❌ Git no reconoce comandos**

**Solución Windows:**

```cmd
# Agregar Git al PATH
# Agregar: C:\Program Files\Git\cmd
# Reiniciar CMD/PowerShell
```

---

## 📱 Aplicaciones Móviles Recomendadas

### **Para practicar en tu teléfono:**

- **Pydroid 3** (Android): Editor Python móvil
- **Pythonista** (iOS): IDE Python para iPad/iPhone
- **GitHub Mobile**: Para revisar código y hacer commits
- **Stack Overflow**: Para consultas rápidas

---

## 🎓 Próximos Pasos

### **Una vez que todo esté configurado:**

1. **✅ Ejecuta la verificación completa**

   ```bash
   python verificar_entorno.py
   ```

2. **📚 Lee la documentación principal**

   ```bash
   # Abre el README principal
   code README.md
   ```

3. **🚀 Dirígete a tu primera clase**

   ```bash
   cd modulo_1_fundamentos/clase_1_entorno_profesional/
   code README.md
   ```

4. **🎯 Únete a la comunidad**
   - Discord del curso: [Enlace de invitación]
   - Foro de estudiantes: [URL del foro]

---

## 🆘 Obtener Ayuda

### **Si tienes problemas:**

1. **📖 Consulta esta guía nuevamente** - muchos problemas se resuelven releyendo
2. **🔍 Busca en el foro** del curso - alguien más puede haber tenido el mismo problema
3. **💬 Pregunta en Discord** - la comunidad es muy colaborativa
4. **📧 Contacta al instructor** - como último recurso para problemas complejos

### **Información de contacto:**

- **Discord**: [Enlace del servidor]
- **Email**: soporte.curso@[institución]
- **Horas de oficina**: Martes y Jueves 18:00-19:00

---

## ✅ Checklist Final

Antes de continuar, verifica que tienes:

- [ ] **Python 3.9+** instalado y funcionando
- [ ] **VS Code** con extensiones de Python
- [ ] **Git** configurado con tu nombre y email
- [ ] **GitHub** account configurada
- [ ] **Entorno virtual** creado y activado
- [ ] **Dependencias** instaladas correctamente
- [ ] **GitHub Copilot** funcionando (si tienes acceso)
- [ ] **Script de verificación** ejecutado exitosamente
- [ ] **Repositorio del curso** clonado y configurado

---

**🎉 ¡Felicitaciones! Tu entorno está listo para empezar a programar con Python e IA.**

**🚀 ¡Dirígete ahora a tu primera clase: `modulo_1_fundamentos/clase_1_entorno_profesional/`!**

---

_💡 **Consejo de pro**: Guarda esta guía en tus marcadores - la vas a necesitar como referencia durante todo el curso._
