from scripts import script01_preparar as script01

def main():
    with open("temario/temario.txt", "r", encoding="utf-8") as f:
        temario = f.read()

    bloques_informacion = script01.main(temario)

    with open("archivo_salida.txt", "w", encoding="utf-8") as f:

        f.write(bloques_informacion)
        

    print(f"Archivo normalizado guardado en: archivo_salida.txt")

if __name__ == "__main__":
    main()
