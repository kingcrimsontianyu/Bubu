#!/usr/bin/env python3

# --> json reference: https://www.w3schools.com/js/js_json_syntax.asp
#         Curly braces hold objects
#         Square brackets hold arrays
#
# --> python json reference: https://docs.python.org/3.4/library/json.html
#         note that a json object translates to a python dictionary
#
# --> custom encoder and decoder
#         json.JSONEncoder.default(obj) here obj refers to each individual value of the dictionary!!!
#
# --> internal data structure is a dict: {key1: value1, key2: value2}
#         key: string, a word or phrase
#         value: BUBlob
#             note: string.
#             type: string. options: word, phrase
#
# --> api
#         load():  read file into python object
#         loads(): convert string into python object
#         dump():  write python object into file
#         dumps(): write python object into string

import sys
from enum import Enum

#------------------------------------------------------------
#------------------------------------------------------------
class BUBlob:
    def __init__(self, note = "", type = "word"):
        self.note = note
        self.type = type

#------------------------------------------------------------
#------------------------------------------------------------
class BUData:
    def __init__(self):
        self.dataPath = "../data/bubu.data"
        self.coreData = dict()

    #------------------------------------------------------------
    #------------------------------------------------------------
    def Show(self):
        for key, value in self.coreData.items():
            print("--> ", key)
            print("    ", value.note)
            print("    ", value.type)




