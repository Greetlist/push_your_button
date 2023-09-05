from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

class BuffTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, header_name):
        super(BuffTableModel, self).__init__()
        self.table_data = data
        self.header_name = header_name
        self.reset_data()

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_name[section]
        return super().headerData(section, orientation, role)

    def data(self, index, role):
        real_data = self.table_data[index.row()][index.column()]
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if type(real_data) == QLineEdit:
                return real_data.text()
            return real_data

    def rowCount(self, index):
        return len(self.table_data)

    def columnCount(self, index):
        return len(self.table_data[0])

    def insertRow(self, new_data=[]):
        new_default_data = [QLineEdit("test"), QLineEdit("111")]
        row_idx = len(self.table_data)
        self.beginInsertRows(QtCore.QModelIndex(), row_idx, row_idx)
        self.table_data.append(new_default_data)
        self.endInsertRows()
        self.layoutChanged.emit()
        return row_idx

    def reset_data(self):
        self.table_data = [
            ["1", 60],
            ["2", 120],
            ["3", 180]
        ]
        self.layoutChanged.emit()