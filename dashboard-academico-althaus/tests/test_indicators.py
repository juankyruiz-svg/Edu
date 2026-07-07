"""Pruebas de indicadores."""
import pandas as pd, sys
sys.path.insert(0, ".")
from src.indicators.global_index import global_logro, global_excelencia, global_riesgo
from src.utils.colors import semaforo_color, semaforo_label, GREEN_HEX, YELLOW_HEX, RED_HEX

FIXTURE = pd.DataFrame([
    {"AD": 5.0,  "A": 85.0, "B": 10.0, "C": 0.0},
    {"AD": 0.0,  "A": 70.0, "B": 30.0, "C": 0.0},
    {"AD": 10.0, "A": 50.0, "B": 30.0, "C": 10.0},
])

def test_global_logro():
    assert global_logro(FIXTURE) == round((90 + 70 + 60) / 3, 2)

def test_global_excelencia():
    assert global_excelencia(FIXTURE) == round((5 + 0 + 10) / 3, 2)

def test_semaforo_verde():
    assert semaforo_color(95) == GREEN_HEX
    assert semaforo_label(90) == "Verde"

def test_semaforo_amarillo():
    assert semaforo_color(80) == YELLOW_HEX
    assert semaforo_label(75) == "Amarillo"

def test_semaforo_rojo():
    assert semaforo_color(60) == RED_HEX
    assert semaforo_label(74) == "Rojo"
