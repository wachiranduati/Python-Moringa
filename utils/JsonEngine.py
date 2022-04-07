from utils.BaseEngine import BaseEngine

class JsonEngine(BaseEngine):

    def __init__(self, dataNm, testNm) -> None:
        super().__init__()
        self.setDataFileName(dataNm) 
        self.setTestFileName(testNm)
    
    def createDocument(self, flType):
        self.setupTestFile(flType)
    
    def destroyDocument(self):
        self.deleteFile()