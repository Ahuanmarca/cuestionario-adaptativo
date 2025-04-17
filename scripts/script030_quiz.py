import random
from funciones.parser import separar_bloques, extraer_fragmento

def main():
    ruta = "temario/salida.txt"

    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

    bloques = separar_bloques(contenido, "_PREGUNTA")
    random.shuffle(bloques)

    seleccionadas = bloques[:60]
    puntaje = 0

    for idx, bloque in enumerate(seleccionadas, 1):
        pregunta = extraer_fragmento(bloque, "_PREGUNTA")
        correcta = extraer_fragmento(bloque, "_RESPUESTA_CORRECTA")
        falsas = extraer_fragmento(bloque, "_RESPUESTAS_FALSAS").splitlines()

        opciones = falsas + [correcta]
        opciones = [o.strip() for o in opciones if o.strip()]
        random.shuffle(opciones)

        print(f"\nPregunta {idx}: {pregunta}\n")
        for i, opcion in enumerate(opciones, 1):
            print(f"  {i}. {opcion}")

        try:
            eleccion = int(input("\nTu respuesta (1-4): "))
            seleccionada = opciones[eleccion - 1]
        except (ValueError, IndexError):
            print("❌ Respuesta inválida. Se contará como incorrecta.")
            continue

        if seleccionada == correcta:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta era: {correcta}")

    print(f"\nTu puntaje final: {puntaje} / 60")
