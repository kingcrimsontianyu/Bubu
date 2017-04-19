#!/usr/bin/env python3

import Core

#------------------------------------------------------------
#------------------------------------------------------------
class BUguiData:
    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def __init__(self, core):
        self.app              = None
        self.desktopGeometry  = None
        self.screenCenter     = None
        self.rootDir          = None
        self.dataDir          = None
        self.fontDir          = None
        self.fontData         = None
        self.mainWindow       = None
        self.pictureDir       = None
        self.core             = core

        # status data
        self.currentRow       = 0
        self.anyThingChanged  = False

    #++++++++++++++++++++++++++++++
    #++++++++++++++++++++++++++++++
    def GetRawData(self):
        return self.core.GetRawData()