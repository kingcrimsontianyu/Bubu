#!/usr/bin/env python3

from PySide import QtCore, QtGui
import os
# from GUI import BUgui # warning: mutual inclusion

#------------------------------------------------------------
#------------------------------------------------------------
class BUPlainTextEdit(QtGui.QPlainTextEdit):
    #------------------------------------------------------------
    #------------------------------------------------------------
    def __init__(self):
        super().__init__()

        # css
        self.css = "QPlainTextEdit {background-color: #323232;"\
                                    "color: #ffffff;"\
                                    "font-size: 20px;"\
                                    "font-weight: regular;"\
                                    "font-family: Consolas, sans-serif}"

        self.setStyleSheet(self.css)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def keyPressEvent(self, event):
        # change tab to 4 space characters
        if event.key() == QtCore.Qt.Key_Tab:
            # create a key event that is still a tab key being pressed but yields four space characters
            event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress, QtCore.Qt.Key_Tab, QtCore.Qt.NoModifier, text="    ")
            super().keyPressEvent(event)
        else:
            super().keyPressEvent(event)
