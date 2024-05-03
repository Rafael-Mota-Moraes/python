from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QGridLayout
import sys
app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red;')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 60px; color: blue;')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 2, 1)

central_widget.show()
app.exec()  # Loop da aplicação
