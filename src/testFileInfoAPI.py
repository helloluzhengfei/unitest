#coding=GBK  
'''
Created on 2017年1月6日

@author: zhengfei.lu
'''
import unittest
from testFileInfo import testFileInfo

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testFileInfo)
    unittest.TextTestRunner(verbosity=2).run(suite)