"""Transforma el DataFrame raw en registros limpios."""
import pandas as pd

def clean_value(v) -> float:
    if pd.isna(v):
        return 0.0
    try:
        return round(float(v), 2)
    except (ValueError, TypeError):
        return 0.0

def compute_indices(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["logro"] = df["AD"] + df["A"]
    df["riesgo"] = df["B"] + df["C"]
    return df

def semaforo(logro: float) -> str:
    if logro >= 90:
        return "verde"
    elif logro >= 75:
        return "amarillo"
    return "rojo"
