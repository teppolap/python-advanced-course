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

        db_file='src/my_db.db'
        try:
            os.remove(db_file)
        except:
            pass
        
        ret=callpython(timeout=5)
        
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        res = cur.execute('SELECT name FROM texttable')

        names=[]
        expected_names=['Matti','Ville','Kaisa','Mikko']
        
        for row in res:
            names.append(row[0])

        for n in expected_names:
            print('Search '+n)
            self.assertTrue(n in names)
            
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

