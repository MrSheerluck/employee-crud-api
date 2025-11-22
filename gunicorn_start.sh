# gunicorn_start.sh
#!/bin.bash

NAME="employee_crud_api"
DJANGODIR=/home/ubuntu/employee_crud_api  # Update this path if needed
VENVDIR=$DJANGODIR/venv
SOCKET=$DJANGODIR/gunicorn.sock
USER=ubuntu
GROUP=ubuntu
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=config.settings
DJANGO_WSGI_MODULE=config.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
source $VENVDIR/bin/activate

# Start Gunicorn
exec $VENVDIR/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKET \
  --log-level=info \
  --log-file=-