#coding=GBK  
import requests
import unittest
import json
import os
import numbers
from ctypes.test.test_numbers import bool_types
import string
import re
class testLastUpdate(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.update_url='app/lastupdate'
        self.recommend_listId=[]
        self.recommend_app_name=[]           
        self.recommend_package_name=[]
        self.recommend_version_code=[]
        self.recommend_cat=[]
        self.recommend_price=[]
        self.recommend_app_permit=[]
        self.recommend_apk_id=[]
        self.recommend_icon_id=[]
        self.recommend_screen_id=[]
        self.recommend_signature=[]
        self.recommend_file_size=[]
        self.recommend_download_count=[]
        self.recommend_create_date=[]
        self.recommend_mod_date=[]
        self.recommend_purchase=[]
        self.recommend_package_name=[]
        
    def test1_cat_list_api(self):
        pqyload = {'pos':'1','limit':'3','orderByColumn':'1'}
        url = self.base_url + self.update_url           
        print '本次测试的URL是'
        print url      
        response = requests.get(url,params = pqyload) 
        jResp = response.json() 
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        
        result_code = jResp["result_code"]        
        self.assertEqual(result_code, 200) #判断result_code是否等于200
    
        list_limit = jResp['limit']
        self.cat_total=jResp["total"]
        self.assertLessEqual(list_limit, self.cat_total)#判断limit数量是否不大于total
    
        jData = jResp["data"]

        for jCat in jData:
            self.recommend_listId.append(jCat['id']) 
            print 'id...'
            print  jCat['id']                                                 
            self.recommend_app_name.append(jCat['app_name']) 
            print 'app_name'
            print  jCat['app_name']  
            self.recommend_app_name.append(jCat['package_name'])
            print 'package_name'
            print  jCat['package_name']         
            self.recommend_package_name.append(jCat['version_name'])
            print 'version_name'
            print  jCat['version_name']
            self.recommend_version_code.append(jCat['version_code'])
            print 'version_code'
            print  jCat['version_code']
            self.recommend_cat.append(jCat['cat'])
            print 'cat'
            print  jCat['cat']
            self.recommend_price.append(jCat['app_desc'])
            print 'app_desc'
            print  jCat['app_desc']
            self.recommend_price.append(jCat['price'])
            print 'price'
            print  jCat['price']
            self.recommend_app_permit.append(jCat['app_permit'])
            print 'app_permit'
            print  jCat['app_permit']
            self.recommend_apk_id.append(jCat['apk_id'])
            print 'apk_id'
            print  jCat['apk_id']
            self.recommend_icon_id.append(jCat['icon_id'])
            print 'icon_id'
            print  jCat['icon_id']
            self.recommend_screen_id.append(jCat['screen_id'])
            print 'screen_id'
            print  jCat['screen_id']
            self.recommend_signature.append(jCat['signature'])
            print 'signature'
            print  jCat['signature']
            self.recommend_file_size.append(jCat['file_size'])
            print 'file_size'
            print  jCat['file_size']
            self.recommend_download_count.append(jCat['download_count'])
            print 'download_count'
            print  jCat['download_count']
            self.recommend_create_date.append(jCat['create_date'])
            print 'create_date'
            print  jCat['create_date']
            self.recommend_mod_date.append(jCat['mod_date'])
            print 'mod_date'
            print  jCat['mod_date']
            self.recommend_purchase.append(jCat['purchase'])
            print 'purchase'
            print  jCat['purchase']
