import unittest
from getURL import getURL


class TestStringMethods(unittest.TestCase):
    def loop_testURL(self):
        INPUT_URLS = ['https://google.com']
        OUTPUT_URLS = ["google.com"]

        for input, output in zip(INPUT_URLS, OUTPUT_URLS):
            self.assertEqual(getURL(input), output)


if __name__ == "__main__":
    unittest.main()

# how to run this test
# cd in to utils directory
# python -m unittest getURLtest.py
