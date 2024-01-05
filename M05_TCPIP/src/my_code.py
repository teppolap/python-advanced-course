import socket
import sys
import threading
import random
import time

localIP="127.0.0.1"
serverPort=7538
buffSize=1024


#Write your code here!
def handle_client_request(msg, client_address, server_socket):
    N = int(msg)
    random_number = random.randint(0, N - 1)
    response_msg = str(random_number)
    bytesToSend = str.encode(response_msg)
    server_socket.sendto(bytesToSend, client_address)

def server_main():
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, serverPort))
    print("UDP server up and listening on port", serverPort)

    while True:
        bytesAddressPair = UDPServerSocket.recvfrom(buffSize)
        message = bytesAddressPair[0]
        client_address = bytesAddressPair[1]

        msg = message.decode()
        print("Received request:", msg, "from", client_address)
        handle_client_request(msg, client_address, UDPServerSocket)

if __name__ == "__main__":
    server_main()  

#You can utilize following client for test purposes
def client_main():
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #No bindig => Pick random port

    for i in range(10):
        msg=str(4+3*i)
        bytesToSend=str.encode(msg)
        serverAddressPort=(localIP, serverPort)
        UDPSocket.sendto(bytesToSend, serverAddressPort)
        bytesAddressPair=UDPSocket.recvfrom(buffSize)
        message=bytesAddressPair[0]

        print(msg+' :',message.decode())
        #time.sleep(1.0)

    UDPSocket.close()

#Set True to run the clients
run_client=False

if run_client:
    th_list=[]
    for i in range(10):
        th_list.append(threading.Thread(target=client_main))
        th_list[-1].start()

    for th in th_list:
        th.join()