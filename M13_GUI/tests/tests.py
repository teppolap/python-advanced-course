import unittest
from helpers import *

#Comment out if no python functions are tested
#NOTE: If this is not commented out, src/my_code.py will be executed.
#(You can abuse this, for example, if you like to check global variables etc.)
#from my_code import *

started_tests = 0
completed_tests = 0



class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()

        my_code="""
import sys
sys.path.insert(0, '../src')
    
import my_code
from tkinter import END

def print_text(n, lbl):
    msg=lbl.cget('text')
    msg='*'+msg+'*'
    print(str(n)+':'+msg+':END')

for i in range(10):
    print_text(i, my_code.lbl)
    my_code.btn.invoke()
"""

        res=callpythoncode(my_code, timeout=2)
        res=res.split('\n')

        print(res)
        res_dict={}
        for r in res:
            if r=='':
                continue
            s=r.split(':')
            print(s)
            res_dict[int(s[0])]=s[1]
            self.assertTrue(s[2]=='END')
        print(res_dict)

        self.assertEqual(res_dict[1], res_dict[9])
        for i in range(2, 9):
            self.assertNotEqual(res_dict[i], res_dict[9])
        
        for n in ['kato', 'toka', 'voi', 'zurf']:
            s='*'+n+'*'
            self.assertIn(s, res_dict.values())
        
        self.endTest()

    def startTest(self):
        global started_tests
        started_tests=started_tests+1
        print('\nStart test', started_tests)

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests=completed_tests+1


def completed():
    global completed_tests
    return completed_tests

def started():
    global started_tests
    return started_tests

