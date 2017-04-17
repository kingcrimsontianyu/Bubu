#!/usr/bin/env python3

import Common
import FileIO

#------------------------------------------------------------
#------------------------------------------------------------
if __name__ == "__main__":

    # instantiate
    buData = Common.BUData() # core data instance
    fileIO = FileIO.BUFileIO(buData) # file IO instance

    fileIO.ShowSystemInfo()

    fileIO.ReadFromFile()

    # fileIO.WriteToFile()

    buData.Show()