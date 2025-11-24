# Sea Level Predictor (freeCodeCamp)

Este repositorio contiene la solución al proyecto **Predictor del nivel del mar** de freeCodeCamp (Data Analysis with Python).

## Descripción

Se analiza un conjunto de datos del cambio promedio global del nivel del mar desde 1880.  
Con esos datos se generan:

- Un diagrama de dispersión (`Year` vs `CSIRO Adjusted Sea Level`).
- Una línea de mejor ajuste usando **todos** los datos (extendida hasta 2050).
- Una segunda línea de mejor ajuste usando sólo los datos desde el año **2000** (extendida también hasta 2050).

El gráfico se guarda como `sea_level_plot.png`.

## Archivos principales

- `sea_level_predictor.py`: contiene la función `draw_plot()` que genera el gráfico.
- `main.py`: archivo auxiliar para probar el gráfico localmente.
- `test_module.py`: pruebas unitarias provistas por freeCodeCamp.
- `epa-sea-level.csv`: archivo de datos original de la EPA (proporcionado por freeCodeCamp).
- `requirements.txt`: lista de dependencias de Python.

## Cómo ejecutar

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/<tu-usuario>/sea-level-predictor.git
   cd sea-level-predictor
