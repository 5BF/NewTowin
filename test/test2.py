from selenium import  webdriver
import unittest
from count import Count


class TestCount(unittest.TestCase):

    def setUp(self):
        #pass
        self.j = Count(2, 3)

    def test_add(self):
        #self.j=Count(2,3)
        self.add=self.j.add()
        self.assertEqual(self.add,5,msg='相加不等于5')

    def test_add2(self):
        self.j=Count(2.3,2.5)
        self.add=self.j.add()
        self.assertEqual(self.add,6,msg='小数相加不等于6')

    def tearDown(self):
        pass

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add2"))

    runner=unittest.TextTestRunner()
    runner.run(suite)
