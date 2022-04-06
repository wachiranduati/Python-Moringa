from setuptools import setup


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
        f.write("test")
        f.close()