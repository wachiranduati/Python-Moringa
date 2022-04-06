import unittest
import pathlib

from utils.CsvEngine import CsvEngine



class TestCsv(unittest.TestCase):

    def setUp(self) -> None:
        x = CsvEngine()
        x.setupTestFile(0)
        return super().setUp()

    def test_setUpData(self):
        path = pathlib.Path("tests/data/dataset_test.csv")
        self.assertEquals((str(path), path.is_file()), (str(path), True))

if __name__ == '__main__':
    unittest.main()