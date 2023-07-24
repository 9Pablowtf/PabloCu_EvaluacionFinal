import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton

class GraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Graficar Valores')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.table = QTableWidget(5, 2)  # Crear una tabla con 5 filas y 2 columnas
        self.table.setHorizontalHeaderLabels(["Categoría", "Valor"])

        categorias = ["Categoría A", "Categoría B", "Categoría C", "Categoría D", "Categoría E"]

        for i in range(5):
            categoria_item = QTableWidgetItem(categorias[i])
            valor_item = QTableWidgetItem("0.0")  # Inicializar los valores de la tabla en 0.0
            self.table.setItem(i, 0, categoria_item)
            self.table.setItem(i, 1, valor_item)

        self.layout.addWidget(self.table)

        self.btn_graficar = QPushButton('Graficar')
        self.btn_graficar.clicked.connect(self.graficar_valores)
        self.layout.addWidget(self.btn_graficar)

        self.setLayout(self.layout)
        self.show()

    def obtener_valores(self):
        valores = []
        for i in range(5):
            valor_item = self.table.item(i, 1)
            try:
                valor = float(valor_item.text())
                valores.append(valor)
            except ValueError:
                print("Error: Ingrese un número válido.")
                return None
        return valores

    def graficar_valores(self):
        valores = self.obtener_valores()
        if valores is not None:
            categorias = ["Categoría A", "Categoría B", "Categoría C", "Categoría D", "Categoría E"]
            x = list(range(1, 6))
            plt.bar(x, valores, color='b', align='center')
            plt.xlabel("Categorías")
            plt.ylabel("Valor")
            plt.title("Gráfico de los valores ingresados")
            plt.xticks(x, categorias)  # Asignar las etiquetas de las categorías en el eje x
            plt.grid(True)
            plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphApp()
    sys.exit(app.exec_())
