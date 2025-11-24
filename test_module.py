import unittest
import os
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo para evitar problemas en entornos sin pantalla

import matplotlib.pyplot as plt
from sea_level_predictor import draw_plot


class SeaLevelPredictorTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Ejecuta draw_plot() una sola vez para todas las pruebas
        y guarda la figura resultante.
        """
        # Asegurarse de que no quede una imagen vieja interfiriendo
        if os.path.exists("sea_level_plot.png"):
            os.remove("sea_level_plot.png")

        cls.fig = draw_plot()
        cls.ax = cls.fig.axes[0]  # Obtener el eje principal

    def test_image_file_created(self):
        """
        Verifica que el archivo de imagen sea_level_plot.png se haya creado.
        """
        self.assertTrue(os.path.exists("sea_level_plot.png"),
                        "El archivo 'sea_level_plot.png' no se creó.")

    def test_title(self):
        """
        Verifica que el título del gráfico sea 'Rise in Sea Level'.
        """
        title = self.ax.get_title()
        self.assertEqual(title, "Rise in Sea Level",
                         f"El título del gráfico debería ser 'Rise in Sea Level', pero es '{title}'.")

    def test_x_label(self):
        """
        Verifica que la etiqueta del eje x sea 'Year'.
        """
        xlabel = self.ax.get_xlabel()
        self.assertEqual(xlabel, "Year",
                         f"La etiqueta del eje x debería ser 'Year', pero es '{xlabel}'.")

    def test_y_label(self):
        """
        Verifica que la etiqueta del eje y sea 'Sea Level (inches)'.
        """
        ylabel = self.ax.get_ylabel()
        self.assertEqual(ylabel, "Sea Level (inches)",
                         f"La etiqueta del eje y debería ser 'Sea Level (inches)', pero es '{ylabel}'.")

    def test_scatter_points_exist(self):
        """
        Verifica que haya al menos una serie de puntos de dispersión en el gráfico.
        """
        # Obtener todos los artistas tipo PathCollection (scatter)
        scatter_plots = [artist for artist in self.ax.collections
                         if isinstance(artist, matplotlib.collections.PathCollection)]
        self.assertTrue(len(scatter_plots) > 0,
                        "No se encontró ningún gráfico de dispersión en el eje.")

    def test_lines_exist(self):
        """
        Verifica que existan al menos dos líneas en el gráfico
        (las dos líneas de mejor ajuste).
        """
        lines = self.ax.get_lines()
        self.assertTrue(len(lines) >= 2,
                        "Debería haber al menos dos líneas de mejor ajuste en el gráfico.")

    def test_lines_reach_2050(self):
        """
        Verifica que las líneas de mejor ajuste se extiendan hasta el año 2050.
        No es estrictamente pixel-perfect, solo se verifica que el mayor valor de x
        de las líneas sea >= 2050.
        """
        lines = self.ax.get_lines()
        max_x_values = []

        for line in lines:
            x_data = line.get_xdata()
            if len(x_data) > 0:
                max_x_values.append(max(x_data))

        self.assertTrue(any(x >= 2050 for x in max_x_values),
                        "Al menos una de las líneas de mejor ajuste debería extenderse hasta el año 2050.")

    @classmethod
    def tearDownClass(cls):
        """
        Cierra la figura después de las pruebas para liberar memoria.
        """
        plt.close(cls.fig)


if __name__ == "__main__":
    unittest.main()
