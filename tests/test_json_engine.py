import unittest
import pathlib

from utils.JsonEngine import JsonEngine

class TestJson(unittest.TestCase):
    
    path = pathlib.Path("tests/data/dataset_test.json")
    x =  JsonEngine()
    data = [{"id":1,"first_name":"Yvor","last_name":"McNalley","email":"ymcnalley0@angelfire.com","gender":"Male","ip_address":"160.92.169.74"},
    {"id":2,"first_name":"Amber","last_name":"Loudyan","email":"aloudyan1@google.com.hk","gender":"Female","ip_address":"12.206.65.11"},]

    def setUp(self) -> None:
        self.x.setupTestFile(0)
        return super().setUp()

    def test_file_exists(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))

    def test_write_data(self):
        self.x.writeRow(self.data, 0)
        self.assertTrue(False)    

    def tearDown(self) -> None:
        # self.x.deleteFile()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()