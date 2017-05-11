import cgi, cgitb

form = cgi.FieldStorage()
band_url = form.getvalue('url')

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"
