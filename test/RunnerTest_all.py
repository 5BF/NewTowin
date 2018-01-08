import unittest

def creatsuite():
    testunit=unittest.TestSuite()
    test_dir=("C:\\Users\\Administrator\\PycharmProjects\\untitled2\\test")
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test*.py',top_level_dir=None)
    for test_case in discover:
        testunit.addTests(test_case)
        print (testunit)
    return (test_case)
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(creatsuite())


