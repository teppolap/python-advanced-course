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

#Check initial state of the label
initial_label=my_code.lbl.cget('text')
my_code.btn.invoke()
final_label=my_code.lbl.cget('text')
print('Got:'+initial_label)
print('Got:'+final_label)
"""

        res=callpythoncode(my_code, timeout=2)
        #print(res)

        for msg in ['Got:Button not pressed!', 'Got:Button pressed!']:
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

