from ui import ScreenShotCoordinateView
from ui import FunctionalView
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QTextBrowser
from PySide6.QtCore import QSize
from thread.LogFetcherThread import LogFetcherThread
from PySide6 import QtWidgets

class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.init_child_widget()
        self.init_log_fetch_thread()

    def init_child_widget(self):
        button_list = [
            {
                "name": "Add Attack",
                "slot": self.open_add_attack_window,
                "member_name": "add_attack_button",
                "grid_x": 0,
                "grid_y": 0
            },
            {
                "name": "Add Buff",
                "slot": self.open_add_buff_window,
                "member_name": "add_buff_button",
                "grid_x": 0,
                "grid_y": 1
            },
            {
                "name": "Start",
                "slot": self.start_auto_hunter,
                "member_name": "start_button",
                "grid_x": 1,
                "grid_y": 0
            },
            {
                "name": "Stop",
                "slot": self.stop_auto_hunter,
                "member_name": "stop_button",
                "grid_x": 1,
                "grid_y": 1
            }
        ]

        self.g_layout = QGridLayout()
        self.setLayout(self.g_layout)

        for button_info in button_list:
            cur_button = QPushButton(button_info["name"])
            cur_button.setCheckable(True)
            cur_button.clicked.connect(button_info["slot"])
            setattr(self, button_info["member_name"], cur_button)
            self.g_layout.addWidget(getattr(self, button_info["member_name"], cur_button), button_info["grid_x"], button_info["grid_y"])
        self.stop_button.setEnabled(False)

        self.log_browser = QTextBrowser()
        self.g_layout.addWidget(self.log_browser, 2, 0, 1, 4)

    def open_add_attack_window(self):
        pass

    def open_add_buff_window(self):
        pass

    def start_auto_hunter(self):
        self.start_button.setText("Hunting")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_auto_hunter(self):
        if self.hunter_thread.isRunning():
            self.hunter_thread.terminate()
            self.stop_button.setText("Stoping...")
            self.stop_button.setEnabled(False)
            self.hunter_thread.wait()
            self.stop_button.setText("Stop")
            self.start_button.setText("Start Fishing")
            self.start_button.setEnabled(True)

    def init_log_fetch_thread(self):
        self.log_fetch_thread = LogFetcherThread.LogFetcherThread(self)
        self.log_fetch_thread.start()

    def append_text(self, text):
        if text is not None:
            self.log_browser.append(text)

    def closeEvent(self, e):
        self.log_fetch_thread.terminate()