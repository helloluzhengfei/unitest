#coding=GBK  

import unittest
from testCatlist import testCatlist

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testCatlist)
    unittest.TextTestRunner(verbosity=2).run(suite)
