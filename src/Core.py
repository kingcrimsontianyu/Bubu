#!/usr/bin/env python3

from enum import Enum
import sys
import os
import json
import os.path

#------------------------------------------------------------
# each blob is a dictionary
#------------------------------------------------------------
class BUBlob:
    def __init__(self, word = "", note = "", type = "word"):
        self.blobDict = dict()
        self.blobDict["word"] = word
        self.blobDict["note"] = note
        self.blobDict["type"] = type

    def Show(self):
        for key, value in self.blobDict.items():
            print("    ", key, ":", value)

#------------------------------------------------------------
# raw data is a list of blobs
#------------------------------------------------------------
class BUData:
    def __init__(self):
        self.dataPath = os.path.join(os.getcwd(), "data", "bubu.data")
        self.rawData = list()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Show(self):
        for item in self.rawData:
            print("-->")
            item.Show()

#------------------------------------------------------------
#------------------------------------------------------------
class BUEncoder(json.JSONEncoder):
    #------------------------------------------------------------
    # obj is a BUBlob in the list
    #------------------------------------------------------------
    def default(self, obj):
        if isinstance(obj, BUBlob):
            return obj.blobDict # return a dict, which is serializable
        else:
            sys.exit("BUEncoder(): wrong data.")

#------------------------------------------------------------
#------------------------------------------------------------
class BUDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook = self.BUDecodeMethod)

    #------------------------------------------------------------
    # obj is a BUBlob in the list
    #------------------------------------------------------------
    def BUDecodeMethod(self, obj):
        result = BUBlob()
        result.blobDict = obj
        return result

#------------------------------------------------------------
#------------------------------------------------------------
class BUCore:
    def __init__(self):
        self.buData = BUData()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ShowSystemInfo(self):
        print("--> python version\n    ", sys.version)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def WriteToFile(self):
        # cls specifies user-defined JSONEncoder subclass
        with open(self.buData.dataPath, 'w') as outfile:
            json.dump(self.buData.rawData, outfile, sort_keys=True, indent=4, cls=BUEncoder)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def WriteTestToFile(self):
        self.buData.rawData.append(BUBlob("godspeed", "a prosperous journey", "word"))
        self.buData.rawData.append(BUBlob("godspeed", "a prosperous journey", "word"))
        self.buData.rawData.append(BUBlob("lug", "drag or carry sth with great effort", "word"))

        # cls specifies user-defined JSONEncoder subclass
        with open(self.buData.dataPath, 'w') as outfile:
            json.dump(self.buData.rawData, outfile, sort_keys=True, indent=4, cls=BUEncoder)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ReadFromFile(self):
        if os.path.exists(self.buData.dataPath):
            with open(self.buData.dataPath, 'r') as infile:
                # cls specifies user-defined JSONDecoder subclass
                self.buData.rawData = json.load(infile, cls=BUDecoder)
        else:
            print("--> warning: " + self.buData.dataPath + " does not exist and will be created.")

    #------------------------------------------------------------
    #------------------------------------------------------------
    def GetRawData(self):
        return self.buData.rawData

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Show(self):
        self.buData.Show()

