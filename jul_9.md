##view callable for ajax
@view_config(route_name='edit', xhr=True, renderer='json')
Use the renderer predicate to handle the json. Order matters; use the more
specific one first.
This is one of these things that is easy in pyramid; devilshly hard in 
other frameworks. 