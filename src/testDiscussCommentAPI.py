#coding=GBK  
'''
Created on 2017年1月6日

@author: zhengfei.lu
'''
import unittest
from testDiscussComment import testDiscussComment

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(testDiscussComment)
    unittest.TextTestRunner(verbosity=2).run(suite)