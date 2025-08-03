"""Tests for the intelligent greeting example.
This module contains tests for the `generar_saludo_personalizado` function,
which generates personalized greetings based on user input.
"""
import pytest
from modulo_1_fundamentos.clase_1_entorno_profesional.ejemplo_saludo_inteligente import (
    generar_saludo_personalizado,
)

@pytest.mark.parametrize(
    "nombre, edad, categoria, emoji",
    [
        ("Ana", 10, "joven programador", "🌟"),
        ("Luis", 15, "futuro developer", "🚀"),
        ("Sofia", 25, "programador en crecimiento", "💻"),
        ("Carlos", 40, "programador experimentado", "🧙‍♂️"),
    ]
)
def test_saludo_parametrizado(nombre, edad, categoria, emoji):
    """
    Test parametrizado para todas las categorías de saludo.
    """
    saludo = generar_saludo_personalizado(nombre, edad)
    assert categoria in saludo
    assert emoji in saludo
    assert nombre in saludo


def test_saludo_contiene_tip_del_dia():
    """
    Verifica que el saludo contiene el tip del día.
    """
    saludo = generar_saludo_personalizado("Test", 20)
    assert "Tip del día" in saludo
