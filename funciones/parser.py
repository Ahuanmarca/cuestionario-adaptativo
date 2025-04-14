# funciones/parser.py

# import re
from typing import List


def separar_bloques(texto: str, delimitador: str) -> List[str]:
    """
    Separa un texto en bloques usando un delimitador como marcador de inicio.

    Args:
        texto (str): Texto completo a separar.
        delimitador (str): Línea que indica el inicio de un nuevo bloque.

    Returns:
        List[str]: Lista de bloques de texto, cada uno incluyendo su delimitador.
    """
    lineas = texto.splitlines()
    bloques = []
    bloque_actual = []

    for linea in lineas:
        if linea.strip().startswith(delimitador):
            if bloque_actual:
                bloques.append("\n".join(bloque_actual).strip())
                bloque_actual = []
        if bloque_actual or linea.strip().startswith(delimitador):
            bloque_actual.append(linea)

    if bloque_actual:
        bloques.append("\n".join(bloque_actual).strip())

    return bloques


def obtener_informacion(texto: str) -> str:
    """
    Extrae el contenido que aparece debajo de la etiqueta _INFORMACION,
    hasta la próxima línea que empiece con "_" o hasta el final del texto.

    No incluye la línea "_INFORMACION" en el resultado.
    """
    lineas = texto.splitlines()
    capturando = False
    contenido = []

    for linea in lineas:
        if linea.strip() == "_INFORMACION":
            capturando = True
            continue
        if capturando:
            if linea.strip().startswith("_"):
                break
            contenido.append(linea)

    return "\n".join(contenido).strip()
