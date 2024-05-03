from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
from PySide6.QtCore import Slot
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


@Slot()
def slot_exemple(status_bar):
    status_bar.showMessage('Meu slot foi executado')


@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(act):
    def inner():
        outro_slot(bool(act.isChecked))
    return inner


# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(lambda: slot_exemple(status_bar))


segunda_acao = primeiro_menu.addAction('segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao1.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec()  # Loop da aplicação
