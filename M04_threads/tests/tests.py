import unittest
from helpers import *

#Never do following! The test process can be halted by student code!
#from my_code import *



started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        expected_output=[
            '41: 16',
            '1: 1',
            '0: 0',
            '35: 4',
            'count =  900'
        ]
        
        my_code="""
import sys
sys.path.insert(0, '../src')

import threading
import time
import concurrent.futures as cf

from my_code import init_values, external_count, external_function

def heavy_computing(thr_id):
    for i in range(18):
        time.sleep(0.25)
        external_function()
    return thr_id, (thr_id*thr_id)%37

#ret=init_values(computing5s)
ret=init_values(heavy_computing)

print(ret)
print('count = ', external_count())

"""
        ret=callpythoncode(my_code, input='', timeout=15)
        
        print(ret)

        for s in expected_output:
            if not s in ret:
                print(32*'-')
                print('Expected result "'+s+'" not found on output!')
                print(32*'-')
                print('Result="""')
                print(ret)
                print('"""')
            self.assertTrue(s in ret)
            
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

