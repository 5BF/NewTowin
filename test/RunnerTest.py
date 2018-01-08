import unittest
import Testadd
import Testsub

suite=unittest.TestSuite()
suite.addTest(Testadd.TestAdd("addtest1"))
suite.addTest(Testadd.TestAdd("addtest2"))
suite.addTest(Testsub.TestSub("Testsub1"))
suite.addTest(Testsub.TestSub("Testsub2"))

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)