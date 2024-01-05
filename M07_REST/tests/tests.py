import unittest
import random
from helpers import *
import os 
import time
import multiprocessing as mp

#Never do following! The test process can be halted by student code!
#from my_code import *

started_tests = 0
completed_tests = 0

            
class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        test_code="""
import sys
import datetime
sys.path.insert(0, '../src')

from my_code import train_departure

date=datetime.date(2020, 7, 21)
departure=train_departure('63', 'HAU', date)
print('63:'+str(departure))

date=datetime.date(2020, 10, 23)
departure=train_departure('11', 'PAR', date)
print('11:'+str(departure))

print('Completed')
"""        
        ret=callpythoncode(test_code, timeout=15)
        print('output="""'+ret+'\n"""')

        expected_res=['63:2020-07-21 08:14', '11:2020-10-23 18:44']

        for res in expected_res:
            self.assertTrue(res in ret)

        print('Tests completed')
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

