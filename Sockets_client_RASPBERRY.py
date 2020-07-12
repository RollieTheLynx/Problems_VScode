#https://www.futurelearn.com/courses/networking-with-python-socket-programming-for-communication/2/steps/791359

#%%
import socket

def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open:
        # read any data from the socket
        data = receiving_socket.recv(1024)
        '''The data is received or read from the client_socket using client_socket.recv(1024). 
        The value 1024 is the maximum number of bytes that should be read at one time. 
        If more than 1,024 bytes had been sent, subsequent calls to recv would receive the rest of the data.'''

        # if no data is returned the socket must be closed
        if not data:
            socket_open = False

        # add the data to the buffer
        buffer = buffer + data.decode()
        '''The data received by the socket is a stream of bits and needs to be decoded to a string using decode() 
        so that it can be printed to the screen.'''

        # is there a terminator in the buffer
        terminator_pos = buffer.find("\n")
        # if the value is greater than -1, a \n must exist
        while terminator_pos > -1:
            # get the message from the buffer
            message = buffer[:terminator_pos]
            # remove the message from the buffer
            buffer = buffer[terminator_pos + 1:]
            # yield the message (see below)
            yield message
            # is there another terminator in the buffer
            terminator_pos = buffer.find("\n")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8081))
print("Connected")

for message in get_text(client_socket):
    print(message)
    if message == 'Hello, thanks for connecting':
        reply = "Send nudes"
        data = reply.encode()
        client_socket.send(data)


client_socket.close()