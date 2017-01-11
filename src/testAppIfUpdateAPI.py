#coding=GBK 

import unittest
from testAppIfUpdate import testAppIfUpdate

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testAppIfUpdate)
    unittest.TextTestRunner(verbosity=2).run(suite)