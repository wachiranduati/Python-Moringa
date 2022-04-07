import unittest
import pathlib

from utils.CsvEngine import CsvEngine



class TestCsv(unittest.TestCase):

    data_filename = "data/dataset.csv"
    test_filename = "tests/data/dataset_test.csv"
    file = ""
    path = pathlib.Path("tests/data/dataset_test.csv")
    x = CsvEngine(data_filename, test_filename)
    csvHeader = ["id","first_name","last_name","email","gender","ip_address"]
    csvLine1 = [1,"Arman","Smaile","asmaile0@nydailynews.com","Male","251.7.174.204"]
    csvLine2 = [2,"Sula","Revel","srevel1@umich.edu","Female","43.84.236.218"]


    def setUp(self) -> None:
        self.x.createDocument(0)
        return super().setUp()

    def test_setUpData(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))

    def test_writeData(self):
        self.x.writeRow(self.csvHeader, 0)
        # self.x.writeRow(self.csvLine1, 0)
        # self.x.writeRow(self.csvLine2, 0)
        readCsv = self.x.readLines(0)
        # //return iterable
        readHeadline = ""
        readLine2 = ""
        readLine3 = ""
        count = 0
        for i in readCsv:
            if(count == 0):
                readHeadline = i
            elif(count == 1):
                readLine2 = i
            else:
                readLine3 = i
            count += 1

        self.assertEqual(self.csvHeader, readHeadline)
        # self.assertEqual(self.csvLine1, readLine2)
        # self.assertEqual(self.csvLine2, readLine3)

    def tearDown(self) -> None:
        self.x.destroyDocument()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()