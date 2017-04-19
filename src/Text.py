#!/usr/bin/env python3

from PySide import QtCore, QtGui
import os
# from GUI import BUgui # warning: mutual inclusion

#------------------------------------------------------------
#------------------------------------------------------------
class BUPlainTextEdit(QtGui.QPlainTextEdit):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self):
        super().__init__()

        # css
        self.css = "QPlainTextEdit {background-color: #323232;"\
                                    "color: #ffffff;"\
                                    "font-size: 20px;"\
                                    "font-weight: bold;"\
                                    "font-family: Century Gothic, sans-serif}"

        self.setStyleSheet(self.css)
