#!/usr/bin/env python3

from PySide import QtCore, QtGui
import os
# from GUI import BUgui # warning: mutual inclusion

#------------------------------------------------------------
#------------------------------------------------------------
class BUTableWidget(QtGui.QTableWidget):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self):
        super().__init__()

        # css
        self.css = "QTableWidget {background-color: #323232;"\
                                "color: #66ffb2;"\
                                "gridline-color: #ffffff;"\
                                "font-size: 20px;"\
                                "font-weight: bold;"\
                                "font-family: Century Gothic, sans-serif}"\
                   "QTableWidget QTableCornerButton::section {background-color: #323232;"\
                                "border: 1px solid #ffffff;}"\
                   "QHeaderView::section {background-color: #323232;"\
                                "color: #33ff99;"\
                                "border: 1px solid #ffffff;"\
                                "font-size: 20px;"\
                                "font-weight: bold;"\
                                "font-family: Century Gothic, sans-serif}"

        self.setStyleSheet(self.css)

#------------------------------------------------------------
# css style sheet does not apply
#------------------------------------------------------------
class BUTableWidgetItem(QtGui.QTableWidgetItem):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self):
        super().__init__()
