import pathlib
import os
import json

class BaseEngine:
    __data_filename = ""
    __test_filename = ""
    __file = ""

    def setDataFileName(self, flnm):
        self.__data_filename = flnm

    def getDataFileName(self):
        return self.__data_filename

    def setTestFileName(self, tstfilename):
        self.__test_filename = tstfilename

    def getTestFileName(self):
        return self.__test_filename

    def setFileNm(self, newFlnm):
        self.__file = newFlnm

    def getFileNm(self):
        return self.__file

    def setupTestFile(self, choice):
        if(int(choice) == 1):
            self.__file = self.__data_filename
        else:
            self.__file = self.__test_filename
        
        self.createFile(self.__file)
    
    def createFile(self, path):
        f = open(path, "w")
        f.close()

    def writeRow(self, content, choice):
        if(int(choice) == 1):
            self.__file = self.__data_filename
        else:
            self.__file = self.__test_filename

        with open(self.__file, 'a', newline='') as f:
            json.dump(content, f)
        

    def readLines(self, choice):
        if(int(choice) == 1):
            self.__file = self.__data_filename
        else:
            self.__file = self.__test_filename

        f = open(self.__file, 'r')
        reader = json.load(f)
        return reader


    def deleteFile(self):
        path = pathlib.Path(self.__file)
        if(path.is_file()):
            os.remove(self.__file)
        else:
            print('The file does not exist')