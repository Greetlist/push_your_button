from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QTableWidget

class AddBuffView(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.init_component()

        self.buff_table = QTableWidget()
        self.buff_table.setHorizontalHeaderLabels(["按键", "调用间隔"])
        self.buff_key_map = dict()

    def init_component(self):
        button_list = [
            {
                "name": "添加Buff按键",
                "slot": self.add_buff_row,
                "member_name": "record_button",
                "grid_x": 0,
                "grid_y": 0
            },
            {
                "name": "保存",
                "slot": self.save_record,
                "member_name": "save_button",
                "grid_x": 0,
                "grid_y": 1
            },
            {
                "name": "重置",
                "slot": self.reset_buff_table,
                "member_name": "start_button",
                "grid_x": 1,
                "grid_y": 0
            },
            {
                "name": "停止",
                "slot": self.stop_auto_hunter,
                "member_name": "stop_button",
                "grid_x": 1,
                "grid_y": 1
            }
        ]
        self.record_button = QPushButton("添加一个Buff按键设置")
        self.record_button.setCheckable(True)
        self.record_button.clicked.connect(self.add_buff_row)

        self.save_button = QPushButton("保存")
        self.save_button.setEnabled(True)
        self.save_button.clicked.connect(self.record_user_key_sequence)

        self.reset_button = QPushButton("重置")
        self.reset_button.setEnabled(True)
        self.reset_button.clicked.connect(self.clear_record)

        self.view_record_button = QPushButton("查看序列")
        self.view_record_button.setEnabled(True)
        self.view_record_button.clicked.connect(self.show_record)

        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)
        self.g_layout.addWidget(self.record_button)

    def add_buff_row(self):
        self.buff_table.