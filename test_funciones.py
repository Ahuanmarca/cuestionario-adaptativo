# test_funciones.py
from funciones.parser import obtener_informacion

bloque_ejemplo = """
_LIBRO
Condiciones Generales
_CAPITULO
Título Preliminar
_INFORMACION
* hello, word
* i took cs50
"""

info_extraida = obtener_informacion(bloque_ejemplo)

print("RESULTADO:")
print("==========")
print(info_extraida)
print("==========")
