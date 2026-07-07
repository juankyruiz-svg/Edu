# Gestión Académica — Colegio Clemente Althaus

Repositorio de trabajo del Subdirector Académico. Centraliza dashboards, rúbricas, evaluaciones y materiales de gestión pedagógica.

## Estructura

```
├── dashboards/
│   └── rendimiento-academico/     → Análisis de competencias (AD/A/B/C), reportes semáforo por trimestre
├── rubricas/
│   └── coordinador-nivel/         → Rúbrica F-GTH-14 y otras rúbricas de evaluación de cargos
├── evaluaciones-desempeno/
│   └── observaciones-docentes/    → Informes individuales de observación de aula por docente
├── curriculo-diversificado/       → Programaciones anuales, diversificación curricular CNEB
├── monitoreo-pedagogico/
│   └── visitas-aula/              → Fichas de monitoreo, feedback de sesiones
├── capacitacion-docente/
│   └── GIA/                       → Materiales de Grupos de Interaprendizaje, talleres
└── docs/                          → Normativa MINEDU/UGEL, actas, comunicados
```

## Cómo usar este repo

1. Cada carpeta tiene su propio README con contexto.
2. Los scripts de análisis (Python/pandas) van en la subcarpeta correspondiente a su tema (ej: un script de análisis de notas → `dashboards/rendimiento-academico/`).
3. Nombra los archivos con formato: `AAAA-trimestre-descripcion.ext` (ej: `2026-T2-comite-grado-7-9.xlsx`).

## Próximos pasos

- [ ] Subir scripts de análisis existentes a `dashboards/rendimiento-academico/`
- [ ] Subir rúbrica F-GTH-14 a `rubricas/coordinador-nivel/`
- [ ] Subir informes de observación a `evaluaciones-desempeno/observaciones-docentes/`
