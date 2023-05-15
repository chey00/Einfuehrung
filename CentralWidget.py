from PyQt6.QtWidgets import QWidget, QSlider, QTextEdit


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        slider = QSlider(self)
        slider.setRange(50, 75)
        slider.setValue(60)

        text_edit = QTextEdit(self)


