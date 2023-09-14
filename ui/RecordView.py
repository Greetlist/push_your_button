from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

class RecordView(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.label_list = list()
        self.init_component()

    def init_component(self):
        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)
        total_str_list = self.parent.gen_sequence_str_from_config()
        for seq_str in total_str_list:
            record_label = QLabel()
            record_label.setText(seq_str)
            self.g_layout.addWidget(record_label)