import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPushButton
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Probando los signals")
        button = QPushButton("Acepta")
        button.setCheckable(True)
        # se llama a la acción (proceso conocido como slot)
        # la acción es accion_en_boton
        button.clicked.connect(self.accion_en_boton)

        # se ubica el boton la pantalla principal
        self.setCentralWidget(button)

    def accion_en_boton(self):
        print("Hemos dado click en un botón")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
