#TODO - Mark everything up

NB: 
>out = “”
>out += “{\r}.”.format(val)
>out “({})”.format(out.rstrip(‘,’))


NB 
Interning in python
>bar = 26
>foo = 26
>bar is foo
True

>bar = 2000
>foo = 2000
>bar is foo
False

Short strings are also interned

<<Break>>

This code is dangerous

>for item in list _:
>    if item:
>        do_shit

Items can exist, but evaluate to false
Use three value logic: True, False, None
So above “if item” should be “if item is None”

Random thought: should be in markdown. Actually will move over there.

#Working on pytest-demo
##See files there for more detail

unittest supports setup and teardown methods for classes
pytest supports fixtures which 

define the fixture

s flag gives stdout 
>pytest -s 

