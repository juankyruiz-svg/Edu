"""Indicadores globales institucionales."""
import pandas as pd

def global_logro(df: pd.DataFrame) -> float:
    return round((df["AD"] + df["A"]).mean(), 2)

def global_excelencia(df: pd.DataFrame) -> float:
    return round(df["AD"].mean(), 2)

def global_riesgo(df: pd.DataFrame) -> float:
    return round((df["B"] + df["C"]).mean(), 2)
