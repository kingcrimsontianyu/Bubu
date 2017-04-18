#!/usr/bin/env python3

from PySide import QtCore, QtGui
import os
# from GUI import BUgui # warning: mutual inclusion

#------------------------------------------------------------
#------------------------------------------------------------
class BUScrollArea(QtGui.QScrollArea):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self):
        super().__init__()

        # css
        self.css = "QScrollArea {background-color: #ffffff;"\
                                "}"

        self.setStyleSheet(self.css)
