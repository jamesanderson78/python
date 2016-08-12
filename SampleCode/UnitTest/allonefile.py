import unittest

# Here's our function under test.
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests" for the function under test, all in one file.
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))
        
    def testThree(self):
        self.assertEqual(IsOdd(3), True)

def main():
    unittest.main()

if __name__ == '__main__':
    main()