
from config import COSTO_MODELOS, TOKENS_POR_BLOQUE
from funciones.parser import separar_bloques
import re

# TODO: Hacer esta función más reutilizable.
# Actualmente funciona únicamente para separar bloques por "_LIBRO", con una única lógica.
def estimar_costo(texto: str, modelo: str = None) -> bool:
    """
    Estima el costo de generar preguntas con el modelo seleccionado.
    Pregunta al usuario si desea continuar. Retorna True si sí, False si no.
    """

    if modelo is None:
        print(f"estimar_costo: No se ha seleccionado modelo.")
        return False

    if modelo not in COSTO_MODELOS:
        print(f"estimar_costo: No tenemos el precio del modelo seleccionado.")
        return False

    # Mapa de precios por 1000 tokens de entrada (puedes ajustarlo con base en OpenAI)
    costo_por_1k_tokens = COSTO_MODELOS

    bloques = separar_bloques(texto, "_LIBRO")
    num_bloques = len(bloques)
    tokens_estimados_por_bloque = TOKENS_POR_BLOQUE  # Ajustable según tu experiencia
    tokens_totales = num_bloques * tokens_estimados_por_bloque

    costo_modelo = costo_por_1k_tokens.get(modelo, 0.005)
    costo_estimado = (tokens_totales / 1000) * costo_modelo # ¿Es 1000 porque son 1000 tokens estimados por bloque?

    print(f"📦 Modelo: {modelo}")
    print(f"📄 Número de bloques: {num_bloques}")
    print(f"🧮 Tokens estimados por bloque: {tokens_estimados_por_bloque}")
    print(f"💰 Costo total estimado: ~${costo_estimado:.4f}")

    continuar = input("¿Deseas continuar? (s/n): ").strip().lower()
    return continuar == "s" or continuar == "y"


def validar_pregunta(texto: str) -> bool:
    """
    Verifica si un bloque de texto cumple con la estructura esperada:
    _PREGUNTA seguido de 1 línea
    _RESPUESTA_CORRECTA seguido de 1 línea
    _RESPUESTAS_FALSAS seguido de 3 líneas (no vacías)
    _COBERTURA seguido de 1 número entre 0 y 100
    """
    # Limpiar saltos vacíos al inicio y al final
    lineas = texto.strip().splitlines()

    # Eliminar líneas vacías intermedias
    lineas = [linea.strip() for linea in lineas if linea.strip() != ""]

    i = 0
    try:
        # _PREGUNTA
        if lineas[i] != "_PREGUNTA":
            return False
        i += 1
        if i >= len(lineas) or lineas[i].startswith("_"):
            return False
        i += 1

        # _RESPUESTA_CORRECTA
        if lineas[i] != "_RESPUESTA_CORRECTA":
            return False
        i += 1
        if i >= len(lineas) or lineas[i].startswith("_"):
            return False
        i += 1

        # _RESPUESTAS_FALSAS
        if lineas[i] != "_RESPUESTAS_FALSAS":
            return False
        i += 1

        falsas = []
        while i < len(lineas) and not lineas[i].startswith("_") and len(falsas) < 3:
            if lineas[i].strip() != "":
                falsas.append(lineas[i])
            i += 1
        if len(falsas) != 3:
            return False

        # _COBERTURA
        if i >= len(lineas) or lineas[i] != "_COBERTURA":
            return False
        i += 1
        if i >= len(lineas):
            return False
        cobertura = lineas[i]
        if not re.fullmatch(r"\d{1,3}", cobertura):
            return False
        cobertura_num = int(cobertura)
        if not (0 <= cobertura_num <= 100):
            return False

        return True
    except IndexError:
        return False
