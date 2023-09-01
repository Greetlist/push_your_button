from PySide6.QtCore import QThread
from logger.logger import Logger
import time
import win32gui
import win32con
import random
from constant.key_board_mapping import QtKeyBoardStringDict

class HunterThread(QThread):
    def __init__(self, parent_widget, sequence_list, window_name):
        super().__init__()
        self.parent_widget = parent_widget
        self.sequence_list = sequence_list
        self.stop = False
        self.window_name = window_name

    def init(self):
        self.maple_window = win32gui.FindWindow(None, self.window_name)
        if self.maple_window is None:
            return False
        return True

    def run(self):
        sequence_len = len(self.sequence_list)
        print(sequence_len)
        print(self.sequence_list)
        print(self.maple_window)
        while not self.stop:
            cur_sequence_idx = random.randint(0, sequence_len) - 1
            for key in self.sequence_list[cur_sequence_idx]:
                key_info = QtKeyBoardStringDict.get(key, None)
                if key_info is not None:
                    virtual_key = key_info["VirtualKey"]
                    print(virtual_key)
                    win32gui.PostMessage(self.maple_window, win32con.WM_KEYDOWN, virtual_key, 0)
                    win32gui.PostMessage(self.maple_window, win32con.WM_KEYUP, virtual_key, 0)
                else:
                    print("error key: {}, key_info is None".format(key))
                time.sleep(0.5)