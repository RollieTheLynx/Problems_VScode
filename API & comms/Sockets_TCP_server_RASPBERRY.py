#https://www.futurelearn.com/courses/networking-with-python-socket-programming-for-communication/2/steps/791359

import socket

def send_text(sending_socket, text):
    text = text + "\n"
    data = text.encode()
    '''The encode() function uses the character encoding standard utf-8 to encode each character in the message string 
    variable into a series of bytes. You can encode your data using different encoding standards, 
    for example message.encode("base64"), which is useful when dealing with non-text data.'''

    sending_socket.send(data)
    '''The connection_socket is the socket that is paired and connected to the client socket. 
    Note that this is different to the server_socket, which is used to listen for and accept connections, not use them.'''


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''The parameters socket.AF_INET and socket.SOCK_STREAM determine the type of socket and protocol to be used.
In this case, AF_INET specifies Internet Protocol version 4 and SOCK_STREAM denotes TCP, so a TCP/IP socket is created.'''

server_socket.bind(("0.0.0.0", 8081))
'''"0.0.0.0" will bind the socket to all network IP addresses available on this computer.

8081 determines the TCP port your socket should use.
Ports are typically used to identify the purpose of the connection and can be any number between 0 and 65535. Ports 0 to 1023 are well known ports that are usually restricted for specific uses: for example, port 80 is HTTP and shouldn’t really be used.
I chose 8081 as it’s typically used for testing, but you could pick any number you wanted.'''

server_socket.listen()
print("Waiting for connection")
connection_socket, address = server_socket.accept()
print("Client connected")

message = "Hello, thanks for connecting"
send_text(connection_socket, message)

data2 = connection_socket.recv(1024)
message2 = data2.decode()
print(message2)

connection_socket.close()
server_socket.close()

