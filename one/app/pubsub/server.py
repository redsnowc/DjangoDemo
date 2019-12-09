import socketserver

from base import RedisSubPub


obj = RedisSubPub(password='1234', db=2)


class Server(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            _msg = obj.subscribe()

            while 1:
                msg = _msg.parse_response()

                if msg:
                    self.request.sendall(msg[2])
        except Exception as e:
            print(self.client_address, 'close')

    def setup(self):
        print('before handle, connection {}'.format(self.client_address))

    def finish(self):
        print('finish run after handle')


if __name__ == '__main__':
    host, port = 'localhost', 8888
    server = socketserver.TCPServer((host, port), Server)
    server.serve_forever()
