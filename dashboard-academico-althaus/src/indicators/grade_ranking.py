"""Ranking de grados por indice de logro."""
import pandas as pd

def grade_ranking(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby("grado").apply(
        lambda g: round((g["AD"] + g["A"]).mean(), 2)
    ).reset_index()
    grouped.columns = ["grado", "logro"]
    grouped["ranking"] = grouped["logro"].rank(ascending=False).astype(int)
    return grouped.sort_values("ranking")
