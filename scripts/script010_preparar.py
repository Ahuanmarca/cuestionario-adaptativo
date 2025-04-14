"""
PSEUDOCODE
array libros[] = separar_bloques(texto, "_LIBRO")
array salida_arr[] = []
for libro in libros[]:
    array capitulos[] = separar_bloques(libro, "_CAPITULO")
    for capitulo in capitulos[]:
        array bloques_informacion[] = separar_bloques(capitulo, "_INFORMACION")
        for bloque in bloques_informacion[]
            estructura = generar_estructura(libro, capitulo, bloque)
            append estructura generada a salida_arr[]
salida = join salida_arr[]
retornar salida
"""

# scripts/script01_preparar.py

from funciones.parser import separar_bloques


def generar_estructura(libro: str, capitulo: str, bloque: str) -> str:

    estructura = f"""_LIBRO
{libro}
_CAPITULO
{capitulo}
_ETIQUETAS
[]
_COBERTURA
0
{bloque}"""

    return estructura


def main(texto: str) -> str:

    bloques_libros = separar_bloques(texto, "_LIBRO")
    salida_arr = []

    for libro in bloques_libros:
        bloques_capitulos = separar_bloques(libro, "_CAPITULO")
        for capitulo in bloques_capitulos:
            bloques_info = separar_bloques(capitulo, "_INFORMACION")
            for bloque in bloques_info:
                titulo_libro = libro.splitlines()[1]
                titulo_capitulo = capitulo.splitlines()[1]
                estructura = generar_estructura(titulo_libro, titulo_capitulo, bloque)
                salida_arr.append(estructura)

    salida = "\n\n".join(salida_arr)
    return salida


if __name__ == "__main__":
    print("Ejecutar desde main.py")
