"""Formateo de valores para el dashboard."""

def fmt_pct(v: float, decimals: int = 0) -> str:
    return f"{round(v, decimals):.{decimals}f}%"

def pedagogical_label(logro: float) -> str:
    if logro >= 90:
        return "Logro consolidado"
    elif logro >= 75:
        return "En proceso — seguimiento"
    return "Alerta — intervencion urgente"
