from config import ARCHIVO_ENTRADA, ARCHIVO_SALIDA
from scripts import script010_preparar as script01
from scripts import script020_generar_preguntas as script02

def main():
    with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as f:
        temario = f.read()

    bloques_informacion = script01.main(temario)
    bloques_con_preguntas = script02.main(bloques_informacion)

    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:

        f.write(bloques_con_preguntas)

    print(f"Archivo normalizado guardado en: {ARCHIVO_SALIDA}")

if __name__ == "__main__":
    main()
