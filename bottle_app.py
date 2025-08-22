
#Import attributes to help create the page
from bottle import default_app, route, post, get, template

#Create a route to connect the form html file to create the page
@route('/movie')
def movie():
    return template("indexMovie.html")

#Add the subdirectory html page for the bmi conversion
@post('/moviecomp')
def results():
    return template("moviecomp.html")

#Needed to make application work
application = default_app()

