##Potential Blog Posts
###For loops
Notorious for being slow, especially wrt to C arrays. Want to do some time testing.
Also want to get a sense of time performance of equality testing wrt to hash table lookup.

Use case of looking for 3, 5, 7 in base 10 numbers
Can find via 
1. set(3, 5, 7)
2. == 3; == 5, == 7
3. number is 3; number is 5; number is 7
4. number in set(3), number in set(5), number in set(7)
5.

##Server 

server = socket.socket(socketoptions)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) <---this allows the operating system to release address when code quits

###chain

server.accept() <--- code hangs
client.connect() <--- connection forms
-----port is passed to ephemeral-- some span of time----


###server setup
1. instantiate socket.socket()
2. set option for releasing
2. bind socket to ADDR
4. listen()
5. return socket

###server run -- accumulator
1. accumulator should come inside loop; should persist in scope of connection

###server testing

from multiprocessing import Process


@pytest.yield_fixture
def server_process():
    process = Process(target=server.start_server)
    process.daemon = True
    process.start()
    yield process

<----when yield from a function, the frame persists on the stack; i.e. the
function and all the local scope variables

###Unit test vs. Functional Test
* unit test works on a single function
* functional tests 

#Http prtotocol
##Interaction
* First a request with initial line, host
* Server responds

##Methods
Most common
* GET, POST, PUT, DELETE
Map to CRUD cycle
* read, write, update, delete --ish
Safe vs. unsafe
* GET is safe
* POST, PUT, DELETE can change data on the server
These are normative distinctions; the server developer's job to get things
to function this way

Idempotence -- request will always have the same response
GET, PUT, DELETE are this
POST is not
Another normative distinction; server developer must ensure that this happens.

##URIs in HTTP
Dynamic/Static -- Map to route names/OR hard uri's

##HTTP/2.0
This is now a thing. It's very different and is gaining traction.

##BDD testing
1. As an anonymous user, cannot edit an entry
2. As a authorized user, I can edit an entry
