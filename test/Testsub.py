from count2 import Count2
import unittest

class  TestSub(unittest.TestCase):
    def setUp(self):
        pass
    def Testsub1(self):
        self.j=Count2(10,20)
        self.sub=self.j.sub()
        self.assertEqual(self.sub,-10)
    def Testsub2(self):
        self.j=Count2(50,20)
        self.sub=self.j.sub()
        self.assertEqual(self.sub,30)

    def tearDown(self):
        pass
