#coding=GBK
import requests
import unittest
import json
import os
import numbers
class testAppCommentsList(unittest.TestCase):
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
            

    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
#        print url       
        response = requests.get(url)
        jResp = response.json()
        jData = jResp["data"]
        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               

              

    def get_comment_list(self, app_id):
        
#        a=input("������pos��ֵ")
#        b=input("������limit��ֵ")
#        self.commentcontent='?pos=%d&limit=%d' %(a,b)
        
        ###########�˴���Ҫ�޸�
        pqyload = {'pos':'0','limit':'100'}
        url = self.base_url + self.get_commentlist_uri + app_id#+self.commentcontent #http://10.110.1.55:8081/1.0/file/
        print '���β��Ե�URL��'
        print url
        
        response = requests.get(url,params = pqyload) 
        self.assertEqual(response.status_code, 200) #�жϷ������Ƿ����200
        print '��������Ӧ����200'
        #print self.cat_list
        jResp = response.json()  
        result_code = jResp["result_code"]        
        self.assertEqual(result_code, 200) #�ж�result_code�Ƿ����200
        print 'result_code�Ľ����200' 
#        print result_code       
        
        
        list_limit = jResp['limit']
        self.cat_total=jResp["total"]
        self.assertLessEqual(list_limit, self.cat_total)#�ж�limit�����Ƿ񲻴���total
        print 'limit������total'   
             
        i=1       
        jData = jResp["data"]
        for jCat in jData: 
            print "�� %d ������"  %i
            i=i+1  
            
            print "���۵�id�ǡ�����"        
               
            print jCat['id']
            
            print "���۵�app_id������"            
            print jCat['app_id']
            
            print "���۵�msg�ǡ�����"            
            print jCat['msg']
            
            print "���۵�ip�ǡ�����"
            print jCat['ip']
            
            print "���۵�stars�ǡ�����"
            print jCat['stars']
            
            print "���۵�create_date�ǡ�����"
            print jCat['create_date']

'''            
            self.comment_id.append(jCat['id'])  
            self.comment_app_id.append(jCat['app_id'])   
            self.comment_msg.append(jCat['msg'])  
            self.comment_ip.append(jCat['ip'])
            self.comment_stars.append(jCat['stars'])
            self.comment_create_date.append(jCat['create_date'])             
                      
       
        
        
        for comid in self.comment_id:
            print comid
''' 

        
                

      
        
        

    
        