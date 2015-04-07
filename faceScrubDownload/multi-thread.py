# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 20:19:38 2015

@author: Chenriwei
"""

import threading
import os
import urllib


def download_and_save(url,savename):
        try:
         urlopen=urllib.URLopener()
         fp = urlopen.open(url)
         data = fp.read()
         fp.close()
         fid=open(savename,'w+b')
         fid.write(data)
         print "下载成功："+ url
         fid.close()
        except IOError:
         print "下载失败:"+ url
         

def get_all_iamge(filename):
    fid=open(filename)
    lines=fid.readlines()
    for line in lines:
        line_split=line.split('\t')
        name=line_split[0]
        image_id=line_split[1]
        face_id=line_split[2]
        box=line_split[4]
        image_url=line_split[3]
        if False == os.path.exists(name):
            os.mkdir(name)
        savefile=name+'/'+image_id+'.jpg'  
        
        while True:
                if(len(threading.enumerate()) < 1000):
                    break
                
        t = threading.Thread(target=download_and_save,args=(image_url,savefile,))
        t.start()

if __name__ == "__main__":
    get_all_iamge('facescrub_actresses.txt')
    get_all_iamge('facescrub_actors.txt')
    print 'done!'