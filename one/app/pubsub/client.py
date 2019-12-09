import socket


def work():
    client = socket.socket()
    client.connect(('localhost', 8888))

    while 1:
        msg = client.recv(1024)
        print(msg)

    client.close()


if __name__ == '__main__':
    work()
