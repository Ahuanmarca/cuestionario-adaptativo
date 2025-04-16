from types import SimpleNamespace

MODELOS = SimpleNamespace(
    gpt4o="gpt-4o",
    gpt4turbo="gpt-4-1106-preview",
    gpt35="gpt-3.5-turbo"
)

MODELO_ACTUAL = MODELOS.gpt35

# WARNING: HARDCODED PRICES MAY CHANGE
COSTO_MODELOS = {
    MODELOS.gpt4o: 0.005,
    MODELOS.gpt4turbo: 0.01,
    MODELOS.gpt35: 0.001,
}

TOKENS_POR_BLOQUE = 1000

ARCHIVO_ENTRADA="temario/temario.txt"

ARCHIVO_SALIDA="temario_salida.txt"
