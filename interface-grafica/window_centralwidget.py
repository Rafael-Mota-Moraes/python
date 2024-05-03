from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
import sys
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 40px; color: red;')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 60px; color: blue;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 2, 1)

# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Olá')


def slot_exemple(status_bar):
    status_bar.showMessage('Meu slot foi executado')


# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))


window.show()
app.exec()  # Loop da aplicação
