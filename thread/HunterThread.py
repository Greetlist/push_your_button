from PySide6.QtCore import QThread
from logger.logger import Logger
import time
import win32gui
import win32con
import random
import time
from constant.key_board_mapping import QtKeyBoardStringDict

class HunterThread(QThread):
    def __init__(self, parent_widget, window_name):
        super().__init__()
        self.parent_widget = parent_widget
        self.stop = False
        self.window_name = window_name

    def init(self):
        self.maple_window = win32gui.FindWindow(None, self.window_name)
        if self.maple_window is None:
            return False
        return True

    def set_key_sequence(self, sequence_list):
        self.sequence_list = sequence_list

    def set_buff_key_list(self, buff_list):
        self.buff_list = buff_list
        self.invoke_cache = dict()
        for item in self.buff_list:
            button_key, period = item
            self.invoke_cache[button_key] = dict()
            vk = self.get_virtual_key(button_key)
            if vk != "":
                self.invoke_cache[button_key]["virtual_key"] = vk
                self.invoke_cache[button_key]["period"] = float(period)
                self.invoke_cache[button_key]["current_invoke_time"] = time.time()

    def get_virtual_key(self, key_str):
        for _, item in QtKeyBoardStringDict.items():
            if item["String"] == key_str:
                return item["VirtualKey"]
        return ""

    def run(self):
        sequence_len = len(self.sequence_list)
        print(sequence_len)
        print(self.sequence_list)
        while not self.stop:
            self.try_invoke_buff()
            if sequence_len < 1:
                time.sleep(1)
                continue
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

    def try_invoke_buff(self):
        for button_key, key_info in self.invoke_cache.items():
            print(key_info)
            if time.time() > key_info["current_invoke_time"] + key_info["period"]:
                win32gui.PostMessage(self.maple_window, win32con.WM_KEYDOWN, key_info["virtual_key"], 0)
                win32gui.PostMessage(self.maple_window, win32con.WM_KEYUP, key_info["virtual_key"], 0)
                key_info["current_invoke_time"] = time.time()