# Dashboard Estratégico de Rendimiento Académico — Clemente Althaus

Dashboard institucional para el análisis y comunicación de resultados por competencias del nivel Primaria, Periodo 1 — 2026.

## Estructura

| Carpeta | Contenido |
|---------|-----------|
| `data/raw/` | Exportaciones originales de SIEWEB (no versionadas) |
| `data/processed/` | CSVs limpios generados por el pipeline ETL |
| `src/etl/` | Scripts de extracción y transformación |
| `src/indicators/` | Cálculo de índices: logro, excelencia, riesgo, rankings |
| `dashboard/` | Aplicación Plotly Dash para padres de familia |
| `reports/` | Generación automática de informes Word y PPT |
| `notebooks/` | Exploración y prototipado |
| `docs/` | Documentación técnica y pedagógica |

## Instalación

```bash
git clone https://github.com/tu-usuario/dashboard-academico-althaus.git
cd dashboard-academico-althaus
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Uso

```bash
# 1. Coloca el XLS de SIEWEB en data/raw/
# 2. Ejecuta el pipeline ETL
python -m src.etl.extract
python -m src.etl.transform
python -m src.etl.load

# 3. Lanza el dashboard
python dashboard/app/app.py
```

## Criterios de semáforo

| Color | Umbral | Significado |
|-------|--------|-------------|
| Verde  | ≥ 90%  | Logro consolidado |
| Amarillo | 75–89% | En proceso, seguimiento |
| Rojo | < 75% | Alerta, intervención urgente |

## Escala CNEB (MINEDU)

- **AD** — Logro destacado
- **A** — Logro previsto
- **B** — En proceso
- **C** — En inicio

---

Desarrollado por la Subdirección Académica — Colegio Clemente Althaus.
