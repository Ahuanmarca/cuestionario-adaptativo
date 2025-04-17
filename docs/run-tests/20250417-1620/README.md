# Conteo de errores en preguntas generadas por GPT

TLDR >> 10 errores en 277 bloques procesados. No tan mal.

PRUEBA
Noté que preguntas generados por GPT 3.5 tienen errores de formaato.
Usé función validar_pregunta para chequear preguntas generadas por GPT.
Comprobación ocurre en script020_generar_preguntas.py.
Cuando hay error, se agrega una línea "=== TO FIX ===" en el archivo generado.

RESULTADO
En temario_salida.txt puedo hacer un search del string "TO FIX".
Sólo encontré 10 errores en total (en total eran más de 270 bloques).
Es decir, el problema no es tan malo, **pero sería ideal que no hubieran estos errores**.
