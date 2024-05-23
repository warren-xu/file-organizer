import os
import shutil

path = input("Enter path to organize: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)    # split filename and extension of file
    extension = extension[1:]   # remove . from extension through slicing

    if os.path.exists(path+'/'+extension):      # if path exists, add it to that extension
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        os.makedirs(path+'/'+extension)         # else create the folder
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)