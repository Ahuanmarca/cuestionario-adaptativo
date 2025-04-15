# test_funciones.py
from funciones.parser import extraer_fragmento
from funciones.parser import actualizar_valor

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
