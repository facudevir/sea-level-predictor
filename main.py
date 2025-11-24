"""
main.py

Archivo de apoyo para probar localmente el proyecto
\"Predictor del nivel del mar\" de freeCodeCamp.
"""

from sea_level_predictor import draw_plot

if __name__ == "__main__":
    # Generar el gráfico y mostrarlo en pantalla
    fig = draw_plot()
    fig.show()
