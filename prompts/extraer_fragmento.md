# PROMPT PARA GPT

---

Crea una funcion llamada extraer_fragmento

La funcion acepta dos argumentos:
* un texto de varias lineas
* un string, que usa para buscar la parte que necesita extraer y retornar

si tenemos:

texto = """_Libro
Condiciones Generales
_CAPITULO
Título de transporte
_INFORMACION
El título de transporte es el contrato entre la empresa y el viajero.
Este documento faculta al viajero para utilizar el servicio.
_PREGUNTA
¿Qué es el título de transporte?"""

foo = extraer_fragmento(texto, "_CAPITULO")

foo == "Título de transporte"

bar = extraer_fragmento(texto, "_INFORMACION")

bar == """El título de transporte es el contrato entre la empresa y el viajero.
Este documento faculta al viajero para utilizar el servicio."""

baz = extraer_fragmento(texto, "_PREGUNTA")

baz == "¿Qué es el título de transporte?"

---

# RESPUESTA DE GPT

``` py
def extraer_fragmento(texto: str, etiqueta: str) -> str:
    """
    Extrae el contenido debajo de una etiqueta (como _INFORMACION, _CAPITULO, etc.),
    hasta encontrar otra línea que comience con "_" o el final del texto.

    Args:
        texto (str): Texto multilínea.
        etiqueta (str): La etiqueta a buscar.

    Returns:
        str: Contenido debajo de la etiqueta (sin incluir la etiqueta).
    """
    lineas = texto.splitlines()
    capturando = False
    contenido = []

    for linea in lineas:
        if linea.strip() == etiqueta:
            capturando = True
            continue
        if capturando:
            if linea.strip().startswith("_"):
                break
            contenido.append(linea)

    return "\n".join(contenido).strip()

```
