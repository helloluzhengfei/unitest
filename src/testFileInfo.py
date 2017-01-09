#coding=GBK
import requests
import unittest
import json
import os
import numbers
class testFileInfo(unittest.TestCase):
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
        
#��һ�β���   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]
#��data�е�id�������α��������뵽self.cat_list��
        for jCat in jData: 
            self.cat_listId.append(jCat['id'])                     
            self.cat_listParent_id.append(jCat['parent_id'])            
       
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

#ɾ����id�е�parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)

#����ѭ�������ų�parent_id��list����id����app����     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '���Ե�%d��Ӧ��' %i
            print 'cat_id���Ե�ID��%r '  %category_id 
           
            i=i+1
            self.get_app_info(category_id)  
        
        
        print 'app_id��file���ԡ�������������' 
        for  app_id in self.list_app_id:                               
            print app_id
            print '\t' 
            
        print 'apk_id��file���ԡ�������������'    
        for apk_id in self.list_apk_id:
             
            print apk_id
            print '\t' 
            self.get_file_info(apk_id, 1)
           
        print 'icon_id��file���ԡ�������������'     
        for icon_id in self.list_icon_id:
            
            print icon_id
            print '\t' 
            self.get_file_info(icon_id, 2)
           
        print 'screen_id��file���ԡ�������������'    
        for screen_id in self.list_screen_id:
             
            print screen_id
            print '\t' 
            for screen_id1 in screen_id:
                self.get_file_info(screen_id1, 3)
                    
#��Ҫ�����ǽ�ȥ��parentid��id���������й����ڵĵ���
             
#�ڶ��β���        10.110.1.55:8081/1.0/cat/app/app_id
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
        print url
       
        response = requests.get(url)

        jResp = response.json()
 
        jData = jResp["data"]

        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               
                self.list_apk_id.append(appData['apk_id'])
                self.list_icon_id.append(appData['icon_id'])
                self.list_screen_id.append(appData['screen_id'])

############################################################
              

    def get_file_info(self, file_id, file_type):
        url = self.base_url + self.file_prop_uri + file_id #http://10.110.1.55:8081/1.0/file/
        print '½����  ����file���Ե�URL��'
        print url
        #print self.cat_list
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print '�ļ������еķ�������Ӧ�����200'
        
        jData = response.json()['data']
        print '½���� id'
        print jData['id']
        
        print '½����    digest'
        print jData['digest']
        
        
        print '½����     size'
        print jData['size']
        
        
        print '½����     mime_type'
        mime_type=jData['mime_type']
        print mime_type
        
        file_suffix = jData['file_suffix']
        print file_suffix
  
   