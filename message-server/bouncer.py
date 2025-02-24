from bottle import Bottle, run, request, response, get, post, template
import requests

# HTTP server to receive messages from clients
app = Bottle()


def send_to_gateway(message):
    """Hand message off to gateway for transmission to subscribers"""
    print("Sending message to gateway: " + str(message))
    requests.post("http://localhost:9091/upload", data=message)
    return 'OK\n'

@app.route('/upload', method=['POST'])
def message_received():
    """Handles incoming messages from users"""
    message_body = request.body.read()
    print("Unformatted Message: " + str(message_body))

    # Mirror the message to connected clients
    if message_body:
        return send_to_gateway(message_body)

    return '500'

def main():
    print("Starting Bouncer")
    app.run(
        host='0.0.0.0',
        port=9090,
    )


if __name__ == '__main__':
    main()
