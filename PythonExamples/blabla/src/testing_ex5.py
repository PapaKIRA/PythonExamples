'''
Created on Nov 20, 2012

@author: Andrei
'''
import unittest
import ex_5

class Test(unittest.TestCase):


    def test_do_plus(self):
        self.assertEqual(5, ex_5.do_plus(2, 3), "do_plus() returned a wrong result")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()