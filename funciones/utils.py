
from config import COSTO_MODELOS, TOKENS_POR_BLOQUE
from funciones.parser import separar_bloques

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
