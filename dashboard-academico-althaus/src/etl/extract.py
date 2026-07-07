"""Extrae datos del XLS exportado por SIEWEB."""
import pandas as pd
from pathlib import Path
import os

RAW_PATH = Path(os.getenv("RAW_DATA_PATH", "data/raw/"))

def read_sieweb_xls(filename: str) -> pd.DataFrame:
    filepath = RAW_PATH / filename
    return pd.read_excel(filepath, engine="xlrd", header=None)

if __name__ == "__main__":
    df = read_sieweb_xls("RendimientoAcademicoPorCompetencia.xls")
    print(f"Leido: {df.shape[0]} filas x {df.shape[1]} columnas")
