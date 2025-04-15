from funciones.parser import separar_bloques
from funciones.parser import extraer_fragmento
from funciones.parser import actualizar_valor
from funciones.gpt_calls import generar_pregunta


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

    salida_arr = []
    bloques_informacion = separar_bloques(texto, "_LIBRO")
    for bloque in bloques_informacion:
        informacion = extraer_fragmento(bloque, "_INFORMACION")
        pregunta_generada = generar_pregunta(informacion)

        pregunta = extraer_fragmento(pregunta_generada, "_PREGUNTA")
        respuesta_correcta = extraer_fragmento(pregunta_generada, "_RESPUESTA_CORRECTA")
        respuestas_falsas = extraer_fragmento(pregunta_generada, "_RESPUESTAS_FALSAS")
        cobertura = extraer_fragmento(pregunta_generada, "_COBERTURA")

        estructura = generar_estructura(pregunta, respuesta_correcta, respuestas_falsas)
        bloque_actualizado = actualizar_valor(bloque, "_COBERTURA", cobertura)

        salida_arr.append(bloque_actualizado + "\n\n" + estructura)

    salida = "\n\n".join(salida_arr)
    return salida


if __name__ == "__main__":
    print("Ejecutar desde main.py")
