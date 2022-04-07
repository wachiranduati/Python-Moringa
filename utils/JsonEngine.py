import pathlib
import os
import json

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

    def writeRow(self, content, choice):
        if(int(choice) == 1):
            self.file = self.data_filename
        else:
            self.file = self.test_filename

        f = open(self.file, 'w', newline='')
        writer = json.dump(content ,f)
        writer.writerow(content)
        f.close()

    def readLines(self, choice):
        if(int(choice) == 1):
            self.file = self.data_filename
        else:
            self.file = self.test_filename

        f = open(self.file, 'r')
        reader = json.load(f)
        return reader


    def deleteFile(self):
        path = pathlib.Path(self.file)
        if(path.is_file()):
            os.remove(self.file)
        else:
            print('The file does not exist')