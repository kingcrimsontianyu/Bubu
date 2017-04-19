#!/usr/bin/env python3

from PySide import QtCore, QtGui
import os
# from GUI import BUgui # warning: mutual inclusion

#------------------------------------------------------------
#------------------------------------------------------------
class BUMessageBox(QtGui.QMessageBox):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self, guiData = None):
        super().__init__()

        # css
        self.css = "QMessageBox {background-color: #323232;"\
                                "font-size: 20px;"\
                                "font-weight: bold;"\
                                "font-family: Century Gothic, sans-serif}"\
                    "QMessageBox QLabel {"\
                                "color: #ffffff;"\
                                "}"\
                    "QMessageBox QPushButton {"\
                                "font-size: 20px;"\
                                "font-weight: bold;"\
                                "font-family: Century Gothic, sans-serif}"
        self.m_data = guiData

        self.setStyleSheet(self.css)
        self.setIcon(QtGui.QMessageBox.Icon(QtGui.QMessageBox.Information))

        if guiData is not None:
            self.setWindowTitle("bubu")
            self.setWindowIcon(QtGui.QIcon(os.path.join(self.m_data.pictureDir, 'bubu.png')))
