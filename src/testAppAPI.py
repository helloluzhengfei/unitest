#coding=GBK 

import unittest
from testApp import testApp

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testApp)
    unittest.TextTestRunner(verbosity=2).run(suite)