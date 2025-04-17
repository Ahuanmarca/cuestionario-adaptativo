# PROMPT PARA GPT

Por favor genera una función de Python que compruebe si un string cumple con tener la siguiente estructura:

```
"""_PREGUNTA
... <-- Una línea de texto.
_RESPUESTA_CORRECTA
... <-- Una línea de texto.
_RESPUESTAS_FALSAS
... <-- Una línea de texto.
... <-- Una línea de texto.
... <-- Una línea de texto.
_COBERTURA
... <-- Una línea, que debe ser un número entre 0 y 100"""
```

A _PREGUNTA siempre debe seguir una línea de texto.
A _RESPUESTA_CORRECTA siempre debe seguir una línea de texto.
A _RESPUESTAS_FALSAS siempre deben seguir TRES líneas de texto.
A _COBERTURA siempre debe seguir una línea de texto, que debe contener únicamente un número entre 0 y 100,

Las líneas vacías deben ser ignoradas, lo cual haría que lo siguiente sea válido.

```
"""_PREGUNTA
... <-- Una línea de texto.
_RESPUESTA_CORRECTA
... <-- Una línea de texto.

_RESPUESTAS_FALSAS
... <-- Una línea de texto.

... <-- Una línea de texto.
... <-- Una línea de texto.
_COBERTURA
... <-- Una línea, que debe ser un número entre 0 y 100"""
```

Saltos de línea al inicio y al final también se deben ignorar cuando estén presentes.
Por lo tanto, esto también sería válido:

```
"""

_PREGUNTA
... <-- Una línea de texto.
_RESPUESTA_CORRECTA
... <-- Una línea de texto.
_RESPUESTAS_FALSAS
... <-- Una línea de texto.

... <-- Una línea de texto.
... <-- Una línea de texto.
_COBERTURA
... <-- Una línea, que debe ser un número entre 0 y 100

"""
```

Esto sería inválido porque sólo hay dos líneas de texto bajo _RESPUESTAS_FALSAS:

```
"""_PREGUNTA
... <-- Una línea de texto.
_RESPUESTA_CORRECTA
... <-- Una línea de texto.
_RESPUESTAS_FALSAS
... <-- Una línea de texto.
... <-- Una línea de texto.
_COBERTURA
... <-- Una línea, que debe ser un número entre 0 y 100"""
```

Esto sería inválido porque, si bien hay tres líneas bajo _RESPUESTAS_FALSAS, una de ellas es una línea vacía, la cual debe ser ignorada por la función.

```
"""_PREGUNTA
... <-- Una línea de texto.
_RESPUESTA_CORRECTA
... <-- Una línea de texto.
_RESPUESTAS_FALSAS
... <-- Una línea de texto.

... <-- Una línea de texto.
_COBERTURA
... <-- Una línea, que debe ser un número entre 0 y 100"""
```

La función debería retornar simplemente True o False.

# RESPUESTA DE GPT

``` py
import re

def es_valido_bloque_pregunta(texto: str) -> bool:
    """
    Verifica si un bloque de texto cumple con la estructura esperada:
    _PREGUNTA seguido de 1 línea
    _RESPUESTA_CORRECTA seguido de 1 línea
    _RESPUESTAS_FALSAS seguido de 3 líneas (no vacías)
    _COBERTURA seguido de 1 número entre 0 y 100
    """
    # Limpiar saltos vacíos al inicio y al final
    lineas = texto.strip().splitlines()

    # Eliminar líneas vacías intermedias
    lineas = [linea.strip() for linea in lineas if linea.strip() != ""]

    i = 0
    try:
        # _PREGUNTA
        if lineas[i] != "_PREGUNTA":
            return False
        i += 1
        if i >= len(lineas) or lineas[i].startswith("_"):
            return False
        i += 1

        # _RESPUESTA_CORRECTA
        if lineas[i] != "_RESPUESTA_CORRECTA":
            return False
        i += 1
        if i >= len(lineas) or lineas[i].startswith("_"):
            return False
        i += 1

        # _RESPUESTAS_FALSAS
        if lineas[i] != "_RESPUESTAS_FALSAS":
            return False
        i += 1

        falsas = []
        while i < len(lineas) and not lineas[i].startswith("_") and len(falsas) < 3:
            if lineas[i].strip() != "":
                falsas.append(lineas[i])
            i += 1
        if len(falsas) != 3:
            return False

        # _COBERTURA
        if i >= len(lineas) or lineas[i] != "_COBERTURA":
            return False
        i += 1
        if i >= len(lineas):
            return False
        cobertura = lineas[i]
        if not re.fullmatch(r"\d{1,3}", cobertura):
            return False
        cobertura_num = int(cobertura)
        if not (0 <= cobertura_num <= 100):
            return False

        return True
    except IndexError:
        return False
```
