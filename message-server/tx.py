from bottle import Bottle, run, request, response, get, post, template
import zmq as zmq

app = Bottle()

context = zmq.Context()
socket = context.socket(zmq.PUB)

@app.route('/push', methods=['POST'])
def push_message():
    message_body = request.body.read()
    socket.send(message_body)

def main():
    socket.bind("tcp://*:5555")

    app.run(
        host='0.0.0.0',
        port=9091,
    )


if __name__ == '__main__':
    main()
