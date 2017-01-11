#coding=GBK  

import unittest
from testFindApp import testFindApp

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testFindApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
