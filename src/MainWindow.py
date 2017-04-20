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
        hbox.addWidget(self.m_button_add)
        hbox.addWidget(self.m_button_sort)
        hbox.addWidget(self.m_button_save)
        hbox.addWidget(self.m_button_backup)
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
        self.m_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

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
        self.m_table.itemChanged.connect(self.SaveChangedTableToMemory)
        self.m_table.customContextMenuRequested.connect(self.RemoveTableItem)
        self.m_button_add.clicked.connect(self.AddTableItem)
        self.m_button_save.clicked.connect(self.SaveToDisk)
        self.m_button_sort.clicked.connect(self.Sort)
        self.m_text.textChanged.connect(self.SaveChangedTextToMemory)

    #------------------------------------------------------------
    # right click automatically triggers cellClicked
    #------------------------------------------------------------
    def RemoveTableItem(self, position):
        menu = QtGui.QMenu()
        rmAction = menu.addAction("remove")
        action = menu.exec_(self.m_table.mapToGlobal(position))
        if action == rmAction:
            self.m_raw.pop(self.m_data.currentRow)
            self.m_table.removeRow(self.m_data.currentRow)
            self.m_data.anyThingChanged = True
            self.m_button_save.setEnabled(True)

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

        # reset
        self.m_data.anyThingChanged = False
        self.m_button_save.setEnabled(False)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def SaveChangedTableToMemory(self):
        p = self.m_table.item(self.m_data.currentRow, 0)
        newText = p.text()
        self.m_raw[self.m_data.currentRow].blobDict["word"] = newText
        print("--> table changed.", newText, "current row: ", self.m_data.currentRow)

        self.m_data.anyThingChanged = True
        self.m_button_save.setEnabled(True)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def SaveChangedTextToMemory(self):
        # the text data are considered user-changed if
        # --- m_text has focus
        # --- m_text content has been changed
        if self.m_text.hasFocus():
            newText = self.m_text.toPlainText()
            self.m_raw[self.m_data.currentRow].blobDict["note"] = newText
            print("--> text changed.", newText)

            self.m_data.anyThingChanged = True
            self.m_button_save.setEnabled(True)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def closeEvent(self, event):
        print("--> closeEvent()")
        if self.m_data.anyThingChanged:
            msgBox = BUMessageBox(self.m_data)
            msgBox.setText("about to exit")
            msgBox.setInformativeText("Unsaved work. What now?")
            msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
            msgBox.setDefaultButton(QtGui.QMessageBox.Save)
            ret = msgBox.exec_()

            if ret == QtGui.QMessageBox.Save:
                self.SaveToDisk()
                super().closeEvent(event)
            elif ret == QtGui.QMessageBox.Discard:
                super().closeEvent(event)
            elif ret == QtGui.QMessageBox.Cancel:
                msgBox.close()
                event.ignore()
            else:
                pass
        else:
            super().closeEvent(event)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Sort(self):
        # sort raw data
        self.m_raw.sort(key=lambda x: x.blobDict["word"])

        # update table
        counter = 0
        for entry in self.m_raw:
            item = self.m_table.item(counter, 0)
            item.setText(entry.blobDict["word"])
            counter += 1

        # update text
        if len(self.m_raw) != 0:
            self.m_text.setPlainText(self.m_raw[0].blobDict["note"])




