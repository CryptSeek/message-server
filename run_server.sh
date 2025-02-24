#!/bin/bash

# Start script for the server, the SERVER_TYPE environment variable must be set to either 'bouncer' or 'gateway'

# Check if SERVER_TYPE is set
if [ -z "$SERVER_TYPE" ]; then
    echo "Error: SERVER_TYPE environment variable is not set."
    exit 1
fi

# Determine which script to run
case "$SERVER_TYPE" in
    "bouncer")
        echo "Starting Bouncer server..."
        python3 message-server/bouncer.py
        ;;
    "gateway")
        echo "Starting Gateway server..."
        python3 message-server/gateway.py
        ;;
    *)
        echo "Error: Unknown SERVER_TYPE '$SERVER_TYPE'. Use 'bouncer' or 'gateway'."
        exit 1
        ;;
esac
