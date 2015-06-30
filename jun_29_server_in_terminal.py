# coding: utf-8
get_ipython().magic(u'clear ')
import socket
server = socket.socket(socket.AF_INET, socket.SOCKET_STREAM, socket.IPPROTO_IP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
server
address =('127.0.0.1', 8000)
server.bind(address)
#Has an address to listen on, but needs to be turned on to listen
server.listen(1)
#Argument is the number of something it will buffer while setting up
client_connection = server.accept()
client_connection
#Notice the port number; used ephemeral socket
#Doesn't want to block up a port 8000; needs to handle multiple clients
client_connection
conn, addr = client_connection
conn.recv(16)
#recieve 16 bytes
conn.recv(16)
conn.recv(16)
#less than 16 byte; message is done
conn.sendall("Things are not bad; how's bout' you?")
conn.recv(16)
conn.close()
get_ipython().magic(u'ls ')
get_ipython().magic(u'run server.py')
get_ipython().magic(u'run server')
get_ipython().magic(u'ls ')
get_ipython().magic(u'ls [1]')
get_ipython().magic(u'run server.py')
get_ipython().magic(u'run server.py')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mv client.py client.py')
get_ipython().magic(u'mv server.py server.py')
get_ipython().magic(u'mv "\'u\'server.py" server.py')
get_ipython().magic(u'ls ')
get_ipython().magic(u'mv socket.py server.py')
get_ipython().magic(u'run server.py')
get_ipython().magic(u'run server.py')
