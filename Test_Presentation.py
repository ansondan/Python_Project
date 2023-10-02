import unittest
def palindrome(mystr):
    return mystr == mystr[::-1]


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEquals(palindrome("12321"), True)


if __name__ == '__main__':
    unittest.main()