"""Ranking de areas curriculares."""
import pandas as pd

def area_ranking(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby("area").apply(
        lambda g: round((g["AD"] + g["A"]).mean(), 2)
    ).reset_index()
    grouped.columns = ["area", "logro"]
    grouped["ranking"] = grouped["logro"].rank(ascending=False).astype(int)
    return grouped.sort_values("ranking")
