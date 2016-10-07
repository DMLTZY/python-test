import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))
for data in [b'**one**', b'**two**', b'**three**']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

print('I will finish...')
s.send(b'exit')
s.close()