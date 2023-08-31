import PySide6.QtCore as QtCore
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QTextBrowser
import time
from constant.key_board_mapping import QtKeyBoardStringDict

class AddKeySequenceView(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.init_component()
        self.init_layout()

        self.key_sequence = []
        self.key_string_sequence = []

    def init_component(self):
        self.save_button = QPushButton("保存")
        self.save_button.setEnabled(True)
        self.save_button.clicked.connect(self.record_user_key_sequence)

        self.reset_button = QPushButton("重置")
        self.reset_button.setEnabled(False)
        self.reset_button.clicked.connect(self.clear_record)

        self.record_brower = QTextBrowser()
        self.record_brower.installEventFilter(self)

        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)
        self.g_layout.addWidget(self.save_button)
        self.g_layout.addWidget(self.reset_button)
        self.g_layout.addWidget(self.record_brower)

    def record_user_key_sequence(self):
        self.save_button.setEnabled(False)
        self.reset_button.setEnabled(True)

    def clear_record(self):
        self.save_button.setEnabled(True)
        self.reset_button.setEnabled(False)
        self.key_sequence = []
        self.key_string_sequence = []

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            key_info = QtKeyBoardStringDict.get(key, None)
            if key_info is not None:
                key_string = key_info["String"]
            else:
                key_string = "Unknown"
            self.key_sequence.append(key)
            self.key_string_sequence.append(key_string)
            self.record_brower.setText(self.gen_sequence_str())
            return True
        return False

    def gen_sequence_str(self):
        return " -> ".join(self.key_string_sequence)

    def init_layout(self):
        pass        

    def add_attack_key(self, key):
        pass