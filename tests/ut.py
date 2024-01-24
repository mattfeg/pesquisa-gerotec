from unittest import TestCase
import unittest


class UtTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_(self):
        self.fail("Unit test ended")


if __name__ == '__main__':
    unittest.main()
