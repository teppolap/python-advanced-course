import unittest
from helpers import *

#Comment out if no python functions are tested
#NOTE: If this is not commented out, src/my_code.py will be executed.
#(You can abuse this, for example, if you like to check global variables etc.)
#from my_code import *

started_tests = 0
completed_tests = 0

code="""
from pynput import keyboard
import time

import sys
sys.path.insert(0, '../src')
import my_code
from getkey import *

#del mainloop

def on_press(key):
    pass

def kbtest():
    print('kbtest() started')
    time.sleep(1.0)
    kb=keyboard.Controller()
    print('kbtest() -- send 9812037465')
    kb.type('9812037465')
    time.sleep(0.5)
    print('kbtest() terminate')

    #Remove sent keys
    for _ in range(20):
        kb.press(keyboard.Key.backspace)
        kb.release(keyboard.Key.backspace)
    time.sleep(0.5)


def test_mainloop():
    init_mainloop()

    ##############################################
    #Taman pitaa olla tassa. Ei toimi erillisessa saikeessa tai ennen init_mainloop-kutsua
    
    kbtest()

    ##############################################
    print('Enter mainloop()')
    while my_code.active_mainloop:
        #print(active_mainloop)
        #Read key pressed (if any)
        k=get_key()
        if k!='':
            if k in my_code.events:
                f=my_code.events[k]
                f()
        else:
            #Release control
            time.sleep(0.01)
    print('Exit mainloop()')
    clean_mainloop()

test_mainloop()
"""



class TestCode(unittest.TestCase):
    def test_Python(self):
        #Test python program
        self.startTest()
        res=callpythoncode(code=code, cmdline_args=[], input='', timeout=10)
        print(res)
        must_include=['45', '17', '23', '34', '40', 'Exit mainloop()']
        for txt in must_include:
            print('Test if output contains "'+txt+'"', end=' ')
            self.assertTrue(txt in res)
            print('- ok')
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

