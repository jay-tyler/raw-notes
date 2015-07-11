##view callable for ajax
@view_config(route_name='edit', xhr=True, renderer='json')
Use the renderer predicate to handle the json. Order matters; use the more
specific one first.
This is one of these things that is easy in pyramid; devilshly hard in 
other frameworks. 

##
session.query(cls).get(eid)   <---   This one will return an Entry or None
...               .filter(cls.id==eid).one()   <---   This one will throw an err if none or > 1

##
Organizing the markdown into the Entry class
@property
def mkdwn(self)
    return markdown(self.text)

##Python packaging -- Cris is taking a screencast here
* def of a package -- any folder containing __init__.py
* __init__.py does not necessarily have to contain anything at all
* each other py file in directory becomes an importable module

##History
distutils then setuptools to extend it
use a setup.py
    from setuptools import setup

setup(
)

#pip install -e git [uri]