#coding=GBK  
import requests
import unittest
import json
import os
import numbers
from ctypes.test.test_numbers import bool_types
import string
import re
class testApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.cat_list_uri = 'cat/list'
        self.cat_app_uri = 'cat/app/'
        self.file_prop_uri = 'file/'
        self.dlwd_icon_uri = 'app/icon/cont/'
        self.dlwd_screen_uri = 'app/screen/cont/'
        self.dlwd_apk_uri = 'app/cont/'
        self.comment_add_uri = 'app/c/' #  POST /app/c/{app_id}
        self.comment_get_uri = 'app/screen/cont/' #GET app/c/list/{app_id}?pos={pos}&limit={limit}
        self.cat_listId = []   #data
        self.cat_len = 0;
        self.cat_listName=[]   #name
        self.cat_listSeq_num=[]   #seq_num
        self.cat_listFile_size=[]   #file_size
        self.cat_listMime_type=[]   #mime_type
        self.cat_listParent_id=[]    #parent_id
        self.cat_listMime_type=[]   
        self.list_app_id=[]
        self.list_icon_id=[]
        self.list_apk_id=[]
        self.list_screen_id=[]

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
#        print self.cat_listId
        
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
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+category_id
        print url
        #print self.cat_list
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print 'app的状态码是200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 200) 
        print 'result_code值为200'
        
        appNum_limit = jResp["limit"]
        appNum_total=jResp['total'] 
        self.assertLessEqual(appNum_limit, appNum_total) 
        print 'limit小于等于total'

 
        jData = jResp["data"]

        for appData in jData:
            
                print 'app_id'
                print appData['id']
                self.list_app_id.append(appData['id'])
                self.list_tmp_id.append(appData['id'])
                
                
                print 'app_name'
                print appData[u'app_name']
                p = re.compile('^[\u4E00-\u9FFF]+$')
                c= p.match(appData['app_name'])
                print c 
  #              b=type(appData['app_name'])            
  #              self.assertEqual(b, str)
                
                print 'package_name'
                print appData['package_name']
                b=type(appData['package_name'])            
 #               self.assertEqual(b, string)
                
                print 'version_name'
                print appData['version_name']
                b=type(appData['version_name'])            
  #              self.assertEqual(b, str)
                
                print 'version_code'
                print appData['version_code']
                b=type(appData['version_code'])            
                self.assertEqual(b, int)
                
                print 'cat'
                print appData['cat']
                b=type(appData['cat'])            
#                self.assertIsInstance(b, str)
                
                print 'price'
                print appData['price']
                b=type(appData['price'])            
 #               self.assertIsInstance(b, float)
                
                
                print 'app_permit'
                print appData['app_permit']
                
                print 'apk_id'
                print appData['apk_id']
                self.list_apk_id.append(appData['apk_id'])
                
                print 'icon_id'
                print appData['icon_id']
                self.list_icon_id.append(appData['icon_id'])
            
                print 'signature'
                print appData['signature']
#                self.assertIsInstance(appData['signature'],str) 
                        
                print 'screen_id'
                print appData['screen_id']
                self.list_screen_id.append(appData['screen_id'])
                
                print 'file_size'
                print appData['file_size']
                b=type(appData['file_size'])            
                self.assertEqual(b, int)
                
                print 'download_count'
                print appData['download_count']
                b=type(appData['download_count'])            
                self.assertEqual(b, int)
                
                print 'create_date'
                print appData['create_date']
                b=type(appData['create_date'])            
                self.assertEqual(b, long)
                
                print 'mod_date'
                print appData['mod_date']
                b=type(appData['mod_date'])            
                self.assertEqual(b, long)
                
                print 'purchase'
                print appData['purchase']
                b=type(appData['purchase'])            
                self.assertEqual(b, bool)
                

        print 'app_id检查' 
        for   app_id in self.list_app_id:
                                  
            print app_id
            print '\t' 
            
        print 'apk_id检查'    
        for apk_id in self.list_apk_id:
             
            print apk_id
            print '\t' 

           
        print 'icon_id检查'     
        for icon_id in self.list_icon_id:
            
            print icon_id
            print '\t' 

           
        print 'screen_id检查'    
        for screen_id in self.list_screen_id:
             
            print screen_id
            print '\t' 
            
        self.assertLessEqual(appNum_limit, len(self.list_tmp_id))
        print '项目数量等于limit'   