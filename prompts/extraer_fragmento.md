Crea una funcion llamada extraer_fragmento
La funcion acepta dos argumentos:
* un texto de varias lineas
* un string, que usara para buscar la parte que necesita extraer y retornar

supongamos que...

texto = """
_Libro
Condiciones Generales
_CAPITULO
Título de transporte
_INFORMACION
El título de transporte es el contrato entre la empresa y el viajero.
"""

si hacemos

foo = extraer_fragmento(texto, "_CAPITULO")

entinces deberia ser cierto que:

foo == "Título de transporte"

Si hacemos

bar = extraer_fragmento(texto, "_INFORMACION")

deberia ser cierto que:

bar == "El título de transporte es el contrato entre la empresa y el viajero."



