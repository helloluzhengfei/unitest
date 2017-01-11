#coding=GBK 

import unittest
from testAppCommentsList import testAppCommentsList

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testAppCommentsList)
    unittest.TextTestRunner(verbosity=2).run(suite)