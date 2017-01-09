#coding=GBK 

import unittest
from testShowApp import testShowApp

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testShowApp)
    unittest.TextTestRunner(verbosity=2).run(suite)