import unittest
import pathlib

from utils.CsvEngine import CsvEngine



class TestCsv(unittest.TestCase):

    path = pathlib.Path("tests/data/dataset_test.csv")
    x = CsvEngine()
    csvHeader = ["id","first_name","last_name","email","gender","ip_address"]
    csvLine1 = [1,"Arman","Smaile","asmaile0@nydailynews.com","Male","251.7.174.204"]
    csvLine2 = [2,"Sula","Revel","srevel1@umich.edu","Female","43.84.236.218"]


    def setUp(self) -> None:
        self.x.setupTestFile(0)
        return super().setUp()

    def test_setUpData(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))

    def test_writeData(self):
        # open new file "empty"
        # write one line
        # read one line and 
        # comma seperated delimiter
        self.x.writeRow(self.csvHeader)
        self.x.writeRow(self.csvLine1)
        self.x.writeRow(self.csvLine2)
        # write
        readCsv = self.x.readLines()
        # //return iterable
        readHeadline = ""
        readLine2 = ""
        readLine3 = ""
        for i in range(3):
            if(i == 0):
                readHeadline = readCsv[i]
            elif(i == 1):
                readLine2 = readCsv[i]
            else:
                readLine3 = readCsv[i]

        self.assertEqual(self.csvHeader, readHeadline)
        self.assertEqual(self.csvLine1, readLine2)
        self.assertEqual(self.csvLine2, readLine3)

    def tearDown(self) -> None:
        self.x.deleteFile()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()