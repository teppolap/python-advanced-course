import socket

buffSize=1024

def fetch_number(IP, p):
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    serverAddress = (IP, p)

    message = "Anna luku!"
    bytesToSend = str.encode(message)
    UDPSocket.sendto(bytesToSend, serverAddress)

    bytesAddressPair = UDPSocket.recvfrom(buffSize)
    response_message = bytesAddressPair[0]

    UDPSocket.close()

    # Palauta paluuviesti muutettuna kokonaisluvuksi
    return int(response_message.decode())


