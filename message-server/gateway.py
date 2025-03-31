"""
CryptSeek Gateway server, handles sending messages to all subscribers
"""
from bottle import Bottle, run, request, response, get, post, template
import gevent
import zmq.green as zmq
import base64

# Set up Bottle/gevent interaction
from gevent import monkey
monkey.patch_all()

app = Bottle()

# Create ZeroMQ publisher socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")       # Port for clients to receive messages


def push_message(encoded_content):
    """Spawned as a greenlet to push messages through ZMQ"""
    print("Relaying Encrypted Message...")
    message = base64.b64decode(encoded_content).decode("utf-8")
    socket.send_string(message)         # Relay message as-is


@app.route('/upload', method=['POST'])
def upload():
    """Receives messages from the bouncer and sends them to all subscribers"""
    encoded_message = request.body.read().decode("utf-8")

    print("Gateway Received Encrypted Message")

    gevent.spawn(push_message, encoded_message)

    return 'OK\n'


def main():
    print("Starting Gateway...")

    app.run(
        host='0.0.0.0',
        port=9091,
        server='gevent',  # Register gevent integration with Bottle
    )


if __name__ == '__main__':
    main()
