#!/bin/bash

# Activate the virtual environment
source ~/Desktop/mrt-dynamic/mrt-api/venv/bin/activate

# Run the Python 3 application in the background
cd ~/Desktop/mrt-dynamic/mrt-api/
gunicorn --worker-class eventlet -w 1 app:app &

sleep 2
# Start the live server
npx live-server ~/Desktop/mrt-dynamic/mrt-dashboard/

deactivate
