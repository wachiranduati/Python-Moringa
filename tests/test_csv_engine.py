import unittest
import pathlib

from utils.CsvEngine import CsvEngine



class TestCsv(unittest.TestCase):

    path = pathlib.Path("tests/data/dataset_test.csv")
    x = CsvEngine()


    def setUp(self) -> None:
        self.x.setupTestFile(0)
        return super().setUp()

    def test_setUpData(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))

    def tearDown(self) -> None:
        self.x.deleteFile()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()