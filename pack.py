from zipfile import ZipFile
import os

with ZipFile('allsrc.zip', 'w') as myzip:
    for file in os.listdir('.'):
        if os.path.isdir(file):
            if os.path.exists(file+'/src/my_code.py'):
                myzip.write(file+'/src/my_code.py')
            if os.path.exists(file+'/src/my_code.h'):
                myzip.write(file+'/src/my_code.h')
            if os.path.exists(file+'/src/my_code.c'):
                myzip.write(file+'/src/my_code.c')
            if os.path.exists(file+'/src/my_code.cs'):
                myzip.write(file+'/src/my_code.cs')


