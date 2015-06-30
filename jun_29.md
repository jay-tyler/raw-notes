#Upcoming
##Break week
Something about this being the week that we get "broken," to be rebuilt
again in week three.

##Learning Journal
User stories around making edits, permalinks, etc.
Work a little bit each day towards this.

##Code review for Parenthetical
* Most people used a Stack to implement the parenthetical function
* The socre method was a reasonable alternate; Cris thought it was trickier
somehow though

##Going over final work for learning journal
* 

block for authentication
{% if request.authenticated_userid %}

Good templating hard codes route names, not urls. Use snippets like this
to get urls:
{{ request.route_url('add') }}


##Looking at add_entry view in detail

Might be good to refactor, which would allow both post and get to add; also
include some validation code to be sure that valid entries are written. Note
that some code seems to be writing empty strings to the DB.

The following GET/POST for a form is a very common pattern.
```
@view_config(route_name='add', renderer='...jinja2')
def add_entry(request):
    if request method = 'POST'
        #get values
        #check values
        #validate entry, if this fails, want to pass stuff to else
        #redirect to home

    else: 
        Entry()

    return {"entry": entry}

```

#Lightning talk - Jesse - Numerical methods

#TCP/IP and sockets
##TCP/IP stack
###Link layer -- bottom; deals with physical connections between machines
** Packages data for transport
** Executes transmission
** Implement in network interface card (NIC) on computer
###Internet layer
* Responsible for hops; addressing and routing
* Agnostic to physical medium (e.g. IP over Avian carrier - IPoAC)
* This layer makes no promises of reliability
* Addressing systems; IPv4, IPv6
###Transport Layer
* Deals with transmission and reception of data
** Error correction
** Flow control
** Congestion management
* Protocols include TCP and UDP
* Protocols vary in reliability
* Reliability is slow and expensive; edge cases are bank statements (want reliability)
and streaming video (want speed)
* This layer establishes a port
####Ports are sometimes well-known; assigned to particular types of applications
* 0-1023 are reserved ports; these are all bound to particular processes; need admin
* 1024 - 65535 are open ports (2^16 == 16 bit)
* 1024 - 49151 may be registered to particular applications
* 49152 these are called ephemeral ports; OS typically delegates these 
###Application Layer
* Deals directly with data created
* Only cares about endpoint data (IP:Port)

A socket is a software representation of the endpoint.


##Sockets in Python
* UNIX socket is a file pointer that behaves like a socket; exchange data




