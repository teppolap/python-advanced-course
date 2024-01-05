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

my_code.entry_a.delete(0, END)
my_code.entry_b.delete(0, END)
my_code.entry_c.delete(0, END)
my_code.entry_a.insert(0, '11')
my_code.entry_b.insert(0, '3')
my_code.entry_c.insert(0, '-4')
my_code.btn.invoke()
root1=my_code.label_root1.cget('text')
root1=root1[0:4]
root2=my_code.label_root2.cget('text')
root2=root2[0:4]
print('Got:'+root1)
print('Got:'+root2)


my_code.entry_a.delete(0, END)
my_code.entry_b.delete(0, END)
my_code.entry_c.delete(0, END)
my_code.entry_a.insert(0, '11')
my_code.entry_b.insert(0, '3')
my_code.entry_c.insert(0, '4')
my_code.btn.invoke()
root1=my_code.label_root1.cget('text')
root2=my_code.label_root2.cget('text')
print('Got:"'+root1+'"')
print('Got:"'+root2+'"')
"""

        res=callpythoncode(my_code, timeout=2)
        print(res)

        for msg in ['Got:0.48', 'Got:-0.7', 'Got:"-"']:
            self.assertTrue(msg in res)
        
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
