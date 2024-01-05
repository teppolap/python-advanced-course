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
            'Got TypeError exception - ok',
            'Test ForwardClass.__str__(): value="1234567890"',
            'Test BackwardClass.__str__(): value="0987654321"',
            'Test ForwardClass.__str__(): value="1234"',
            'Test BackwardClass.__str__(): value="4321"',
            'Test ForwardClass.__str__(): value="[1, \'ab\', 3.14159265]"',
            'Test BackwardClass.__str__(): value="]56295141.3 ,\'ba\' ,1["',
            'Test ForwardClass.print(): 1234567890',
            'Test BackwardClass.print(): 0987654321'
        ]
        
        my_code="""
import sys
sys.path.insert(0, '../src')

from my_code import BaseClass, ForwardClass, BackwardClass


if True:
    try:
        print('Trying to create BaseClass object...', end=' ')
        b=BaseClass('s')
    except TypeError:
        print('Got TypeError exception - ok')

    for test_value in ['1234567890', 1234, [1, 'ab', 3.14159265]]:
        print(32*'-')
        print('Create ForwardClass('+str(test_value)+')')
        fw=ForwardClass(test_value)
        print('Test ForwardClass.print():', end=' ')
        fw.print()
        print('Test ForwardClass.__str__():', end=' ')
        s=str(fw)
        print('value="'+s+'"', end=' ')
        assert s==str(test_value)
        print('ok ')

        print(32*'-')

        print('Create BackwardClass('+str(test_value)+')')
        bw=BackwardClass(test_value)
        print('Test BackwardClass.print():', end=' ')
        bw.print()
        print('Test BackwardClass.__str__():', end=' ')
        s=str(bw)
        bw_testvalue=str(test_value)[::-1]
        print('value="'+s+'"', end=' ')
        assert s==bw_testvalue
        print('ok ')
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

