# -*- coding:utf-8 -*-

from pyautocad import Autocad, APoint
import os

def getFileList(rootdir):   
    files = []
    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字    
        for filename in filenames:                        #输出文件信息
            files.append(parent+"/"+filename) #输出文件路径信息       
    return files  

if __name__ == "__main__":
    acad = Autocad()
    rootdir = "G:/dx/1000"
    for fl in getFileList(rootdir):
        doc = acad.Application.Documents.Open(fl)         
        try:
            l = doc.Layers("SUB")
            doc.ActiveLayer = doc.Layers("0")
            for obj in doc.Modelspace:
                if obj.Layer == "SUB":
                    obj.delete()
                else:
                    pass
            l.Delete()
            doc.Save()
            print u"%s处理完" % doc.name
        except:            
            print u"%s处理不成功!" % doc.name
        finally:
            doc.Close()
        
