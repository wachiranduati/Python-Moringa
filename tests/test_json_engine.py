import unittest
import pathlib

from utils.JsonEngine import JsonEngine

class TestJson(unittest.TestCase):
    data = "data/dataset.json"
    test = "tests/data/dataset_test.json"
    path = pathlib.Path("tests/data/dataset_test.json")
    x =  JsonEngine(data, test)
    data = {"id":2,"first_name":"Amber","last_name":"Loudyan","email":"aloudyan1@google.com.hk","gender":"Female","ip_address":"12.206.65.11"}

    def setUp(self) -> None:
        self.x.createDocument(0)
        return super().setUp()

    def test_file_exists(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))

    def test_write_data(self):
        self.x.writeRow(self.data, 0)
        dataRead = self.x.readLines(0)
        self.assertEqual(self.data, dataRead) 

    def tearDown(self) -> None:
        self.x.destroyDocument()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()