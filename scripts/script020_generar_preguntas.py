from config import MODELO_ACTUAL
from tqdm import tqdm
from funciones.parser import separar_bloques, extraer_fragmento, actualizar_valor
from funciones.gpt_calls import generar_pregunta
from funciones.utils import estimar_costo, validar_pregunta


def generar_estructura(pregunta: str, respuesta: str, falsas: str) -> str:
    estructura = f"""_PREGUNTA
{pregunta}
_RESPUESTA_CORRECTA
{respuesta}
_RESPUESTAS_FALSAS
{falsas}
_DESCARTADA
[]
_ACIERTOS_CONSECUTIVOS
0
_REFORMULADA
False"""

    return estructura


def main(texto: str) -> str:

    if not estimar_costo(texto, modelo=MODELO_ACTUAL):
        print("Operación cancelada.")
        return "=== ⛔ Llamada a GPT cancelada ==="

    salida_arr = []
    bloques_informacion = separar_bloques(texto, "_LIBRO")
    for bloque in tqdm(bloques_informacion, desc="Generando preguntas", unit="bloque"):
        informacion = extraer_fragmento(bloque, "_INFORMACION")
        pregunta_generada = generar_pregunta(informacion, MODELO_ACTUAL)

        pregunta = extraer_fragmento(pregunta_generada, "_PREGUNTA")
        respuesta_correcta = extraer_fragmento(pregunta_generada, "_RESPUESTA_CORRECTA")
        respuestas_falsas = extraer_fragmento(pregunta_generada, "_RESPUESTAS_FALSAS")
        cobertura = extraer_fragmento(pregunta_generada, "_COBERTURA")

        estructura = generar_estructura(pregunta, respuesta_correcta, respuestas_falsas)
        bloque_actualizado = actualizar_valor(bloque, "_COBERTURA", cobertura)

        if validar_pregunta(pregunta_generada):
            salida_arr.append(bloque_actualizado + "\n\n" + estructura)
        else:
            advertencia = "=== TO FIX: Pregunta generada ==="
            salida_arr.append(bloque_actualizado + "\n\n" + advertencia + "\n\n" + estructura)

    salida = "\n\n".join(salida_arr)
    return salida


if __name__ == "__main__":
    print("Ejecutar desde main.py")
