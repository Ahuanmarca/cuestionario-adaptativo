# test_funciones.py
from funciones.parser import extraer_fragmento
from funciones.parser import actualizar_valor
from funciones.utils import validar_pregunta

texto = """_LIBRO
Condiciones Generales
_CAPITULO
Título Preliminar
_INFORMACION
* hello, world
* i took cs50
_PREGUNTA
¿Who took cs50?"""

fragmento = extraer_fragmento(texto, "_INFORMACION")
valor_actualizado = actualizar_valor(texto, "_INFORMACION", "Esta información fue editada.")

print("\n")
print("==== texto original ===")
print(texto)
print("\n")
print("==== extraer_fragmento(texto, '_INFORMACION') ===")
print(fragmento)
print("\n")
print("==== actualizar_valor(texto, '_INFORMACION', 'Esta información fue editada.') ===")
print(valor_actualizado)
print("====")
print("\n")

pregunta_buena_1 = """_PREGUNTA
¿Cuál es la capital de Perú?
_RESPUESTA_CORRECTA
Lima.
_RESPUESTAS_FALSAS
Santiago.
Bogotá.
Buenos Aires.
_COBERTURA
80"""

pregunta_buena_2 = """

_PREGUNTA
¿Cuál es la capital de Perú?
_RESPUESTA_CORRECTA
Lima.
_RESPUESTAS_FALSAS
Santiago.

Bogotá.
Buenos Aires.
_COBERTURA

80

"""

pregunta_mala_1 = """_PREGUNTA
¿Cuál es la capital de Perú?
_RESPUESTA_CORRECTA
Lima.
_RESPUESTAS_FALSAS
Santiago.

Buenos Aires.
_COBERTURA
80"""

pregunta_mala_2 = """_PREGUNTA
_RESPUESTA_CORRECTA
Lima.
_RESPUESTAS_FALSAS
Santiago.
Arequipa.
Buenos Aires.
_COBERTURA
80"""

print("=== validar_pregunta ===")
print("Debe salir True:", validar_pregunta(pregunta_buena_1))
print("Debe salir True:", validar_pregunta(pregunta_buena_2))
print("Debe salir False:", validar_pregunta(pregunta_mala_1))
print("Debe salir False:", validar_pregunta(pregunta_mala_2))
