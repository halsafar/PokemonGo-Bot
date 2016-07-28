from socketIO_client import SocketIO, LoggingNamespace, BaseNamespace


"""
Just a simple socketIO client.
Echo's whatever events it receives to the screen.
"""


class Namespace(BaseNamespace):

    def on_connect(self):
        print('[Connected]')

    def on_location(self, msg):
        print('test: ', msg)


if __name__ == "__main__":
    try:
        with SocketIO('localhost', 8000, Namespace) as socketIO:
            while True:
                socketIO.wait_for_callbacks(seconds=1)
    except (KeyboardInterrupt, SystemExit):
        print "Exiting"
