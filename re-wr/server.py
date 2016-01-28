import sys
import socket
import select
HOST = ''
SERVER_LIST = []
PORT = 6000
RECV_BUFFER = 4096
def server():
    #create socket 
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #parse socket layer, lets you reuse address
    #Bind host/port
    ser_socket.bind(HOST, PORT))
    #start listening
    ser_socket.listen(10)
    #change socket to readable text
    SERVER_LIST.append(ser_socket)
    print("Starting server connection listening on port:", str(PORT))
    while 1:
        #create variable to handle info
        ready_to_read, ready_to_write, in_error = select.select(SERVER_LIST, [],[],0)
        #for each incoming socket
        for sock in ready_to_read:
            #new connection request
            if sock == ser_socket:
                sockfd, addr = ser_socket.accept()
                SERVER_LIST.append(sockfd)
                print("Client: (%s, %s) " % addr)
                broadcast(ser_socket,sockfd, "[%s:%s] entered our chatting room\n" % addr)
            #if already known connecion
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        #if anything in socket
                        broadcast(ser_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                    else:
                        #socket is broken, remove
                        if sock in SERVER_LIST:
                            SERVER_LIST.remove(sock)
                        broadcast(ser_socket, sock, "Client (%s, %s) is offline\n" % addr)
                except:
                    broadcast(ser_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue
    ser_socket.close()
    """The broadcast method is to tell all the clients the incoming messages"""
def broadcast(ser_socket, sock, message):
    for socket in SERVER_LIST:
        if socket != sock and socket != sock:
            try:
                socket.send(message)
            except:
                #Broken socket connection
                socket.close()
                #Remove it
                if socket in SERVER_LIST:
                    SERVER_LIST.remove(socket)
if __name__ == "__main__":
    sys.exit(server())
