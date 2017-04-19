#!/usr/bin/env python3

from PySide import QtCore, QtGui
import sys
import os
from GUIdata import BUguiData
from Button import BUPushButton
from Text import BUPlainTextEdit
from ScrollArea import BUScrollArea
from Table import BUTableWidget
from Table import BUTableWidgetItem
from Tree import BUTreeWidget
from MessageBox import BUMessageBox
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
        self.m_button_sort = BUPushButton("sort")
        self.m_button_save = BUPushButton("save")
        self.m_button_save.setEnabled(False)
        self.m_button_backup = BUPushButton("back up")
        self.m_button_exit = BUPushButton("exit")
        hbox.addWidget(self.m_button_add)
        hbox.addWidget(self.m_button_sort)
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
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
            self.m_table.setItem(counter, 0, item)
            counter += 1

        hbox = QtGui.QHBoxLayout()
        self.m_text = BUPlainTextEdit()
        if len(self.m_raw) != 0:
            self.m_text.setPlainText(self.m_raw[0].blobDict["note"])
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
        self.m_table.cellClicked.connect(self.ShowText)
        self.m_button_add.clicked.connect(self.AddTableItem)
        self.m_button_save.clicked.connect(self.SaveToDisk)
        self.m_button_exit.clicked.connect(self.Quit)
        self.m_button_sort.clicked.connect(self.Sort)
        self.m_text.textChanged.connect(self.SaveToMemoryIfChanged)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ShowText(self, row, column):
        self.m_data.currentRow = row
        entry = self.m_raw[self.m_data.currentRow]
        self.m_text.setPlainText(entry.blobDict["note"])

    #------------------------------------------------------------
    #------------------------------------------------------------
    def AddTableItem(self):
        blob = Core.BUBlob()
        self.m_raw.insert(0, blob)
        self.m_table.insertRow(0)

        item = BUTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
        self.m_table.setItem(0, 0, item)

        self.m_data.anyThingChanged = True
        self.m_button_save.setEnabled(True)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def SaveToDisk(self):
        self.m_data.core.WriteToFile()
        msg = BUMessageBox(self.m_data)
        msg.setText("The data have been saved.")
        msg.exec_()

        # reset
        self.m_data.anyThingChanged = False
        self.m_button_save.setEnabled(False)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def SaveToMemoryIfChanged(self):
        # the data are considered user-changed if
        # --- m_text has focus
        # --- m_text content has been changed
        if self.m_text.hasFocus():
            print("--> text changed.", self.m_text.toPlainText())
            self.m_raw[self.m_data.currentRow].blobDict["note"] = self.m_text.toPlainText()

            self.m_data.anyThingChanged = True
            self.m_button_save.setEnabled(True)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Quit(self):
        if self.m_data.anyThingChanged:
            print("things changed")
        else:
            self.m_data.app.quit()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Sort(self):
        # sort raw data
        self.m_raw.sort(key=lambda x: x.blobDict["word"])

        # update table and text
        counter = 0
        for entry in self.m_raw:
            item = self.m_table.item(counter, 0)
            item.setText(entry.blobDict["word"])
            counter += 1

        if len(self.m_raw) != 0:
            self.m_text.setPlainText(self.m_raw[0].blobDict["note"])




