#!/usr/bin/env python3

from PySide import QtCore, QtGui
import sys
import os
from GUIdata import BUguiData
from Button import BUPushButton
from TextEdit import BUTextEdit
from ScrollArea import BUScrollArea
from Table import BUTableWidget
from Table import BUTableWidgetItem
from Tree import BUTreeWidget
import Core

#------------------------------------------------------------
#------------------------------------------------------------
class BUMainWindow(QtGui.QMainWindow):
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self, guiData):
        super().__init__()
        self.m_button_add = None
        self.m_button_save = None
        self.m_table = None
        self.m_text = None

        self.m_data = guiData
        self.m_raw = self.m_data.GetRawData() # alias for a simplified name

        self.Initialize()
        self.Delegate()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Initialize(self):
        self.setWindowTitle("bubu")
        self.setMinimumSize(320,320)
        self.resize(1200,640)
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.m_data.pictureDir, 'bubu.png')))

        hbox = QtGui.QHBoxLayout()
        self.m_button_add = BUPushButton("add word")
        self.m_button_save = BUPushButton("save")
        self.m_button_backup = BUPushButton("back up")
        self.m_button_exit = BUPushButton("exit")
        hbox.addWidget(self.m_button_add)
        hbox.addWidget(self.m_button_save)
        hbox.addWidget(self.m_button_backup)
        hbox.addWidget(self.m_button_exit)
        buttonWidget = QtGui.QWidget()
        buttonWidget.setLayout(hbox)

        self.m_table = BUTableWidget()
        self.m_table.setRowCount(len(self.m_raw))
        self.m_table.setColumnCount(1)
        self.m_table.horizontalHeader().hide()
        self.m_table.verticalHeader().hide()
        self.m_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        # self.m_table.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.m_table.setColumnWidth(0, 10)
        self.m_table.setCornerButtonEnabled(False)

        counter = 0
        for entry in self.m_raw:
            item = BUTableWidgetItem()
            item.setText(entry.blobDict["word"])
            item.setFlags(~QtCore.Qt.ItemIsEditable)
            self.m_table.setItem(counter, 0, item)
            counter += 1

        hbox = QtGui.QHBoxLayout()
        self.m_text = BUTextEdit()
        hbox.addWidget(self.m_table)
        hbox.addWidget(self.m_text)
        hbox.setStretchFactor(self.m_table, 1)
        hbox.setStretchFactor(self.m_text, 3)
        textWidget = QtGui.QWidget()
        textWidget.setLayout(hbox)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(buttonWidget)
        vbox.addWidget(textWidget)

        helper = QtGui.QWidget()
        helper.setLayout(vbox)
        self.setCentralWidget(helper)

        self.css = "QMainWindow {background-color: #323232}"
        self.setStyleSheet(self.css)

        self.show()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Delegate(self):
        self.m_table.cellClicked.connect(self.ChangeText)
        self.m_button_add.clicked.connect(self.AddTableItem)
        # self.m_button_save.clicked
        self.m_button_exit.clicked.connect(self.Quit)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ChangeText(self, row, column):
        entry = self.m_raw[row]
        self.m_text.setText(entry.blobDict["note"])

    #------------------------------------------------------------
    #------------------------------------------------------------
    def AddTableItem(self):
        blob = Core.BUBlob("", "", "word")
        self.m_raw.insert(0, blob)
        self.m_table.insertRow(0)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Quit(self):
        self.m_data.app.quit()
