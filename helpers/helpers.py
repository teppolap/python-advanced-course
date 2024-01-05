# -*- coding: utf-8 -*-
import sys
import subprocess
import re
import os


def getpath():
    # Find path to current root
    pathlist = split(sys.argv[0])
    if len(pathlist) == 1:
        path = './'
    else:
        path = pathlist[0] + '/'

    return path

#Run code
def callpythoncode(code, cmdline_args=[], input='', timeout=30):
    path=getpath()

    testcodefile='tests/my_test_code.py'
    f=open(testcodefile, "w")
    f.write(code)
    f.close()
    
    cmd_line=[sys.executable, '../'+testcodefile,]+cmdline_args
    try:
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except subprocess.TimeoutExpired:
        print('Timeout expired!')
        return ''
    except:
        print('Execute dropped to fallback!')
        cmd_line_str=' '.join(cmd_line)
        rc = subprocess.run(cmd_line_str, cwd=path+'/src', stdout=subprocess.PIPE, universal_newlines=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    os.remove(testcodefile)    
    
    return rc.stdout

#Run my_code.py and additional code
def callpythonmaincode(code, cmdline_args=[], input='', timeout=30):
    my_code=loadmycode()

    return callpythoncode(code=my_code+code, cmdline_args=cmdline_args, input=input, timeout=timeout)

#Load student code
def loadmycode():
    for encoding in ['latin1', 'utf8','utf16','cp437']:
        try:
            with open('src/my_code.py', encoding=encoding) as f:
                my_code = f.read()
            return my_code
        except:
            pass

#Run my_code.py
def callpython(cmdline_args=[], input='', timeout=30):
    path=getpath()

    cmd_line=[sys.executable, 'my_code.py',]+cmdline_args
    try:
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
    except subprocess.TimeoutExpired:
        print('Timeout expired!')
        return ''
    except:
        print('Execute dropped to fallback!')
        cmd_line_str=' '.join(cmd_line)
        print('"',cmd_line_str, '"')
        rc = subprocess.run(cmd_line_str, cwd=path+'/src', stdout=subprocess.PIPE, universal_newlines=True, input=input, timeout=timeout)
        print("Fallback completed, don't worry")

    return rc.stdout


import threading
#Run my_code.py in separate thread
def callpython_subprocess(cmdline_args=[], input='', timeout=30):
    th=threading.Thread(target=callpython, args=(cmdline_args, input, timeout))
    th.start()
    return th

def load_python_code():
    file_name=getpath()+'/src/my_code.py'
    with open(file_name) as f:
        contents = f.read()
        return contents
    


def callCS(cmdline_args=[], input='', timeout=30):
    path=getpath()

    #Compile the source code
    try:
        rc = subprocess.run(['mcs', 'my_code.cs'], cwd=path+'/src', shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile falled to fallback!!')
        rc = subprocess.run(['mcs my_code.cs'], cwd=path+'/src', shell=True)
        print("Fallback completed, don't worry")

    cmd_line=['mono','my_code.exe',]+cmdline_args
    rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)

    return rc.stdout

def callCSFunction(cmdline_args=[], input='', timeout=30):
    path=getpath()

    #Compile the source code
    try:
        rc = subprocess.run(['mcs', '../tests/testmain.cs', 'my_code.cs'], cwd=path+'/src', shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile falled to fallback!!')
        rc = subprocess.run(['mcs ../tests/testmain.cs my_code.cs'], cwd=path+'/src', shell=True)
        print("Fallback completed, don't worry")

    cmd_line=['mono','../tests/testmain.exe',]+cmdline_args
    rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)

    return rc.stdout


def callC(cmdline_args=[], input='', timeout=30):
    path=getpath()

    #Compile the source code
    try:
        rc = subprocess.run(['gcc','my_code.c','-o','my_code.exe'], cwd=path+'/src', shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile dropped to fallback!!')
        rc = subprocess.run(['gcc my_code.c -o my_code.exe'], cwd=path+'/src', shell=True)


    try:
        cmd_line=['./my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Running dropped to fallback!!')
        cmd_line=[path+'\\src\\my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)

    return rc.stdout

def callCFunction(cmdline_args=[], input='', timeout=30):
    path=getpath()

    #Compile the source code
    try:
        rc = subprocess.run(['gcc','my_code.c','../tests/testmain.c','-o','my_code.exe', '-D', 'CLIBRARYTEST'], cwd=path+'/src', shell=True)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Compile dropped to fallback!!')
        rc = subprocess.run(['gcc my_code.c ../tests/testmain.c -o my_code.exe -DCLIBRARYTEST'], cwd=path+'/src', shell=True)
        print("Fallback completed, don't worry")


    try:
        cmd_line=['./my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)
        if rc.returncode!=0:
            raise FileNotFoundError
    except:
        print('!!Running dropped to fallback!!')
        cmd_line=[path+'\\src\\my_code.exe']+cmdline_args
        rc = subprocess.run(cmd_line, cwd=path+'/src', stdout=subprocess.PIPE, text=True, input=input, timeout=timeout)

    return rc.stdout

def split(s):
    return re.split('/|\\\\', s)
