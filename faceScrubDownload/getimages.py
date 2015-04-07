# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 15:28:53 2015

@author: Chenriwei
"""

import os
import re
import time
import urllib

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
        print image_url+'\n'
        print box+'\n'
        if False == os.path.exists(name):
            os.mkdir(name)
        
        try:
         urlopen=urllib.URLopener()
         fp = urlopen.open(image_url)
         data = fp.read()
         fp.close()
         file=open(name+'/'+image_id+'.jpg','w+b')
         file.write(data)
         print "下载成功："+ image_url
         file.close()
        except IOError:
         print "下载失败:"+ image_url

if __name__ == "__main__":
    get_all_iamge('facescrub_actors.txt')