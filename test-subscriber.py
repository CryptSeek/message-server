"""
Test subscriber file, this is the python implementation of any subscriber.
"""
import zmq as zmq

def main():
    print("Starting subscriber")

    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)

    subscriber.setsockopt(zmq.SUBSCRIBE, b'')
    subscriber.setsockopt(zmq.RCVTIMEO, 600000)

    while True:
        subscriber.connect("tcp://cryptseek.wycre.net:5555")
        print("Subscriber connected")

        while True:
            msg = subscriber.recv_string()
            print(msg)



if __name__ == '__main__':
    main()
