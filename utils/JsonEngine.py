import pathlib
import os
import json

from utils.BaseEngine import BaseEngine

class JsonEngine(BaseEngine):

    def __init__(self, dataNm, testNm) -> None:
        super().__init__()
        self.setDataFileName(dataNm) 
        self.setTestFileName(testNm)
        print("{0}, {1}".format(dataNm, testNm))
    
    def createDocument(self, flType):
        self.setupTestFile(flType)
    
    def destroyDocument(self):
        self.deleteFile()