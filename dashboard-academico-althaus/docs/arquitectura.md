# Arquitectura del sistema

## Flujo de datos

```
SIEWEB (XLS) → data/raw/ → src/etl/ → data/processed/ → dashboard/ + reports/
```

## Stack

| Capa       | Tecnología                  |
|------------|-----------------------------|
| ETL        | Python, pandas, xlrd        |
| Indicadores| Python, pandas              |
| Dashboard  | Plotly Dash                 |
| Reportes   | python-pptx, python-docx    |
| CI/CD      | GitHub Actions              |
