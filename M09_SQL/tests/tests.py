import unittest
from helpers import *
import sqlite3
import os
#Never do following! The test process can be halted by student code!
#from my_code import *

started_tests = 0
completed_tests = 0

            
class TestCode(unittest.TestCase):
    def test_Python(self):
        self.startTest()
        res=callpython(timeout=5)
        
        expected_names=['Matti','Ville','Kaisa','Mikko', 'Urpo', 'Kati', 'Joonas', 'Miisa']
        
        for n in expected_names:
            print('Search '+n)
            self.assertTrue(n in res)
            
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

