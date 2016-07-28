from socketIO_client import SocketIO, LoggingNamespace, BaseNamespace


class Namespace(BaseNamespace):

    def on_connect(self):
        print('[Connected]')

    def on_location(self, msg):
        print('test: ', msg)

if __name__ == "__main__":
    with SocketIO('localhost', 8000, Namespace) as socketIO:
        socketIO.wait_for_callbacks(seconds=1)
        socketIO.wait(10)
