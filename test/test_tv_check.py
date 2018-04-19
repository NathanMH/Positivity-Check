import time
import unittest
import os
from tv_check.tv_check import load_csv

csv_test_loc = os.getcwd() + "\\test\\the-office-lines-scripts-test.csv" # Windows
characters_test = ["Michael", "Jim"]

class TestTv(unittest.TestCase):
    def test_load_csv(self):
        load_csv(csv_test_loc)

if __name__ == '__main__':
    unittest.main()

    # t1 = time.clock()
    # t2 = time.clock()
    # print("Time: " + '{:.5}'.format(str(t2 - t1)))