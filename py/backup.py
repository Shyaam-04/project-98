import os
import shutil

source= input("Enter the path of the folder which you want to backup")
destination = input("Enter the backup folder")

fileList = os.listdir(source)
for file in fileList:
    shutil.copy(source+"/"+file,destination)
    
