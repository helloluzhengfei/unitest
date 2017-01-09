#coding=GBK
import requests
import unittest
import json
import os
import numbers
class testShowApp(unittest.TestCase):
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
        self.get_commentlist_uri='app/c/list/'###########�¼�
        self.get_app_allinfo_uri='app/'
       
        
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
        
        self.comment_id=[] 
        self.comment_app_id=[]    
        self.comment_msg=[]   
        self.comment_ip=[] 
        self.comment_stars=[] 
        self.comment_create_date=[] 
        
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
        
        
       
        for  app_id in self.list_app_id:                               
            print app_id
            self.get_comment_list(app_id)
            print '\t' 
            
#        print 'apk_id��file���ԡ�������������'    
#       for apk_id in self.list_apk_id:
             
#            print apk_id
#            print '\t' 
#            self.get_file_info(apk_id, 1)
           
#        print 'icon_id��file���ԡ�������������'     
#        for icon_id in self.list_icon_id:
            
#            print icon_id
#            print '\t' 
#            self.get_file_info(icon_id, 2)
           
#        print 'screen_id��file���ԡ�������������'    
#        for screen_id in self.list_screen_id:            
#            print screen_id
#            print '\t' 
#            for screen_id1 in screen_id:
#                self.get_file_info(screen_id1, 3)
                    
#��Ҫ�����ǽ�ȥ��parentid��id���������й����ڵĵ���
             
#�ڶ��β���        10.110.1.55:8081/1.0/cat/app/app_id
#ѭ����������app_id,apk_id,icon_id,scree����idȫ����������
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
#        print url       
        response = requests.get(url)
        jResp = response.json()
        jData = jResp["data"]
        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               
#                self.list_apk_id.append(appData['apk_id'])
#                self.list_icon_id.append(appData['icon_id']) 

#                self.list_screen_id.append(appData['screen_id'])

############################################################
              

    def get_comment_list(self, app_id):
        
#        a=input("������pos��ֵ")
#        b=input("������limit��ֵ")
#        self.commentcontent='?pos=%d&limit=%d' %(a,b)
        
        ###########�˴���Ҫ�޸�
        
        url = self.base_url + self.get_app_allinfo_uri + app_id#+self.commentcontent #http://10.110.1.55:8081/1.0/file/
        print '½����  ���β��Ե�URL��'
        print url
        
        response = requests.get(url) 
        self.assertEqual(response.status_code, 200) #�жϷ������Ƿ����200
        print '��������Ӧ����200'
        #print self.cat_list
        jResp = response.json()  
        result_code = jResp["result_code"]        
        self.assertEqual(result_code, 200) #�ж�result_code�Ƿ����200
        print 'result_code�Ľ����200' 
#        print result_code       
        
        
          
             
              
        jData = jResp["data"]
        
        print "���۵�id�ǡ�����"                     
        print jData['id']
            
        print "���۵�app_name������"            
        print jData['app_name']
            
        print "���۵�package_name�ǡ�����"            
        print jData['package_name']
            
        print "���۵�version_name�ǡ�����"
        print jData['version_name']
            
        print "���۵�version_code�ǡ�����"
        print jData['version_code']
            
        print "���۵�cat�ǡ�����"
        print jData['cat']
        
        print "���۵�app_desc�ǡ�����"
        print jData['app_desc']
        
        print "���۵�version_desc�ǡ�����"
        print jData['version_desc']
        
        print "���۵�cprice�ǡ�����"
        print jData['price']
        
        print "���۵�app_permit�ǡ�����"
        print jData['app_permit']
        
        print "���۵�apk_id�ǡ�����"
        print jData['apk_id']
        
        print "���۵�icon_id�ǡ�����"
        print jData['icon_id']
        
        print "���۵�screen_id�ǡ�����"
        print jData['screen_id']
        
        print "���۵�signature�ǡ�����"
        print jData['signature']
        
        print "���۵�file_size�ǡ�����"
        print jData['file_size']
        
        print "���۵�download_count�ǡ�����"
        print jData['download_count']
        
        print "���۵�create_date�ǡ�����"
        print jData['create_date']
        
        print "���۵�mod_date�ǡ�����"
        print jData['mod_date']
        
        print "���۵�purchase�ǡ�����"
        print jData['purchase'] 
  