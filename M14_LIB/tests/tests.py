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
import random
sys.path.insert(0, '../src')
    
from my_code import testPalindrome


def ispal1(s):
    s=s.lower()
    s=''.join(ch for ch in s if ch.isalnum())

    return s==s[::-1]

def ispal2(s):
    s=s.lower()
    s=''.join(ch for ch in s if ch.isalnum())

    return s==s[:-1]

def ispal3(s):
    s=s.lower()
    s=''.join(ch for ch in s if ch.isalnum())

    return s==s[1::-1]

def ispal4(s):
    return random.randint(0,3)<1

if testPalindrome(ispal1):
    print('1st test ok')
if not testPalindrome(ispal2):
    print('2nd test ok')
if not testPalindrome(ispal3):
    print('3rd test ok')
if not testPalindrome(ispal4):
    print('4th test ok')

"""

        res=callpythoncode(my_code, timeout=2)

        for er in ['1st test ok','2nd test ok','3rd test ok', '4th test ok']:
            self.assertTrue(er in res)
            print(er)
        
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

