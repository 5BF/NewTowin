from count2 import Count2
import unittest

class  TestAdd(unittest.TestCase):
    def setUp(self):
        pass

    def addtest1(self):
        self.j=Count2(2,3)
        self.add=self.j.add()
        self.assertEqual(self.add,5)

    def addtest2(self):
        self.j=Count2(5,6)
        self.add=self.j.add()
        self.assertEqual(self.add,11)

    def tearDown(self):
        pass