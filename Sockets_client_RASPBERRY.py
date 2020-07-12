#https://www.futurelearn.com/courses/networking-with-python-socket-programming-for-communication/2/steps/791359

#%%
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8081))
print("Connected")

data = client_socket.recv(1024)
'''The data is received or read from the client_socket using client_socket.recv(1024). The value 1024 is the maximum number of bytes that should be read at one time. 
If more than 1,024 bytes had been sent, subsequent calls to recv would receive the rest of the data.'''

message = data.decode()
'''The data received by the socket is a stream of bits and needs to be decoded to a string using decode() so that it can be printed to the screen.'''

print(message)

if message == 'Hello, thanks for connecting':
    reply = "Send nudes"
    data = reply.encode()
    client_socket.send(data)


client_socket.close()