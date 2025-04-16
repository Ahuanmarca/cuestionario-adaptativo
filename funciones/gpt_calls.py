import openai
from dotenv import load_dotenv

# === Cargar API Key ===
load_dotenv()
client = openai.OpenAI()

def generar_pregunta(texto: str, modelo: str) -> str:
    """
    Genera una pregunta de opción múltiple y un puntaje de cobertura a partir de un bloque de información.
    Utiliza la API de OpenAI para hacerlo.
    """

    prompt = f"""
A continuación se presenta un fragmento de un texto de estudio. A partir de él, genera UNA sola pregunta adecuada para un examen de opción múltiple. La pregunta debe evaluar un aspecto relevante y específico del contenido, y no debe ser ambigua ni demasiado obvia.

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
{texto.strip()}
"""

    response = client.chat.completions.create(
        # model="chatgpt-4o-latest",
        # model="gpt-3.5-turbo",
        # model="gpt-4",
        # model="gpt-4-0125-preview",
        # model="gpt-4-turbo",
        # model="gpt-4o-mini",
        model=modelo,
        messages=[
            {"role": "system", "content": "Eres un experto en redacción de preguntas de examen"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    pregunta = response.choices[0].message.content.strip()
    return pregunta
