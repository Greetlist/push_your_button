from PySide6.QtWidgets import QWidget, QLabel

class RecordView(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.init_component()

    def init_component(self):
        self.record_label = QLabel()
        self.record_label.setText(self.parent.gen_sequence_str())