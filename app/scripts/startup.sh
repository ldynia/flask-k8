#!/bin/ash

CONTAINER_IP=$(ip addr | grep inet | tail -n1 | awk '{print $2}' |  cut -d'/' -f1)
echo "Container IP: $CONTAINER_IP"

echo "Install requirements.txt"
pip install --upgrade pip
pip install -r /app/requirements.txt --no-cache-dir

# is $@ empty
if [ -z "$@" ]
then
    echo "Run App"
    flask run --host=$HOST --port=$PORT
else
    echo "Executeing \$@ command: $@"
    exec $@
fi