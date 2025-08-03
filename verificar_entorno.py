#!/usr/bin/env python3
"""Curso: Python Junior con IA.
Propósito: Verificar que todas las herramientas
"""

import sys
import subprocess
import importlib
from pathlib import Path


def print_header():
    """Imprime el encabezado informativo del verificador en consola."""
    print("=" * 60)
    print("🔍 VERIFICADOR DEL ENTORNO DE DESARROLLO")
    print("🐍 Curso: Python Junior con IA")
    print("=" * 60)
    print()


def print_section(title):
    """Imprime un título de sección con formato."""
    print(f"\n📋 {title}")
    print("-" * (len(title) + 4))


def check_python_version():
    """Verifica que Python esté instalado"""
    print_section("VERIFICANDO PYTHON")
    version = sys.version_info
    version_str = f"Python {version.major}.{version.minor}.{version.micro}"
    print(f"🐍 Versión instalada: {version_str}")
    if version.major == 3 and version.minor >= 9:
        print("✅ Versión de Python es correcta (3.9+")
        return True
    print("❌ Necesitas Python 3.9 o superior")
    print("💡 Descarga desde: https://python.org/downloads")
    return False


def check_pip():
    """Verifica si pip está instalado y funcionando correctamente."""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', '--version'],
            capture_output=True, text=True, timeout=10, check=False
        )
        if result.returncode == 0:
            print(f"📦 pip: {result.stdout.strip()}")
            return True
        print("❌ pip no está funcionando correctamente")
        return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("❌ pip no está instalado o no responde")
        return False


def check_required_packages():
    """Verifica que los paquetes requerid"""
    print_section("VERIFICANDO PAQUETES PYTHON")
    required_packages = [
        ('pytest', 'Framework de testing'),
        ('flake8', 'Linter de código'),
        ('pylint', 'Análisis estático'),
        ('black', 'Formateador de código'),
        ('colorama', 'Colores en terminal'),
        ('tabulate', 'Formateo de tablas'),
        ('requests', 'Cliente HTTP'),
    ]
    all_installed = True
    for package, description in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package:<12} - {description}")
        except ModuleNotFoundError:
            print(f"❌ {package:<12} - {description} (NO INSTALADO)")
            all_installed = False
    if not all_installed:
        print("\n💡 Para instalar paquetes faltantes:")
        print("   pip install -r requirements.txt")
    return all_installed


def check_git():
    """Verifica que Git esté correctamente"""
    print_section("VERIFICANDO GIT")
    try:
        result = subprocess.run(
            ['git', '--version'],
            capture_output=True, text=True, timeout=10, check=False
        )
        if result.returncode != 0:
            print("❌ Git no está instalado correctamente")
            return False
        print(f"📱 {result.stdout.strip()}")

        name_result = subprocess.run(
            ['git', 'config', 'user.name'],
            capture_output=True, text=True, timeout=5, check=False
        )
        email_result = subprocess.run(
            ['git', 'config', 'user.email'],
            capture_output=True, text=True, timeout=5, check=False
        )

        name = name_result.stdout.strip()
        email = email_result.stdout.strip()

        if name and email:
            print(f"✅ Configurado como: {name} <{email}>")
            return True

        print("❌ Git no está configurado con usuario y email")
        print("💡 Configura con:")
        print('   git config --global user.name "Tu Nombre"')
        print('   git config --global user.email "tu@email.com"')
        return False

    except subprocess.TimeoutExpired:
        print("⚠️ Git está instalado pero la configuración no responde")
        return False
    except FileNotFoundError:
        print("❌ Git no está instalado")
        print("💡 Descarga desde: https://git-scm.com")
        return False


def check_vscode():
    """Verifica si VS Code está instalado."""
    print_section("VERIFICANDO VISUAL STUDIO CODE")
    try:
        result = subprocess.run(
            ['code', '--version'],
            capture_output=True, text=True, timeout=10, check=False
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            print(f"💻 VS Code versión: {lines[0]}")
            print("✅ Visual Studio Code está instalado")
            return True
        print("❌ VS Code no responde correctamente")
        return False
    except FileNotFoundError:
        print("❌ VS Code no está instalado o no está en el PATH")
        print("💡 Descarga desde: https://code.visualstudio.com")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️ VS Code no responde (puede estar ocupado)")
        return False


def check_project_structure():
    """Verifica la presencia de archivos y carpet"""
    print_section("VERIFICANDO ESTRUCTURA DEL PROYECTO")
    current_dir = Path.cwd()
    required_files = [
        'README.md',
        'requirements.txt',
        'setup_instructions.md',
        '.gitignore'
    ]
    required_dirs = [
        'modulo_1_fundamentos',
        'recursos'
    ]
    all_present = True
    print("📁 Archivos esenciales:")
    for file in required_files:
        if (current_dir / file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (faltante)")
            all_present = False
    print("\n📁 Directorios del curso:")
    for directory in required_dirs:
        if (current_dir / directory).is_dir():
            print(f"✅ {directory}/")
        else:
            print(f"❌ {directory}/ (faltante)")
            all_present = False
    return all_present


def check_virtual_environment():
    """Detecta si se está ejecutando dentro de un entorno"""
    print_section("VERIFICANDO ENTORNO VIRTUAL")
    if hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    ):
        print("✅ Entorno virtual activo")
        print(f"📍 Ubicación: {sys.prefix}")
        return True
    print("⚠️ No se detectó entorno virtual activo")
    print("💡 Recomendación:")
    print("   python -m venv .venv")
    print("   .venv\\Scripts\\activate  # Windows")
    print("   source .venv/bin/activate  # macOS/Linux")
    return False


def run_basic_tests():
    """ de importaciones, escritu"""
    print_section("EJECUTANDO TESTS BÁSICOS")
    try:
        print("🧪 Probando importaciones básicas...")
        print("✅ Importaciones básicas funcionan")

        print("🧪 Probando escritura de archivos...")
        test_file = Path("test_write.tmp")
        try:
            test_file.write_text("test", encoding="utf-8")
            test_file.unlink()
            print("✅ Escritura de archivos funciona")
        except OSError:
            print("❌ No hay permisos de escritura en el directorio")
            return False

        print("🧪 Probando ejecución de Python...")
        result = subprocess.run(
            [sys.executable, '-c', 'print("Hello, World!")'],
            capture_output=True, text=True, timeout=5, check=False
        )
        if result.returncode == 0 and "Hello, World!" in result.stdout:
            print("✅ Ejecución de Python funciona")
        else:
            print("❌ Problema ejecutando Python")
            return False

        return True

    except (subprocess.SubprocessError, OSError) as e:
        print(f"❌ Error en tests básicos: {type(e).__name__} - {e}")
        return False


def generate_report(checks_results):
    """Genera un resumen final de resultados de las verificaciones."""
    print_section("REPORTE FINAL")
    total = len(checks_results)
    passed = sum(checks_results.values())
    print(f"📊 Verificaciones completadas: {passed}/{total}\n")
    for name, result in checks_results.items():
        status = "✅ BIEN" if result else "❌ PROBLEMA"
        print(f"{name:<25} {status}")
    print("\n" + "=" * 60)
    if passed == total:
        print("🎉 ¡EXCELENTE! Tu entorno está completamente configurado.")
        print("🚀 Estás listo para comenzar el curso de Python con IA.")
        print("\n🎯 Ir a modulo_1_fundamentos/clase_1_entorno_profesional/")
    elif passed >= total * 0.8:
        print("⚠️ Tu entorno está casi listo. Hay algunos problemas menores.")
        print("🔧 Revisa los elementos marcados con ❌ y corrígelos.")
    else:
        print("🚨 Tu entorno necesita configuración adicional.")
        print("📖 Consulta setup_instructions.md para una guía completa.")
    print("\n💡 Puedes ejecutar este script las veces que necesites.")
    print("   python verificar_entorno.py")


def main():
    """Función que ejecuta las verificaciones"""
    print_header()
    checks = {
        "Python 3.9+": check_python_version(),
        "pip funcionando": check_pip(),
        "Paquetes requeridos": check_required_packages(),
        "Git configurado": check_git(),
        "VS Code instalado": check_vscode(),
        "Estructura proyecto": check_project_structure(),
        "Entorno virtual": check_virtual_environment(),
        "Tests básicos": run_basic_tests(),
    }
    generate_report(checks)
    print("\n📞 RECURSOS DE AYUDA:")
    print("📖 Documentación: README.md")
    print("⚙️ Configuración: setup_instructions.md")
    print("💬 Discord: [Enlace del curso]")
    print("📧 Email: soporte.curso@[institución]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Verificación interrumpida por el usuario.")
        print("💡 Puedes ejecutar el script nuevamente cuando quieras.")
    except RuntimeError as e:
        print(f"\n❌ Error inesperado: {type(e).__name__} - {e}")
        print("🆘 Si este error persiste, contacta al soporte del curso.")
        sys.exit(1)
