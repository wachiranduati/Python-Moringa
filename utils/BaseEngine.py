import pathlib
import os
import json

class BaseEngine:
    __data_filename = ""
    __test_filename = ""
    file = ""

    def setDataFileName(self, flnm):
        self.__data_filename = flnm

    def getDataFileName(self):
        return self.__data_filename

    def setTestFileName(self, tstfilename):
        self.__test_filename = tstfilename

    def getTestFileName(self):
        return self.__test_filename

    def setupTestFile(self, choice):
        if(int(choice) == 1):
            self.file = self.__data_filename
        else:
            self.file = self.__test_filename
        
        self.createFile(self.file)
    
    def createFile(self, path):
        f = open(path, "w")
        f.close()

    def writeRow(self, content, choice):
        if(int(choice) == 1):
            self.file = self.__data_filename
        else:
            self.file = self.__test_filename

        f = open(self.file, 'w', newline='')
        json.dump(content ,f)
        f.close()

    def readLines(self, choice):
        if(int(choice) == 1):
            self.file = self.__data_filename
        else:
            self.file = self.__test_filename

        f = open(self.file, 'r')
        reader = json.load(f)
        return reader


    def deleteFile(self):
        path = pathlib.Path(self.file)
        if(path.is_file()):
            os.remove(self.file)
        else:
            print('The file does not exist')