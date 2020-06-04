#
# Docker entry point
#

# start the application server
#gunicorn --worker-class gevent -w 4 -b 127.0.0.1:8080 onefigrapp.wsgi
#gunicorn --worker-class eventlet -w 4 -b 0.0.0.0:8080 onefigrapp.wsgi

# debug server for now...
python3 manage.py runserver 0.0.0.0:8080

#
# end of file
#
