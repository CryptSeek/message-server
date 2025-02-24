# CryptSeek Message Server
This is the server for the CryptSeek Messenger app.

## Deployment
The best way to deploy this is with Docker / Docker Compose. Dockerfile and `docker-compose.yml` coming soon.

### [`run_server.sh`](run_server.sh)
This script will launch either of the servers depending on the `SERVER_TYPE` environment variable.

## Design
Inside the [`message-server`](message-server) package, there are two servers written in python: `bouncer` and `gateway`

### Bouncer
The bouncer uses Bottle to create an HTTP server exposing the `/upload` path to POST requests. 
The body of a POST request is sent to the `gateway` server for transmission to subscribers.

Currently, no data processing or handling is performed on the incoming data, this will change in the future.

### Gateway
The gateway creates a ZeroMQ socket in Publish mode to send data out to subscribers. 
To enable synchronous sending of messages, we use `gevent` to spawn greenlets for every message the gateway must send.
The gateway does maintain a Bottle server to work with `gevent` and to receive messages from the bouncer.
Ideally the gateway should perform no checking, leaving that to the bouncer.

The REST interface for the gateway needs to be isolated using firewalls or network isolation, otherwise users can bypass
the bouncer and send messages directly to the server.

## Test file
The [`test-subscriber.py`](test-subscriber.py) file contains a reference implementation for a subscriber of the server.