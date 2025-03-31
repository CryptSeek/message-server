from bottle import Bottle, run, request, response, get, post, template
import requests
import os
import base64

# HTTP server to receive messages from clients
app = Bottle()


# Gateway URL
gateway = f'http://{os.environ["GATEWAY_ADDRESS"]}/upload'


def send_to_gateway(message):
    """Relay encrypted message to gateway"""
    print("🔒 Sending encrypted message to gateway...")
    encoded_message = base64.b64encode(message.encode()).decode()       # Ensure message is properly encoded
    response = requests.post(gateway, data=encoded_message)
    return response.text


@app.route('/upload', method=['POST'])
def message_received():
    """Receives encrypted messages from users"""
    message_body = request.body.read().decode('utf-8')
    print("Received Encrypted Message:" + str(message_body))

    # Forward message if valid
    if message_body:
        return send_to_gateway(message_body)

    return '500'


def main():
    print("Starting Bouncer...")
    print("GATEWAY_ADDRESS =", gateway)
    app.run(
        host='0.0.0.0',
        port=9090,
        server='gunicorn', workers=4,
    )


if __name__ == '__main__':
    main()
