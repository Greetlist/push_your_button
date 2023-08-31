from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QTextBrowser

class AddBuffView(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.init_component()

    def init_component(self):
        self.record_button = QPushButton("开始记录按键序列")
        self.record_button.setCheckable(True)

        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)
        self.g_layout.addWidget(self.record_button)