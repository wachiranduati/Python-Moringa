import unittest
import pathlib

from utils.JsonEngine import JsonEngine

class TestJson(unittest.TestCase):
    
    path = pathlib.Path("tests/data/dataset_test.json")
    x =  JsonEngine()

    def setUp(self) -> None:
        self.x.setupTestFile(0)
        return super().setUp()

    def test_file_exists(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))

    def test_write_data(self):
        self.assertTrue(False)    

    def tearDown(self) -> None:
        self.x.deleteFile()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()