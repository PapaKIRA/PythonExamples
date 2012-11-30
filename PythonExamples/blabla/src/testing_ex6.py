'''
Created on Nov 22, 2012

@author: Andrei
'''
import unittest
import ex_6

class Test(unittest.TestCase):


    def test_do_minus(self):
        self.assertEqual(10, ex_6.do_minus(20, 10), "do_minus() returned a wrong result")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()