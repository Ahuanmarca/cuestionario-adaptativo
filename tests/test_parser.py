from funciones import parser


def test_separar_bloques():
    texto = """_LIBRO
Uno
_LIBRO
Dos
_LIBRO
Tres"""
    bloques = parser.separar_bloques(texto, "_LIBRO")
    assert len(bloques) == 3
    assert bloques[0] == "_LIBRO\nUno"
    assert bloques[1] == "_LIBRO\nDos"
    assert bloques[2] == "_LIBRO\nTres"


def test_extraer_fragmento():
    texto = """_LIBRO
Condiciones Generales
_CAPITULO
Título de transporte
_INFORMACION
Esto es info.
Segunda línea de info.
_PREGUNTA
¿Qué es esto?"""

    assert parser.extraer_fragmento(texto, "_LIBRO") == "Condiciones Generales"
    assert parser.extraer_fragmento(texto, "_CAPITULO") == "Título de transporte"
    assert parser.extraer_fragmento(texto, "_INFORMACION") == "Esto es info.\nSegunda línea de info."
    assert parser.extraer_fragmento(texto, "_PREGUNTA") == "¿Qué es esto?"


def test_actualizar_valor_linea():
    texto = """_LIBRO
Condiciones Generales
_COBERTURA
0"""
    actualizado = parser.actualizar_valor(texto, "_COBERTURA", "85")
    assert "_COBERTURA\n85" in actualizado
    assert "0" not in actualizado


def test_actualizar_valor_multilinea():
    texto = """_INFORMACION
Texto viejo línea 1.
Texto viejo línea 2.
_PREGUNTA
¿Qué es esto?"""
    nuevo_valor = "Texto NUEVO línea 1.\nTexto NUEVO línea 2."
    actualizado = parser.actualizar_valor(texto, "_INFORMACION", nuevo_valor)
    assert nuevo_valor in actualizado
    assert "Texto viejo" not in actualizado
