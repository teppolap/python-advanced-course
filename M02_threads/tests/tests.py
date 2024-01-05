import unittest
from helpers import *

#Never do following! The test process can be halted by student code!
#from my_code import *



started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    """
    def test_Python(self):
        #Test python program
        self.startTest()
        self.assertEqual(callpython(cmdline_args=['a', 'b'], input='\n').strip(), 'a b')
        self.endTest()
    """
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        expected_output=[
            'None started 0',
            '->test_heavy_computing(0)',
            '->test_heavy_computing(1)',
            '->test_heavy_computing(2)',
            '->test_heavy_computing(3)',
            '->test_heavy_computing(4)',
            '->test_heavy_computing(5)',
            '->test_heavy_computing(6)',
            '->test_heavy_computing(7)',
            '->test_heavy_computing(8)',
            '->test_heavy_computing(9)',
            'All started 10',
            '<-test_heavy_computing(0)',
            '<-test_heavy_computing(1)',
            '<-test_heavy_computing(2)',
            '<-test_heavy_computing(3)',
            '<-test_heavy_computing(4)',
            '<-test_heavy_computing(5)',
            '<-test_heavy_computing(6)',
            '<-test_heavy_computing(7)',
            '<-test_heavy_computing(8)',
            '<-test_heavy_computing(9)',
            'All completed 0'
        ]
        
        my_code="""
import sys
sys.path.insert(0, '../src')

import threading
import time

from my_code import start_threads, wait_threads

if True:
    try:
        del heavy_computing
    except:
        pass

    lock_count=threading.Lock()
    thCount=0
    
    def test_heavy_computing(idx):
        global thCount
        global lock_count
        
        print('->test_heavy_computing('+str(idx)+')')
        with lock_count:
            thCount=thCount+1
        time.sleep(2)
        with lock_count:
            thCount=thCount-1
        print('<-test_heavy_computing('+str(idx)+')')

    N=10
    
    with lock_count:
        print('None started', thCount)

    th_list=start_threads(test_heavy_computing, N)
    time.sleep(0.5)

    with lock_count:
        print('All started', thCount)
    wait_threads(th_list)
    with lock_count:
        print('All completed', thCount)
"""
        ret=callpythoncode(my_code, input='')

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

