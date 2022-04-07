import unittest
import pathlib

class TestJson(unittest.TestCase):
    
    path = pathlib.Path("tests/data/dataset_test.json")

    def setUp(self) -> None:
        # //create the file
        return super().setUp()

    def test_file_exists(self):
        self.assertEqual((str(self.path), self.path.is_file()), (str(self.path), True))
        

    def tearDown(self) -> None:
        # delete the file
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()