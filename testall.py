import os
import sys
import subprocess

if __name__=='__main__':
    resultsfile=open('results.txt', 'wt')
    skiplist=['ex_template', 'helpers']

    for file in os.listdir('.'):
        if file in skiplist:
            continue
        if os.path.isdir(file):
            cmdline=sys.executable+' test.py'
            print(cmdline)
            #rc=os.system(cmdline)
            #print('#', rc)
            rc=subprocess.call(cmdline, shell=True, cwd=file)
            #print('#', rc)
            try:
                exresfile=open(file+'/tests/result.txt', 'rt')
                res=exresfile.read()
                #print('#',res)
                resultsfile.write(file+'\t'+res+'\n')
                exresfile.close()
            except:
                #Result file not found
                resultsfile.write(file+'\t'+'0\t0\n')
                pass

    resultsfile.close()
