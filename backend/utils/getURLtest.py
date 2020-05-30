import unittest
from getURL import getURL


class TestStringMethods(unittest.TestCase):

    def test_getURL(self):
        self.assertEqual(getURL("https://globalnews.ca/news/7007185/coronavirus-exposure-warning-covid19-halifax/"), 'https://www.canadahelps.org/en/donate-to-coronavirus-outbreak-response/')

    def sample_getURL(self):
        PLACEHOLDER_INPUT_URL = 'https://globalnews.ca/news/7007185/coronavirus-exposure-warning-covid19-halifax/'
        PLACEHOLDER_OUTPUT_URL = 'https://www.canadahelps.org/en/donate-to-coronavirus-outbreak-response/'
        self.assertEqual(getURL(PLACEHOLDER_INPUT_URL),
                         PLACEHOLDER_OUTPUT_URL)


if __name__ == "__main__":
    unittest.main()

# how to run this test
# cd in to utils directory
# python -m unittest getURLtest.py
