import unittest
from Roller import Roller

class TestRoller(unittest.TestCase):
    """docstring for TestRoller."""

    def test_OneDOne(self):
        testRoller = Roller((1, 1))
        self.assertEqual(testRoller.roll(), 1)

    def test_TwentyDTwenty(self):
        testRoller = Roller((20, 20))
        self.assertGreaterEqual(testRoller.roll(), 20)
        self.assertLessEqual(testRoller.roll(), 400)




if __name__ == '__main__':
    unittest.main()
