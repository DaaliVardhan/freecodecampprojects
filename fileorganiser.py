import os
import shutil
dirname=input('enter the folder name:')
li=os.listdir(dirname)
for i in li:
    filename,extension=os.path.splitext(i)
    extension=extension[1:]
    if extension=="":
        continue
    if os.path.exists(dirname+"/"+extension):
        shutil.move(dirname+'/'+i,dirname+'/'+extension+'/'+i)
    else:
        os.makedirs(dirname+'/'+extension)
        shutil.move(dirname+'/'+i,dirname+'/'+extension+'/'+i)