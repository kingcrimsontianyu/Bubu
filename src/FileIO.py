#!/usr/bin/env python3

import sys
import Common
from Common import BUBlob
import json
import os.path

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
class BUFileIO:
    def __init__(self, buData):
        self.buData = buData

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ShowSystemInfo(self):
        print("--> python\n    ", sys.version)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def WriteToFile(self):
        self.buData.coreData["godspeed"] = BUBlob("a prosperous journey", "word")
        self.buData.coreData["lug"] = BUBlob("drag or carry sth with great effort", "word")

        # cls specifies user-defined JSONEncoder subclass
        with open(self.buData.dataPath, 'w') as outfile:
            json.dump(self.buData.coreData, outfile, sort_keys=True, indent=4, cls=BUEncoder)

    #------------------------------------------------------------
    #------------------------------------------------------------
    def ReadFromFile(self):
        if os.path.exists(self.buData.dataPath):
            with open(self.buData.dataPath, 'r') as infile:
                # cls specifies user-defined JSONDecoder subclass
                self.buData.coreData = json.load(infile, cls=BUDecoder)
        else:
            # initialize data
            self.buData.coreData = dict()



