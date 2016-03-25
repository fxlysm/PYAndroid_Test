__author__ = 'Lambert Liu'

import unittest
import time
from uiautomator import device as d


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_run_calculator(self):
        print("Run Calculator")
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)
        d(description="Apps",className="android.widget.TextView").click()
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()
