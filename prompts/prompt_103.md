# Cuestionario Adaptativo App

## Proyecto:
Aplicación para entrenar para exámenes de opción múltiple

## Descripción breve:
* La aplicación generará preguntas en base a un material original.
* El material original estará estructurado de una forma específica.
* La aplicación generará un archivo txt que servirá como base de datos, donde almacenará las preguntas con una estructura normalizada.
* Cuando el usuario quiera entrenar, la aplicación hará una selección de preguntas, siguiendo ciertos criterios que debemos definir.
* Algunos de los criterios son:
* Se seleccionan 60 preguntas de la base de datos (que puede tener cientos o miles de preguntas).
* Se selecciona una cantidad de cada “libro” o “tema” que componga el temario. En principio queremos 20 de “Condiciones Generales”, 12 de “Igualdad de Género”, 12 de “Cultura de Seguridad” y 16 de “Experiencia de Usuario”.
* La aplicación presentará las preguntas al usuario y aceptará respuestas y feedback.
* Cuando el usuario termine de responder el cuestionario:
    * Se le presentará un resumen de su desempeño.
    * En base a las respuestas y el feedback de actualizará la base de datos.
* Cuando el usuario vuelva a utilizar la aplicación para entrenar, la aplicación utilizará la base de datos actualizada, lo cual eventualmente llevará a cuestionarios mejorados y mejor entrenamiento.

---

La información de origen estará en un archivo .txt plano, que contendrá cientos o miles de preguntas, y tendrá la siguiente estructura:

```
_LIBRO
Condiciones Generales
_CAPITULO
Título Preliminar

_INFORMACION
Renfe Viajeros tiene por objeto social:
* La prestación de servicios de transporte de viajeros por ferrocarril, tanto nacional como internacional.
* La mediación en la prestación de cualesquiera servicios turísticos.
* La organización, oferta y/o comercialización de viajes combinados o productos turísticos.
* La prestación de otros servicios o actividades complementarias o vinculadas al transporte ferroviario.

_INFORMACION
Renfe Viajeros presta el servicio de transporte de viajeros por ferrocarril, bajo el principio de seguridad, desarrollando su actividad con una clara orientación al cliente, con criterios de calidad, eficiencia, rentabilidad e innovación, persiguiendo el incremento de la cuota de mercado del ferrocarril, sobre la base del compromiso con la sociedad y el desarrollo de sus empleados.

_LIBRO
Condiciones Generales
_CAPITULO
Contrato de Transporte

_INFORMACION
El título de transporte es el documento que formaliza el contrato de transporte entre Renfe Viajeros y la persona que viaja. Faculta al viajero para hacer uso del servicio.

_INFORMACION
Características del título de transporte:
* Puede ser oneroso o gratuito.
* Puede ser para la prestación de uno o más servicios de transporte.
* Puede incluir otros servicios.
* Existen diferentes formatos (soportes) de títulos de transporte, en función del sistema de venta utilizado.
* Todos los títulos de transporte están provistos de un sistema de seguridad, con el objetivo de evitar el fraude.

_INFORMACION
Obligaciones del cliente con respecto al título de transporte:
* El cliente debe disponer de un título de transporte válido durante todo el viaje, que deberá conservar desde la entrada a la estación de origen hasta la salida de la estación de destino.
* En caso de ser solicitado por el personal de Renfe Viajeros, o el personal autorizado, deberá presentarlo, junto con los documentos acreditativos correspondientes.
* El cliente deberá comprobar, en el momento de obtener el título de transporte, que los datos de este se ajustan a su petición, pudiendo desistir en ese momento de contratar.
```

## Flujo de la aplicación

Antes de que el usuario pueda empezar a entrenar respondiendo cuestionarios, la aplicación tiene que hacer una preparación previa para tener una primera versión de la base de datos con preguntas.

## PREPARACIÓN PREVIA

### Paso 1: Normalizar información cruda

Queremos generar un archivo de salida con la siguiente estructura para cada bloque de información. Ejemplo de estructura:

```
_LIBRO
Libro Blanco de la Cultura de Seguridad del Grupo Renfe
_CAPITULO
Introducción
_ETIQUETAS
[]
_COBERTURA
0
_INFORMACION
Objetivo del Libro Blanco de Cultura de Seguridad Operacional del Grupo Renfe: Presentar la Cultura de Seguridad Operacional revisada que el Grupo Renfe quiere implantar y el Plan de Transformación que la hará posible, con visión alineada con el Plan Estratégico 2019-2023-2028 del Grupo.
```

Explicación de los campos en la estructura anterior:
_LIBRO <-- Título del libro
_CAPITULO <-- Título del capítulo
_ETIQUETAS <-- Dos square brackets vacíos. Aún no he diseñado la funcionalidad que tendrán estas etiquetas. Creo que irían cosas de diferente naturaleza que luego faciliten la filtración, como LEYES, DIFICIL, CIFRAS, IMPORTANTE, etc.
_COBERTURA <-- Representa que tan cubierto está el bloque de información a través de las preguntas generadas en base dicho bloque. Es un atributo del bloque de información, no de las preguntas generadas a partir del mismo. Empieza en 0 porque al principio no existen preguntas generadas.
_INFORMACIÓN <-- El bloque de información completo del texto original.

#### PSEUDOCODE

``` bash
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
```

#### TODO

[x] Crear función separar_bloques()
[x] Crear función generar_estructura()

### Paso 2: Generar preguntas

Por cada bloque de información queremos usar la API de GPT para generar:
* UNA pregunta adecuada para un examen de opción múltiple.
* Una respuesta correcta.
* 3 respuestas falsas pero realistas.
* Un número de 0 a 100 que represente la cobertura.
El output de GPT será validado por la aplicación.
Después de validado cada output, será agregado debajo del bloque de información de la siguiente manera:

```
_LIBRO
Libro Blanco de la Cultura de Seguridad del Grupo Renfe
_CAPITULO
Introducción
_ETIQUETAS
[]
_COBERTURA
80  <-- cobertura calculada
_INFORMACION
Objetivo del Libro Blanco de Cultura de Seguridad Operacional del Grupo Renfe: Presentar la Cultura de Seguridad Operacional revisada que el Grupo Renfe quiere implantar y el Plan de Transformación que la hará posible, con visión alineada con el Plan Estratégico 2019-2023-2028 del Grupo.

_PREGUNTA
Pregunta generada.
_RESPUESTA_CORRECTA
Respuesta correcta generada.
_RESPUESTAS_FALSAS
1era respuesta falsa generada.
2da respuesta falsa generada.
3ra respuesta falsa generada.
_DESCARTADA
[]
_ACIERTOS_CONSECUTIVOS
0
_REFORMULADA
False
```

#### PSEUDOCODE
``` bash
texto_entrada = 1er argumento de main
texto_salida_arr = []
errores = 0

generar_pregunta_prompt = """A continuación se presenta un fragmento de un texto de estudio. A partir de él, genera UNA sola pregunta adecuada para un examen de opción múltiple. La pregunta debe evaluar un aspecto relevante y específico del contenido, y no debe ser ambigua ni demasiado obvia.

También deberás generar:
- Una respuesta correcta.
- Tres respuestas incorrectas pero creíbles.
- Un número de 0 a 100 que indique qué tan completamente se cubre el contenido del texto con esta pregunta. Si solo pregunta por un aspecto pequeño, el número será bajo. Si cubre casi todo lo importante, el número será alto. Si todos los aspectos del texto están cubiertos, el número debería ser de al menos 90.

FORMATO DE RESPUESTA:
_PREGUNTA
[Pregunta generada]
_RESPUESTA_CORRECTA
[Respuesta correcta]
_RESPUESTAS_FALSAS
[Respuesta falsa 1]
[Respuesta falsa 2]
[Respuesta falsa 3]
_COBERTURA
[número entre 0 y 100]

TEXTO:
[Texto del bloque]"""

array bloques_informacion[] = separar_bloques(texto_entrada, "_LIBRO")
for bloque in bloques_informacion[]:
    informacion = obtener_informacion(bloque, "_INFORMACION") # obtiene solo el texto bajo _INFORMACION
    pregunta_generada = generar_pregunta(informacion, generar_pregunta_prompt) # generar pregunta con GPT
    
    if (validar_pregunta(pregunta_generada) == False:
        errores = errores +1
        if errores >= 5:
            detener todo el script y lanzar advertencia clara    
    else:
        estructura = generar_estructura(informacion, pregunta_generada) # no olvidar actualizar _COBERTURA
        append estructura a archivo_salida

hacer backup de archivo_entrada en carpeta de debugging
sobre escribir archivo_entrada con contenido de archivo_salida
```

#### TODO
[x] función obtener_informacion()
[ ] función generar_pregunta()
[ ] función validar_pregunta()
[ ] función generar_estructura()
[ ] función obtener_puntaje_cobertura()

---

En este punto la base de datos está lista para ser utilizada por la aplicación para que el usuario realice sesiones de entrenamiento.

Cada bloque de información debería tener una _COBERTURA calculada, y un único bloque de _PREGUNTA debajo.

---

UTILIZACIÓN DE LA APLICACIÓN PARA ENTRENAR

### Paso 3: Cuestionario

El usuario lanza la aplicación para entrenar.
La aplicación genera un cuestionario de 64 preguntas.
El usuario responde las preguntas y (opcionalmente) da feedback.
Cuando acierta, la aplicación muestra un mensaje de éxito.
Cuando se equivoca, la aplicación muestra un mensaje de equivocación, la respuesta correcta, y el fragmento de información correspondiente.
La aplicación va almacenando las respuestas y el feedback (¿en un objeto?). Tendrá que poder mapear cada una a su posición en la base de datos en el siguiente paso (iteración de la base de datos).
Al terminar, la aplicación brinda un resumen al usuario.
También al terminar, se genera una iteración de la base de datos.

### Paso 4: Iteración de la base de datos

Después de que el usuario ha terminado de responder un cuestionario, la aplicación debe actualizar los bloques de información y las respuestas de la base de datos, en base a las respuestas y el feedback provisto por el usuario.

#### PSEUDOCODE
Suponiendo que respuestas[] es un array con las respuestas, almacenadas como objetos u alguna otra estructura de datos adecuada.
```
for respuesta in respuestas[]:
    if respuesta correcta:
        if no hay feedback:
            if _ACIERTOS_CONSECUTIVOS >= 0:
                _ACIERTOS_CONSECUTIVOS += 1
            else if _ACIERTOS_CONSECUTIVOS < 0:
                _ACIERTOS_CONSECUTIVOS = 1
            else if _ACIERTOS_CONSECUTIVOS >= 5:
                if _REFORMULADA == False:
                    agregar DOMINADA a campo _DESCARTADA (dentro de los corchetes).
                    generar una nueva versión de la pregunta, cumpliendo con:
                        * sin cambiar el sentido
                        * debe tener _REFORMULADA == True (significa que la pregunta es la reformulación de otra pregunta)
                        * debe tener _ACIERTOS_CONSECUTIVOS == 0
                    agregar nueva pregunta debajo de la anterior (su parent)
                if _REFORMULADA == True && _COBERTURA < 90%:
                    agregar “DOMINADA” al campo _DESCARTADA
                    generar pregunta completamente nueva en base al bloque de información, con todos sus atributos reseteados
                    actualizar cobertura (debería aumentar)
                if _REFORMULADA == True && _COBERTURA >= 90%:
                    Se debe considerar todo el bloque de contenido como DOMINADO, y ya no aparecerá en futuros cuestionarios generados.
        if usuario da feedback (marca pregunta como "chiva", "sentido común", etc):
            se agrega el defecto a corchetes de _DESCARTADA (ej. [ CHIVA ]), para indicar que la pregunta está descartada, y el motivo
            se genera una nueva pregunta que no tenga ese defecto con GPT
            la pregunta se agrega debajo de la anterior (su parent)

    else if respuesta incorrecta:
        se ignora el feedback, si lo hay
        si _ACIERTOS_CONSECUTIVOS > 0, se pone en 0
        si _ACIERTOS_CONSECUTIVOS <= 0, se le hace -1 # <-- para poder implementar luego algún sistema que priorice las preguntas más débiles, pero aún no lo he esbozado).

guardar base de datos actualizada
```

#### TODO
* función para chequear cobertura

---
