import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import numpy as np

# Función para controlar el brazo robótico
def controlar_brazo(grado):
    print(f"Mover brazo a {grado} grados")

# Clase para la interfaz gráfica
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Brazo Robotico")
        self.setGeometry(100, 100, 400, 300)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # Botones para controlar el brazo robótico
        for i in range(0, 181, 45):
            button = QPushButton(f"Mover a {i} grados")
            button.clicked.connect(lambda _, angle=i: controlar_brazo(angle))
            layout.addWidget(button)
        
        # Widget central
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# Inicializar la aplicación PyQt
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
