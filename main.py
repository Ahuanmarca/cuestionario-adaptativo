from scripts import script010_preparar as script01

def main():
    with open("temario/mini.txt", "r", encoding="utf-8") as f:
        temario = f.read()

    bloques_informacion = script01.main(temario)

    with open("mini_salida.txt", "w", encoding="utf-8") as f:

        f.write(bloques_informacion)
        

    print(f"Archivo normalizado guardado en: mini_salida.txt")

if __name__ == "__main__":
    main()
