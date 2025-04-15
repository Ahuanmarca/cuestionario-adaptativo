# funciones/parser.py

import re
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


def extraer_fragmento(texto: str, delimitador: str) -> str:
    """
    Extrae el contenido que aparece debajo de un delimitador,
    hasta la próxima línea que empiece con "_" o hasta el final del texto.

    No incluye la línea con el delimitador en el resultado.

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
        if linea.strip() == delimitador:
            capturando = True
            continue
        if capturando:
            if linea.strip().startswith("_"):
                break
            contenido.append(linea)

    return "\n".join(contenido).strip()

def actualizar_valor(texto: str, etiqueta: str, nuevo_valor: str) -> str:
    """
    Reemplaza el valor asociado a una etiqueta específica en un texto multilínea.
    La etiqueta debe estar sola en una línea, y el valor asociado son las líneas
    que siguen hasta la próxima etiqueta (otra línea que comience con "_").

    Args:
        texto (str): Texto estructurado con etiquetas tipo "_ETIQUETA\nvalor".
        etiqueta (str): La etiqueta que se desea actualizar (ej. "_COBERTURA").
        nuevo_valor (str): El nuevo valor que se insertará debajo de la etiqueta.

    Returns:
        str: El texto con el valor reemplazado.
    """
    lineas = texto.splitlines()
    resultado = []
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        resultado.append(linea)

        if linea.strip() == etiqueta:
            i += 1  # saltar a la línea siguiente, que será reemplazada
            # eliminar todas las líneas del valor actual
            while i < len(lineas) and not lineas[i].startswith("_"):
                i += 1
            # insertar el nuevo valor (puede ser multilínea)
            resultado.extend(nuevo_valor.splitlines())
            continue

        i += 1

    return "\n".join(resultado)
