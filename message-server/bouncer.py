from bottle import Bottle, run, request, response, get, post, template
import requests
import os

# HTTP server to receive messages from clients
app = Bottle()


# Gateway URL
gateway = f'http://{os.environ["GATEWAY_ADDRESS"]}/upload'

def send_to_gateway(message):
    """Hand message off to gateway for transmission to subscribers"""
    print("Sending message to gateway: " + str(message))
    requests.post(gateway, data=message)
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
    print("GATEWAY_ADDRESS =", gateway)
    app.run(
        host='0.0.0.0',
        port=9090,
    )


if __name__ == '__main__':
    main()
