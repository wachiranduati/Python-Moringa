import pathlib
import os

class JsonEngine:
    data_filename = "data/dataset.json"
    test_filename = "tests/data/dataset_test.json"
    file = ""

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