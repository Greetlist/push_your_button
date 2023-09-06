from typing import Any, Union
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import json
import os

class BuffTableModel(QtCore.QAbstractTableModel):
    def __init__(self, header_name):
        super(BuffTableModel, self).__init__()
        self.header_name = header_name
        self.root_path = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.root_path, "buff_config.json")
        self.reset_data()

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_name[section]
        return super().headerData(section, orientation, role)

    def data(self, index, role):
        real_data = self.table_data[index.row()][index.column()]
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return real_data

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.table_data[index.row()][index.column()] = str(value)
            return True
        return super().setData(index, value, role)        

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def rowCount(self, index):
        return len(self.table_data)

    def columnCount(self, index):
        return len(self.table_data[0])

    def insertRow(self, new_data=[]):
        new_default_data = ["", 120]
        row_idx = len(self.table_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_idx, row_idx)
        self.table_data.append(new_default_data) if len(new_data) == 0 else self.table_data.append(new_data)
        self.endInsertRows()
        self.layoutChanged.emit()
        return row_idx

    def reset_data(self):
        self.read_history_config()
        self.layoutChanged.emit()

    def read_history_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                raw_data = f.read()
                print(raw_data)
                self.table_data = json.loads(raw_data)
        else:
            self.table_data = [["test", "test"]]

    def save_buff_config(self):
        with open(self.config_path, "w+") as f:
            f.write(json.dumps(self.table_data))