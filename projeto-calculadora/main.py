from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow
import sys
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH


def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size: 150px;')
    return label1


if __name__ == '__main__':
    # Cria aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
