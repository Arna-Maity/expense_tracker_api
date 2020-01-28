import unittest
import spent

class testSpent(unittest.TestCase):
    def test_sample(self):
        print("Running Sample Test Case")
        self.assertEqual(3+4,7)


if __name__ == '__main__':
    unittest.main()