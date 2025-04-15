# PROMPT PARA GPT

Crea una función llamada actualizar_valor

La función recibe 3 argumentos:
* string con múltiples líneas, con estructura detallada más abajo
* string con etiqueta que servirá para encontrar un valor en el string anterior
* string con un valor nuevo, que servirá para reemplazar el valor anteior

Suponiendo que tenemos este texto (considéralo también como ejemplo de estructura):

```py
texto = """_LIBRO
Condiciones Generales
_CAPITULO
Servicios de Transporte Ferroviario
_ETIQUETAS
[]
_COBERTURA
0
_INFORMACION
Renfe Viajeros tiene por objeto social:
* La prestación de servicios de transporte de viajeros por ferrocarril, tanto nacional como internacional.
* La mediación en la prestación de cualesquiera servicios turísticos.
* La organización, oferta y/o comercialización de viajes combinados o productos turísticos.
* La prestación de otros servicios o actividades complementarias o vinculadas al transporte ferroviario."""
```

El texto funciona como una especie de diccionario, con keys y values.

## Ejemplos de uso:

Al ejecutar (para reemplazar el value de _COBERTURA):

``` py
texto_actualizado = actualizar_valor(texto, "_COBERTURA", "75")
```

El resultado debería ser:

``` py
texto_actualizado == """_LIBRO
Condiciones Generales
_CAPITULO
Servicios de Transporte Ferroviario
_ETIQUETAS
[]
_COBERTURA
75
_INFORMACION
Renfe Viajeros tiene por objeto social:
* La prestación de servicios de transporte de viajeros por ferrocarril, tanto nacional como internacional.
* La mediación en la prestación de cualesquiera servicios turísticos.
* La organización, oferta y/o comercialización de viajes combinados o productos turísticos.
* La prestación de otros servicios o actividades complementarias o vinculadas al transporte ferroviario."""
```

Como puedes ver, nada más ha cambiado en el texto.

Al ejecutar (para cambiar el valor de _INFORMACION):

``` py
nueva_info = """hello, world
i took cs50... a long time ago"""

foo = actualizar_valor(texto, "_INFORMACION", nueva_info)
```

El resultado debería ser:

``` py
foo == """_LIBRO
Condiciones Generales
_CAPITULO
Servicios de Transporte Ferroviario
_ETIQUETAS
[]
_COBERTURA
0
_INFORMACION
hello, world
i took cs50... a long time ago"""
```

# RESPUESTA DE GPT

``` py
def actualizar_valor(texto: str, etiqueta: str, nuevo_valor: str) -> str:
    """
    Reemplaza el valor asociado a una etiqueta específica en un texto multilínea.
    La etiqueta debe estar sola en una línea, y el valor asociado son las líneas
    que siguen hasta la próxima etiqueta (otra línea que comience con "_").

    Args:
        texto (str): Texto estructurado con etiquetas tipo "_ETIQUETA\nvalor".
        etiqueta (str): La etiqueta que se desea actualizar (ej. "_COBERTURA").
        nuevo_valor (str): El nuevo valor que se insertará debajo de la etiqueta.

    Returns:
        str: El texto con el valor reemplazado.
    """
    lineas = texto.splitlines()
    resultado = []
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        resultado.append(linea)

        if linea.strip() == etiqueta:
            i += 1  # saltar a la línea siguiente, que será reemplazada
            # eliminar todas las líneas del valor actual
            while i < len(lineas) and not lineas[i].startswith("_"):
                i += 1
            # insertar el nuevo valor (puede ser multilínea)
            resultado.extend(nuevo_valor.splitlines())
            continue

        i += 1

    return "\n".join(resultado)

```
