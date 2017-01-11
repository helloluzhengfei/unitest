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
    #第一次测试   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri
        print url
        
        response = requests.get(url)        
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        print '服务器响应码是200'
        
        jResp = response.json()  
        result_code = jResp["result_code"]
               
        self.assertEqual(result_code, 200) #判断result_code是否等于200
        print 'result_code的结果是200'
       
        list_limit = jResp['limit']
        self.cat_total=jResp["total"]
        self.assertLessEqual(list_limit, self.cat_total)#判断limit数量是否不大于total
        print 'limit不大于total'
        
        jData = jResp["data"]
#把data中的id部分依次遍历，放入到self.cat_list中
        for jCat in jData:

            self.cat_listId.append(jCat['id'])   #0000-3b85e060-14ab-4f2a-a5f3-16cec8ebf9a9                              
            self.cat_listName.append(jCat["name"]) #中文名字
            
            
            
                      
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
                   
#此处放在data中的内容  
        self.cat_listId.append(u'0') 
        print 'id是。。。。。。' 
        print self.cat_listId  
        print 'Name是。。。。。。' 
        print self.cat_listName  
        print 'Seq_num是。。。。。。' 
        print self.cat_listSeq_num 
        print 'File_siz是。。。。。。'    
        print self.cat_listFile_size  
        print 'Mime_type是。。。。。。'   
        print self.cat_listMime_type    
        print 'Parent_id是。。。。。。'  
        print self.cat_listParent_id
        print 'create_date是。。'
        print self.cat_list_create_date
        print 'mod_date是。。。'
        print self.cat_list_mod_date


#判断        Parent_id是否包含在listId中
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))

        for Parent_idRemSm in self.cat_listParent_idRemSm:     
            self.assertIn(Parent_idRemSm,self.cat_listId) 
        print 'Parent_id在Id内'  

        b=[] 
        for i in range(0,100):
            b.append(i)
        for Seq_num in self.cat_listSeq_num:         
            self.assertIn(Seq_num,b)
        print 'seq_num为数字，最大两位'
            
        self.cat_listId_len=len(self.cat_listId)-1 #把self.cat_list的长度放到变量self.cat_list_len中
        self.assertEqual(list_limit, self.cat_listId_len) #判断data中的项目数量是否等于limit
        print '项目数量等于limit'

        print u'第一次检查完美结束'
        print '\t'
'''
#删除在id中的parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)
        
        print '去除parent-id后的id有：'
        print self.cat_listId
#依次循环带入排除parent_id的list——id进行app测试     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '测试第%d个应用' %i
            print 'cat_id测试的ID是%r '  %category_id 
           
            i=i+1
#            self.get_app_info(category_id)
 
'''