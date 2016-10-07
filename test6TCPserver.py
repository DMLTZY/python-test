import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))

s.listen(1)
print('WAITING FOR CONNECTION...')


def han(sock, addr):
    print('ACCEPT NEW CONNECTION FROM {}'.format(addr))
    sock.send(b'WELCOME..')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('HELLO, {}'.format(data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print('CONNENTION IS CLOSED')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=han, args=(sock, addr))
    t.start()