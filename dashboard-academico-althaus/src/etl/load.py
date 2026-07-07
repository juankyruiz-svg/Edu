"""Exporta datos procesados a data/processed/."""
import pandas as pd
from pathlib import Path
import os

PROCESSED_PATH = Path(os.getenv("PROCESSED_DATA_PATH", "data/processed/"))

def save_csv(df: pd.DataFrame, filename: str) -> None:
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    out = PROCESSED_PATH / filename
    df.to_csv(out, index=False, encoding="utf-8-sig")
    print(f"Guardado: {out} ({len(df)} filas)")
