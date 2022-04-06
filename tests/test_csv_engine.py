import unittest
import pathlib

class TestCsv(unittest.TestCase):

    def test_setUpData(self):
        path = pathlib.Path("tests/data/dataset_test.csv")
        self.assertEquals((str(path), path.is_file()), (str(path), True))

if __name__ == '__main__':
    unittest.main()