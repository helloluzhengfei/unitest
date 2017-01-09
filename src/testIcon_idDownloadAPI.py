#coding=GBK  

import unittest
from testIcon_idDownload import testIcon_idDownload

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testIcon_idDownload)
    unittest.TextTestRunner(verbosity=2).run(suite)