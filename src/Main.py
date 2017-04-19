#!/usr/bin/env python3

from PySide import QtCore, QtGui
import Core
import GUI

#------------------------------------------------------------
#------------------------------------------------------------
if __name__ == "__main__":
    buCore = Core.BUCore()
    buCore.ReadFromFile()

    # add artificial data
    for i in range(100):
        key = str(i)
        blob = Core.BUBlob(str(i), str(i) + "    The Witcher 3: Wild Hunt was met with widespread critical acclaim upon its release, with praise directed toward its gameplay, narrative, world design, combat and visuals. It became the most awarded game of 2015, receiving numerous Game of the Year awards from various gaming publications, critics, and award events, and is regarded by many to be one of the greatest role-playing games of all time. The game was also a commercial success, selling over six million copies within six weeks of its release. Two expansion packs for the game were also released, Hearts of Stone and Blood and Wine, with both receiving further critical acclaim. A Game of the Year edition, which includes the base game, its two expansion packs, and all additional downloadable content, was released in August 2016.")
        buCore.GetRawData().append(blob)

    gui = GUI.BUgui(buCore)
    gui.Loop()