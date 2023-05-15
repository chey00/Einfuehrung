from PyQt6.QtWidgets import QWidget, QSlider, QTextBrowser, QHBoxLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.text_edit = QTextBrowser(self)
        self.text_edit.setText("Started app")

        self.slider = QSlider(self)
        self.slider.setRange(50, 75)
        self.slider.setValue(60)
        self.slider.valueChanged.connect(self.append_text)

        layout = QHBoxLayout(self)
        layout.addWidget(self.slider)
        layout.addWidget(self.text_edit)

        self.setLayout(layout)

    def append_text(self, value_as_int):
        text = "Value changed: " + str(value_as_int)
        self.text_edit.append(text)
