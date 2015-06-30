# coding: utf-8
get_ipython().magic(u'clear ')
ipython
get_ipython().magic(u'clear ')
import socket
dir(socket)
socket.IPPROTO_IP
socket.IPPROTO_STREAM
[name for name in socket if name.startswith('IPPROTO')]
[name for name in dir(socket) if name.startswith('IPPROTO')]
foo =[name for name in dir(socket) if name.startswith('IPPROTO')]
foo
my_socket = socket.socket()
my_socket.type
my_socket.family
my_socket.proto
families = [name for name in dir(socket) if name.startswith('AF_')]
families
for fam in families:
    print getattr(socket, fam)
    
for fam in families:
    print getattr(socket, fam)
print fam
for fam in families:
    print getattr(socket, fam)
    print fam
    
types = [name for name in dir(socket) if name.startswith('SOCK_')
]
types
my_socket.type
socket.SOCK_STREAM
#if we set up a socket without args, will get an IPv4 one with sock_stream
my_socket.proto
protocols = [name for name in dir(socket) if name.startswith('IPPROTO_')]
protocols
for p in protocols:
protocols
my_socket
#before connnecting to another socket, want family, type, and  protocol
socket.getservbyname('http')
socket.getservbyname('smtp')
socket.gethostbyname('google.com')
socket.gethostbyname('google.com')
socket.getaddrinfo('google.com')
socket.getaddrinfo('google.com', 'http')
#(type, family, protocol, (IP, port))
addrinfo = (2, 1, 6, '', ('74.125.25.139', 80) 
)
addrinfo
google_sock = socket.socket(*addrinf[:3])
google_sock = socket.socket(*addrinfo[:3])
google_sock.type
google_sock.family
google_sock.proto
#We have now built a socket that will talk to the google socket
google_sock.connect(addrinfo[-1])
msg = "GET / HTTP/1.1\r\nHOST: me.you.com\r\n\r\n"
msg
#Must always sent byte strings to a socket
#Must always send* byte strings to a socket
google_sock.sendall(msg)
google_sock.recv(1024)
response = google_sock.recv(1024)
response = __
response
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STEAM, socket.IPPROTO_IP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
address = ('127.0.0.1', 8000)
client.connect(address)
client_socket.connect(address)
client.sendall('Hey there, server. How\'s it hanging?')
client_socket.sendall('Hey there, server. How\'s it hanging?')
client_socket.recv(16)
client_socket.recv(16)
client_socket.recv(16)
#What if we recieve a last message of 16 bytes, exactly?
client.shutdown(socket.SHUT_WR)
client_connection.shutdown(socket.SHUT_WR)
client_socket.shutdown(socket.SHUT_WR)
#Done writing; this connection will never be used again
client_socket.close()
get_ipython().magic(u'run client.py')
get_ipython().magic(u'ls ')
get_ipython().magic(u'run client.py')
