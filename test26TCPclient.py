import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 12345))
info = s.recv(1024)
print(info.decode('utf-8'))
while True:
    mes = input('> ')
    if mes == 'qq':
        break
    s.send(mes.encode('utf-8'))
    data = s.recv(1024)
    print('I receive >> {}'.format(data.decode('utf-8')))
