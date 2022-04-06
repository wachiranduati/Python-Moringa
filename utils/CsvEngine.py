from setuptools import setup
import os
import pathlib


class CsvEngine:
    
    data_filename = "data/dataset.csv"
    test_filename = "tests/data/dataset_test.csv"
    file = ""

    # def __init__(self, option):
    #     self.setupTestFile(option)

    def setupTestFile(self, choice):
        if(int(choice) == 1):
            self.file = self.data_filename
        else:
            self.file = self.test_filename
        
        self.createFile(self.file)

    def createFile(self, path):
        f = open(path, "w")
        f.close()

    def deleteFile(self):
        path = pathlib.Path(self.file)
        if(path.is_file()):
            os.remove(self.file)
        else:
            print('The file does not exist')