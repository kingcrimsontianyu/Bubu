#!/usr/bin/env python3

from enum import Enum
import sys
import os
import json
import os.path

#------------------------------------------------------------
#------------------------------------------------------------
class BUBlob:
    def __init__(self, note = "", type = "word"):
        self.note = note
        self.type = type

    def Show(self):
        print("    ", self.note)
        print("    ", self.type)

#------------------------------------------------------------
#------------------------------------------------------------
class BUData:
    def __init__(self):
        self.dataPath = os.path.join(os.getcwd(), "data", "bubu.data")
        self.rawData = dict()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Show(self):
        for key, value in self.rawData.items():
            print("--> ", key)
            value.Show()

#------------------------------------------------------------
#------------------------------------------------------------
class BUEncoder(json.JSONEncoder):
    #------------------------------------------------------------
    # obj is the value in each (key, value) pair of the dict data
    #------------------------------------------------------------
    def default(self, obj):
        if isinstance(obj, BUBlob):
            serializable = [obj.note, obj.type]
            return serializable
        else:
            return json.JSONEncoder.default(self, obj)



#------------------------------------------------------------
#------------------------------------------------------------
class BUDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook = self.BUDecodeMethod)

    #------------------------------------------------------------
    # obj is the entire raw dict
    #------------------------------------------------------------
    def BUDecodeMethod(self, obj):
        result = dict()
        for key, value in obj.items():
            result[key] = BUBlob(value[0], value[1])
        return result


#------------------------------------------------------------
#------------------------------------------------------------
class BUCore:
    def __init__(self):
        self.buData = BUData()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ShowSystemInfo(self):
        print("--> python\n    ", sys.version)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def WriteToFile(self):
        self.buData.rawData["godspeed"] = BUBlob("a prosperous journey", "word")
        self.buData.rawData["lug"] = BUBlob("drag or carry sth with great effort", "word")

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
            sys.exit("--> " + self.buData.dataPath + " does not exist.")

    #------------------------------------------------------------
    #------------------------------------------------------------
    def GetRawData(self):
        return self.buData.rawData

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Show(self):
        self.buData.Show()

