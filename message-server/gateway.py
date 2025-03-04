"""
CryptSeek Gateway server, handles sending messages to all subscribers
"""
from bottle import Bottle, run, request, response, get, post, template
import gevent
import zmq.green as zmq

# Set up Bottle/gevent interaction
from gevent import monkey
monkey.patch_all()

app = Bottle()

# Create ZeroMQ publisher socket
context = zmq.Context()
socket = context.socket(zmq.PUB)

def push_message(content):
    """Spawned as a greenlet to push messages through ZMQ"""
    print("Pushing Message: " + str(content))
    message = str(content).encode("utf-8")
    socket.send(message)
    return 'OK\n'


@app.route('/upload', method=['POST'])
def upload():
    """Receives messages from the bouncer and sends them to all subscribers"""
    message_body = request.body.read().decode("utf-8")

    print("Gateway Received: " + str(message_body))

    return gevent.spawn(push_message, message_body)


def main():
    print("Starting Gateway")
    socket.bind("tcp://0.0.0.0:5555")

    app.run(
        host='0.0.0.0',
        port=9091,
        server='gevent',  # Register gevent integration with Bottle
    )


if __name__ == '__main__':
    main()
