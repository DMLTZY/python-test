import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host, port))
s.listen(1)

while True:
    print("I'm server, I'm ready...")
    sock, addr = s.accept()
    print('{} has connnent...'.format(addr))
    sock.send(b'You have connented, input something')
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.send(('HELLO:' + data.decode('utf-8')).encode('utf-8'))
    sock.close()