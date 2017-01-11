#coding=GBK  
import requests
import unittest
import json
import os
import numbers
from ctypes.test.test_numbers import bool_types
import string
import re
class testAppIfUpdate(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.cat_list_uri = 'cat/list'
        self.cat_app_uri = 'cat/app/'
        self.update_url='app/update/query'
        self.cat_listId = []   #data
        self.cat_listParent_idRemSm=[]
        self.cat_listParent_id=[]
        self.cat_len = 0;     
        self.package_name=[]
        self.version_code=[]      

    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()          
        jData = jResp["data"]
        for jCat in jData:
            self.cat_listId.append(jCat['id'])                                                      
            self.cat_listParent_id.append(jCat['parent_id'])            
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')       
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)       
        print '去除parent_id的id列表'
        print self.cat_listId  
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '第%d个应用' %i
            print '该应用的id是%r '  %category_id         
            i=i+1
            self.get_app_info(category_id)  
              

    def get_app_info(self, category_id):        
        url = self.base_url + self.cat_app_uri+category_id       
        response = requests.get(url)
        jResp = response.json()
        jData = jResp["data"]

        for appData in jData:
  #          a=self.package_name.append(appData['package_name'])
            a=appData['package_name']
            print appData['package_name']
   #         b=self.version_code.append(appData['version_code'])
            b=appData['version_code']
            print a
            print b        
            self.get_test1_cat_list_api(a,b)  
         
    def get_test1_cat_list_api(self,package_name,version_code):
        print package_name
        print version_code
        pqyload = {"query_param":[{"package_name":package_name,"version_code":version_code}]}
        print pqyload
        url = self.base_url + self.update_url           
        print '本次测试的URL是'
        print url      
        response = requests.post(url,data = json.dumps(pqyload)) 
        jResp = response.json() 
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        
        result_code = jResp["result_code"]        
        self.assertEqual(result_code, 200) #判断result_code是否等于200
    
        list_limit = jResp['limit']
        self.cat_total=jResp["total"]
        self.assertLessEqual(list_limit, self.cat_total)#判断limit数量是否不大于total
    
        jData = jResp["data"] 
          

        for jCat in jData:
           
            print 'id...'
            print  jCat['id']                                                 
            
            print 'app_name'
            print  jCat['app_name']          
            
            print 'version_name'
            print  jCat['version_name']
           
            print 'version_code'
            print  jCat['version_code']
            
           
            print 'app_desc'
            print  jCat['app_desc']
            
 #           print 'version_desc'
 #           print  jCat['version_desc']
           
            print 'app_permit'
            print  jCat['app_permit']
            
            print 'apk_id'
            print  jCat['apk_id']
            
            print 'icon_id'
            print  jCat['icon_id']
            
            print 'screen_id'
            print  jCat['screen_id']
            
            print 'signature'
            print  jCat['signature']
            
            print 'file_size'
            print  jCat['file_size']
            
            print 'download_count'
            print  jCat['download_count']
            
            print 'create_date'
            print  jCat['create_date']
            
            print 'mod_date'
            print  jCat['mod_date']
            
            print 'purchase'
            print  jCat['purchase']                         