#coding=GBK 

import unittest
from testLastUpdate import testLastUpdate

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testLastUpdate)
    unittest.TextTestRunner(verbosity=2).run(suite)