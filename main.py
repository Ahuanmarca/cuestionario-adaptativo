import argparse
from config import ARCHIVO_ENTRADA, ARCHIVO_SALIDA
from scripts import script010_preparar as script01
from scripts import script020_generar_preguntas as script02
from scripts import script030_quiz


def main():
    parser = argparse.ArgumentParser(
        description="Aplicación de cuestionario adaptativo"
    )
    parser.add_argument(
        "accion", choices=["preparar", "generar"], help="Acción a ejecutar"
    )
    args = parser.parse_args()

    if args.accion == "quiz":
        script030_quiz.main()
    elif args.accion == "generar":
        with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as f:
            temario = f.read()

        bloques_informacion = script01.main(temario)
        bloques_con_preguntas = script02.main(bloques_informacion)

        with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:

            f.write(bloques_con_preguntas)

        print(f"Archivo normalizado guardado en: {ARCHIVO_SALIDA}")
    else:
        print("Uso: python3 main.py generar || quiz")


if __name__ == "__main__":
    main()
