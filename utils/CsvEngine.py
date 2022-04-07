from setuptools import setup
import csv

from utils.BaseEngine import BaseEngine


class CsvEngine(BaseEngine):

    def __init__(self, dataNm, testNm) -> None:
        super().__init__()
        self.setDataFileName(dataNm) 
        self.setTestFileName(testNm)

    def createDocument(self, flType):
        self.setupTestFile(flType)
    
    def destroyDocument(self):
        self.deleteFile()

    def writeRow(self, content, choice):
        if(int(choice) == 1):
            self.setFileNm(self.getDataFileName())
        else:
            self.setFileNm(self.getTestFileName())

        
        f = open(self.getFileNm(), 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(content)
        f.close()


    def readLines(self, choice):
        if(int(choice) == 1):
            self.setFileNm(self.getDataFileName())
        else:
            self.setFileNm(self.getTestFileName())
        finalData = [] 
        with open(self.getFileNm(), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                finalData.append(row)
        return finalData