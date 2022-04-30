import os
import shutil

path = input("Enter the path of the folder that you want to organise")
fileList = os.listdir(path)
for file in fileList:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file , path+"/"+ext)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext)
