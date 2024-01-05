import unittest
import socket
import random
from helpers import *
import os 
import time
import multiprocessing as mp

#Never do following! The test process can be halted by student code!
#from my_code import *

import platform
import threading

use_fork=False

started_tests = 0
completed_tests = 0

succeed=0

def client_main(idx):
    global succeed

    localIP="127.0.0.1"
    serverPort=7538
    buffSize=1024

    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #No bindig => Pick random port

    largest_value=0

    UDPSocket.settimeout(10)
    
    for i in range(50):
        maxval=4+3*i
        msg=str(maxval)
        bytesToSend=str.encode(msg)
        serverAddressPort=(localIP, serverPort)
        UDPSocket.sendto(bytesToSend, serverAddressPort)
        bytesAddressPair=UDPSocket.recvfrom(buffSize)
        message=bytesAddressPair[0]
        rc=str(message.decode())
        retval=int(rc)

        assert retval<maxval
        assert retval>=0

        if retval>largest_value:
            largest_value=retval
        
        #print(msg+' :',message.decode())
        #time.sleep(1.0)

    UDPSocket.close()

    assert largest_value>30

    print('Test client '+str(idx)+' passed!')
    succeed=succeed+1

class TestCode(unittest.TestCase):
    def run_clients(self):
        time.sleep(3)
        client_list=[]
        for idx in range(20):
            th=threading.Thread(target=client_main, args=(idx,))
            th.start()
            client_list.append(th)

        for c in client_list:
            c.join()

        global succeed
        print(succeed, 'succesfully served clients, shall be 20!')
        self.assertTrue(succeed>=20)
        print('\n\nNOTE:Client process tests completed succesfully. This is the only test that matters on this assignment.\n\n')
        

    def test_Python(self):
        if (platform.system()!='Windows') and use_fork:
            print('Use fork() to create subprocesses!')
            pid=os.fork()

            if pid!=0: #Parent
                self.startTest()
                self.run_clients()
                self.endTest()
                print('Wait server to exit')
                time.sleep(3)
            else:
                #Forked process, start student server
                callpython(timeout=5)
                #Time.sleep(20)
                print('Server completed!')
                #time.sleep(1)
                #print('\n\nNOTE:Server process tells that \'0 tests completed succesfully\', don\'t worry!\n\n')
                os._exit(os.EX_OK)
        else:
            print('Use multiprocessing to create subprocesses!')
            print('Start server...')
            #mp.set_start_method('spawn')
            p=callpython_subprocess(timeout=5)
            #p.start()
            time.sleep(1)
            print('Start Clients...')
            self.startTest()
            self.run_clients()
            time.sleep(1)
            self.endTest()
            for cp in mp.active_children():
                print(cp)
            
            #p.terminate()
            #p.kill()
            p.join()
            #print(p)
            
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
