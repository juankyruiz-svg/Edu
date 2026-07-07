"""Semaforo de desempeno institucional."""

VERDE_UMBRAL = 90
AMARILLO_UMBRAL = 75
GREEN_HEX = "#639922"
YELLOW_HEX = "#BA7517"
RED_HEX = "#E24B4A"

def semaforo_color(logro: float) -> str:
    if logro >= VERDE_UMBRAL:
        return GREEN_HEX
    elif logro >= AMARILLO_UMBRAL:
        return YELLOW_HEX
    return RED_HEX

def semaforo_label(logro: float) -> str:
    if logro >= VERDE_UMBRAL:
        return "Verde"
    elif logro >= AMARILLO_UMBRAL:
        return "Amarillo"
    return "Rojo"
