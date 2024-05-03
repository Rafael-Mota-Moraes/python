from PySide6.QtWidgets import QApplication, QPushButton
import sys
app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red;')
botao.show()

app.exec()  # Loop da aplicação
