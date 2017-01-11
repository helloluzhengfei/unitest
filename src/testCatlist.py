#coding=GBK
import requests
import unittest
import json
import os
import numbers
import re
class testCatlist(unittest.TestCase):
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
        self.app_Id=[]
        self.cat_list_create_date=[]
        self.cat_list_mod_date=[]
    #��һ�β���   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri
        print url
        
        response = requests.get(url)        
        self.assertEqual(response.status_code, 200) #�жϷ������Ƿ����200
        print '��������Ӧ����200'
        
        jResp = response.json()  
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 200) #�ж�result_code�Ƿ����200
        print 'result_code�Ľ����200'
       
        list_limit = jResp['limit']
        self.cat_total=jResp["total"]
        self.assertLessEqual(list_limit, self.cat_total)#�ж�limit�����Ƿ񲻴���total
        print 'limit������total'
        
        jData = jResp["data"]
#��data�е�id�������α��������뵽self.cat_list��
        for jCat in jData:

            self.cat_listId.append(jCat['id'])   #0000-3b85e060-14ab-4f2a-a5f3-16cec8ebf9a9                              
            self.cat_listName.append(jCat["name"]) #��������
            
            
            
                      
            self.cat_listSeq_num.append(jCat['seq_num'])   
            b=type(jCat['seq_num'])            
            self.assertEqual(b, int)
                    
            self.cat_listFile_size.append(jCat['file_size']) 
            c=type(jCat['file_size'])            
            self.assertEqual(c, int)
                       
            self.cat_listMime_type.append(jCat['mime_type'])
                                    
            self.cat_listParent_id.append(jCat['parent_id'])  
                    
            self.cat_listMime_type.append(jCat['mime_type']) 
           
            
            self.cat_list_create_date.append(jCat['create_date'])
            d=type(jCat['file_size'])            
            self.assertEqual(d, int)
            
            self.cat_list_mod_date.append(jCat['mod_date'])       
            e=type(jCat['file_size'])            
            self.assertEqual(e, int)
                   
#�˴�����data�е�����  
        self.cat_listId.append(u'0') 
        print 'id�ǡ�����������' 
        print self.cat_listId  
        print 'Name�ǡ�����������' 
        print self.cat_listName  
        print 'Seq_num�ǡ�����������' 
        print self.cat_listSeq_num 
        print 'File_siz�ǡ�����������'    
        print self.cat_listFile_size  
        print 'Mime_type�ǡ�����������'   
        print self.cat_listMime_type    
        print 'Parent_id�ǡ�����������'  
        print self.cat_listParent_id
        print 'create_date�ǡ���'
        print self.cat_list_create_date
        print 'mod_date�ǡ�����'
        print self.cat_list_mod_date


#�ж�        Parent_id�Ƿ������listId��
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))

        for Parent_idRemSm in self.cat_listParent_idRemSm:     
            self.assertIn(Parent_idRemSm,self.cat_listId) 
        print 'Parent_id��Id��'  

        b=[] 
        for i in range(0,100):
            b.append(i)
        for Seq_num in self.cat_listSeq_num:         
            self.assertIn(Seq_num,b)
        print 'seq_numΪ���֣������λ'
            
        self.cat_listId_len=len(self.cat_listId)-1 #��self.cat_list�ĳ��ȷŵ�����self.cat_list_len��
        self.assertEqual(list_limit, self.cat_listId_len) #�ж�data�е���Ŀ�����Ƿ����limit
        print '��Ŀ��������limit'

        print u'��һ�μ����������'
        print '\t'
'''
#ɾ����id�е�parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)
        
        print 'ȥ��parent-id���id�У�'
        print self.cat_listId
#����ѭ�������ų�parent_id��list����id����app����     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '���Ե�%d��Ӧ��' %i
            print 'cat_id���Ե�ID��%r '  %category_id 
           
            i=i+1
#            self.get_app_info(category_id)
 
'''