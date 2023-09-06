from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QTableView
from ui.BuffTable import BuffTableModel

class AddBuffView(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.init_component()

    def init_component(self):
        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)
        button_list = [
            {
                "name": "添加Buff按键",
                "slot": self.add_buff_row,
                "member_name": "record_button"
            },
            {
                "name": "保存",
                "slot": self.save_record,
                "member_name": "save_button"
            },
            {
                "name": "重置",
                "slot": self.reset_buff_table,
                "member_name": "reset_button",
            },
            {
                "name": "查看",
                "slot": self.show_record,
                "member_name": "show_button"
            }
        ]
        for button_info in button_list:
            cur_button = QPushButton(button_info["name"])
            cur_button.setCheckable(True)
            cur_button.clicked.connect(button_info["slot"])
            setattr(self, button_info["member_name"], cur_button)
            self.g_layout.addWidget(getattr(self, button_info["member_name"], cur_button))

        self.buff_table = QTableView()
        self.buff_table_model = BuffTableModel(["按键", "调用间隔"])
        self.buff_table.setModel(self.buff_table_model)
        #self.buff_table.setHorizontalHeaderLabels(["按键", "调用间隔"])
        self.buff_key_map = dict()
        self.g_layout.addWidget(self.buff_table)

    def add_buff_row(self):
        self.buff_table_model.insertRow()

    def save_record(self):
        self.buff_table_model.save_buff_config()

    def reset_buff_table(self):
        self.buff_table_model.reset_data()

    def show_record(self):
        pass