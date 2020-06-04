#
# Docker entry point
#

# start the application server
gunicorn -w 4 -b 0.0.0.0:8080 onefigrapp.wsgi

#
# end of file
#
