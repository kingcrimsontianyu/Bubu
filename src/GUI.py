#!/usr/bin/env python3

import PySide
from PySide import QtCore, QtGui
import sys
import os
from MainWindow import BUMainWindow
from GUIdata import BUguiData
import Core

#------------------------------------------------------------
#------------------------------------------------------------
class BUgui:
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self, core):
        self.m_data = BUguiData(core)
        self.Initialize()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Initialize(self):
        self.m_data.app = QtGui.QApplication(sys.argv)
        self.m_data.desktopGeometry = self.GetDesktopGeometry()
        self.m_data.screenCenter = (self.m_data.desktopGeometry.width() / 2.0, self.m_data.desktopGeometry.height() / 2.0)

        #******************************
        # font
        #******************************
        self.m_data.rootDir = os.getcwd()
        self.m_data.dataDir = os.path.join(self.m_data.rootDir, "data")
        self.m_data.fontDir = os.path.join(self.m_data.dataDir, "font", "CenturyGothic")
        self.m_data.fontData = QtGui.QFontDatabase()
        for file in os.listdir(self.m_data.fontDir):
            if file.endswith(".ttf"):
                print(os.path.join(self.m_data.fontDir, file))
                self.m_data.fontData.addApplicationFont(os.path.join(self.m_data.fontDir, file))
        #******************************
        # picture
        #******************************
        self.m_data.pictureDir = os.path.join(self.m_data.dataDir, "pic")

        self.m_data.mainWindow = BUMainWindow(self.m_data)

        self.m_data.core.ShowSystemInfo()
        self.ShowSystemInfo()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Loop(self):
        # enter main event loop and wait until exit() is called
        sys.exit(self.m_data.app.exec_())

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ShowSystemInfo(self):
        print("--> pyside version\n    ", PySide.__version__)

        temp = QtGui.QFontDatabase()
        print("--> system font families\n", temp.families())

    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def GetDesktopGeometry(self):
        desktopWidget = QtGui.QApplication.desktop()
        primaryScreenIdx = desktopWidget.primaryScreen()
        primaryScreen = desktopWidget.screen()
        return QtGui.QDesktopWidget.screenGeometry(primaryScreen)






