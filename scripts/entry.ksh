#
# Docker entry point
#

# start the application server (startup is slow so increase timeout)
gunicorn -w 4 -b 0.0.0.0:8080 --timeout 120 --log-level debug onefigrapp.wsgi

#
# end of file
#
