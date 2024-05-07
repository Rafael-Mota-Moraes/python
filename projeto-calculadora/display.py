from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGING, MINUMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from utils import isEmpty, isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGING for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINUMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()  # 'a'
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]

        if isEnter or text == '=':
            print(f'EQ {text} pressionado, sinal emitido', type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()

        if isDelete or text == 'C' or text == 'c':
            print('isDelete pressionado, sinal emitido', type(self).__name__)
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            print('isEsc pressionado, sinal emitido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            print('inputPressed pressionado, sinal emitido', type(self).__name__)
            self.inputPressed.emit(text)
            return event.ignore()
