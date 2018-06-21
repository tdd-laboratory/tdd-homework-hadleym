import unittest
import library

NUM_CORPUS = '''
On the 5th of May every year, Mexicans celebrate Cinco de Mayo. This tradition
began in 1845 (the twenty-second anniversary of the Mexican Revolution), and
is the 1st example of a national independence holiday becoming popular in the
Western Hemisphere. (The Fourth of July didn't see regular celebration in the
US until 15-20 years later.) It is celebrated by 77.9% of the population--
trending toward 80.                                                                
'''

class TestCase(unittest.TestCase):

    # Helper function
    def assert_extract(self, text, extractors, *expected):
        actual = [x[1].group(0) for x in library.scan(text, extractors)]
        print('actual: '+ str(actual))
        print('expected: ' + str([x for x in expected]))
        self.assertEquals(str(actual), str([x for x in expected]))

    # First unit test; prove that if we scan NUM_CORPUS looking for mixed_ordinals,
    # we find "5th" and "1st".
    def test_mixed_ordinals(self):
        self.assert_extract(NUM_CORPUS, library.mixed_ordinals, '5th', '1st')

    # Second unit test; prove that if we look for integers, we find four of them.
    def test_integers(self):
        self.assert_extract(NUM_CORPUS, library.integers, '1845', '15', '20', '80')

    # Third unit test; prove that if we look for integers where there are none, we get no results.
    def test_no_integers(self):
        self.assert_extract("no integers", library.integers)

    # Test 2015-07-25 format extracts as date
    def test_dates(self):
        self.assert_extract("something 2015-12-25.", library.dates_iso8601, '2015-12-25')

    # Test that months greater than 12 are ignored as dates
    def test_no_dates(self):
        self.assert_extract("something 2015-13-25 not ending", library.dates_iso8601)

    def test_word_dates(self):
        self.assert_extract("something 25 Jan 2017.", library.dates_wordy, '25 Jan 2017')

if __name__ == '__main__':
    unittest.main()
