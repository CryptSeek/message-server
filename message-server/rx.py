from bottle import Bottle, run, request, response, get, post, template

app = Bottle()

def mirror_message(message_body):
    # TODO mirror to tx server
    print(message_body)
    return 'OK'


@app.route('/rx', method=['OPTIONS', 'POST'])
def message_received():
    data_key = request.forms.get('data')
    if data_key:
        message_body = data_key
    else:
        message_body = request.body.read()
    return mirror_message(message_body)

def main():
    app.run(
        host='0.0.0.0',
        port=9090,
    )


if __name__ == '__main__':
    main()
