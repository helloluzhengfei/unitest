#coding=GBK  

import unittest
from testScreen_idDownload import testScreen_idDownload

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testScreen_idDownload)
    unittest.TextTestRunner(verbosity=2).run(suite)