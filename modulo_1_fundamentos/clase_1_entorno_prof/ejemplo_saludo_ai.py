#!/usr/bin/env python3
"""Saludo Personalizado Inteligente.

Python Junior con IA - Clase 1
Primer programa Python profesional
"""


def solicitar_nombre():
    """Solicita el nombre del usuario con validación básica."""
    while True:
        nombre = input("¿Cuál es tu nombre? ").strip()
        # Validación básica
        if not nombre:
            print("❌ El nombre no puede estar vacío. Inténtalo de nuevo.")
            continue
        if len(nombre) < 2:
            print("❌ El nombre debe tener al menos 2 caracteres.")
            continue
        if not nombre.replace(" ", "").isalpha():
            print("❌ El nombre solo puede contener letras y espacios.")
            continue
        return nombre.title()  # Capitalizar nombre


def solicitar_edad():
    """Solicita la edad del usuario con validación."""
    while True:
        try:
            edad_input = input("🎂 ¿Cuántos años tienes? ")
            edad = int(edad_input)
            if edad <= 0:
                print("❌ La edad debe ser un número positivo.")
                continue
            if edad > 120:
                print("❌ ¡Esa edad parece muy alta! Verifica el número.")
                continue
            return edad
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")


def generar_saludo_perso(nombre, edad):
    """Genera un saludo personalizado basado en nombre y edad."""
    # Determinar categoría por edad
    if edad < 13:
        categoria = "joven programador"
        emoji = "🌟"
    elif edad < 18:
        categoria = "futuro developer"
        emoji = "🚀"
    elif edad < 30:
        categoria = "programador en crecimiento"
        emoji = "💻"
    else:
        categoria = "programador experimentado"
        emoji = "🧙‍♂️"
    saludo = f"""{emoji} ¡Hola, {nombre}! {emoji}
    🎯 A los {edad} años, eres un {categoria}.
    Tip del día: La curiosidad"""
    return saludo


def main():
    """Función principal del programa."""
    print("=" * 50)
    print("🐍 PROGRAMA: SALUDO PERSONALIZADO INTELIGENTE")
    print("=" * 50)
    try:
        # Solicitar datos del usuario
        nombre = solicitar_nombre()
        edad = solicitar_edad()
        # Generar y mostrar saludo
        saludo = generar_saludo_perso(nombre, edad)
        print(saludo)
        # Mensaje de despedida
        print("🎉 ¡Programa ejecutado exitosamente!")
        print("📚 Continúa con los siguientes ejercicios.")
    except KeyboardInterrupt:
        print("\n\n👋 ¡Programa interrumpido por el usuario!")
        print("💡 Tip: Usa Ctrl+C para salir de programas en ejecución.")
    except RuntimeError as error:
        print(f"\n❌ Error inesperado: {error}")
        print("🤖 Usa este error para preguntar a la IA cómo solucionarlo.")


# Ejecutar programa solo si se ejecuta directamente
if __name__ == "__main__":
    main()
