#coding=GBK 

import unittest
from testRecommend import testRecommend

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testRecommend)
    unittest.TextTestRunner(verbosity=2).run(suite)