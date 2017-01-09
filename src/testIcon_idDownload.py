#coding=GBK
import requests
import unittest
import json
import os
import numbers
class testIcon_idDownload(unittest.TestCase):
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
        
#第一次测试   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]
#把data中的id部分依次遍历，放入到self.cat_list中
        for jCat in jData: 
            self.cat_listId.append(jCat['id'])                     
            self.cat_listParent_id.append(jCat['parent_id'])            
       
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

#删除在id中的parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)

#依次循环带入排除parent_id的list——id进行app测试     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '测试第%d个应用' %i
            print 'cat_id测试的ID是%r '  %category_id 
           
            i=i+1
            self.get_app_info(category_id)  
        
        
#        print 'app_id的file测试。。。。。。。' 
#        for  app_id in self.list_app_id:                               
#            print app_id
#            print '\t' 
            
#        print 'apk_id的file测试。。。。。。。'    
#        for apk_id in self.list_apk_id:
             
#            print apk_id
#            print '\t' 
#            self.get_file_info(apk_id, 1)
           
        print 'icon_id的file测试。。。。。。。'     
        for icon_id in self.list_icon_id:
            
            print icon_id
            print '\t' 
            self.get_file_info(icon_id, 2)
           
#        print 'screen_id的file测试。。。。。。。'    
#        for screen_id in self.list_screen_id:            
#            print screen_id
#            print '\t' 
#            for screen_id1 in screen_id:
#                self.get_file_info(screen_id1, 3)
                    
#主要作用是将去除parentid的id放在数组中供后期的调用
             
#第二次测试        10.110.1.55:8081/1.0/cat/app/app_id
#循环遍历，将app_id,apk_id,icon_id,scree——id全部放入数组
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
#        print url       
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
        print '陆正飞  本次download测试的URL是'
        print url
        #print self.cat_list
        response = requests.get(url)
                
        jData = response.json()['data']
        mime_type=jData['mime_type']
        print mime_type
        
        filesize=self.download_file(file_id, file_type, mime_type)
        self.assertEqual(jData['size'], filesize) #判断下载的文件大小是否与data中的一致       
        print '下载的文件大小与data中的一致'
        print '\t'
        
#########################################################################
    def download_file(self, local_filename, file_type, mime_type):
        stored_filename = local_filename
        if file_type == 0:
            return
        elif file_type == 1:          #APK
            url = self.base_url + self.dlwd_apk_uri + local_filename
            stored_filename += ".apk"
        elif file_type == 2:     #icon
            url = self.base_url + self.dlwd_icon_uri + local_filename
            img_type = mime_type.split('/')[-1]
            stored_filename += "." + img_type
        elif file_type == 3:     #screen shot
            url = self.base_url + self.dlwd_screen_uri + local_filename
            img_type = mime_type.split('/')[-1]
            stored_filename += "." + img_type
        else:
            print "Error file_type="%file_type
            return
        
        print url
                
        print "#####################File will be saved as: "+stored_filename
        resp = requests.get(url, stream = True)
        if resp.status_code == 200:

            open(stored_filename, 'wb').write(resp.content)
            #得出下载文件的大小
            fileSize = os.path.getsize(stored_filename)
                   
            print '下载的文件大小是'
            print fileSize
            return fileSize
 
    