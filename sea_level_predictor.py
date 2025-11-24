"""
sea_level_predictor.py

Proyecto: Predictor del nivel del mar (freeCodeCamp)

Este archivo contiene la función draw_plot() que:
 - importa 'epa-sea-level.csv' con pandas
 - crea un diagrama de dispersión (Year vs CSIRO Adjusted Sea Level)
 - calcula y dibuja la línea de mejor ajuste para todos los datos extendida hasta 2050
 - calcula y dibuja la línea de mejor ajuste usando datos desde 2000 hasta el último año, extendida hasta 2050
 - etiqueta los ejes y el título
 - guarda la figura como 'sea_level_plot.png' y devuelve el objeto Figure
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    """
    Lee 'epa-sea-level.csv', crea el gráfico requerido,
    guarda la imagen y devuelve la Figure.

    Returns
    -------
    matplotlib.figure.Figure
        Figura con el gráfico (también se guarda en 'sea_level_plot.png').
    """

    # Leer datos
    df = pd.read_csv('epa-sea-level.csv')

    # Crear figura y eje
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)

    # Gráfico de dispersión
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # -------- Línea de mejor ajuste (todos los datos) --------
    x_all = df['Year']
    y_all = df['CSIRO Adjusted Sea Level']

    lr_all = linregress(x_all, y_all)
    slope_all = lr_all.slope
    intercept_all = lr_all.intercept

    # Extender la línea hasta 2050
    x_future_all = np.arange(int(x_all.min()), 2051)
    y_future_all = intercept_all + slope_all * x_future_all

    ax.plot(x_future_all, y_future_all, label='Best fit (all data)')

    # -------- Línea de mejor ajuste (desde 2000 en adelante) --------
    df_2000 = df[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']

    lr_2000 = linregress(x_2000, y_2000)
    slope_2000 = lr_2000.slope
    intercept_2000 = lr_2000.intercept

    # Extender la segunda línea hasta 2050 (inicia en 2000)
    x_future_2000 = np.arange(2000, 2051)
    y_future_2000 = intercept_2000 + slope_2000 * x_future_2000

    ax.plot(x_future_2000, y_future_2000, label='Best fit (2000 onwards)')

    # Etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Leyenda
    ax.legend()

    # Guardar figura
    plt.savefig('sea_level_plot.png')

    # Devolver la figura (para las pruebas)
    return fig


# Permitir ejecución directa para desarrollo local
if __name__ == '__main__':
    fig = draw_plot()
    plt.show()
