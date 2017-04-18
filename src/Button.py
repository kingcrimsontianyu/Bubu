#!/usr/bin/env python3

from PySide import QtCore, QtGui
import os
# from GUI import BUgui # warning: mutual inclusion

#------------------------------------------------------------
#------------------------------------------------------------
class BUPushButton(QtGui.QPushButton):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self, text):
        super().__init__(text)

        # css
        self.css = "QPushButton {padding: 5px;"\
                                "text-align:left;"\
                                "background-color: #3399ff;"\
                                 "color: white;"\
                                 "border: none;"\
                                 "font-size: 20px;"\
                                 "font-weight: bold;"\
                                 "font-family: Century Gothic, sans-serif}"\
                                 "QPushButton:pressed {"\
                                 "background-color: #66b2ff;}"

        self.setStyleSheet(self.css)


