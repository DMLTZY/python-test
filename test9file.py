with open('a.txt', 'wb') as f:
    f.write('张'.encode('utf-8'))

with open('a.txt', 'rb') as f:
    print(f.read())


print(ord('张'))

print(u'24352'.decode('utf-8'))


print(int('111001011011110010100000', 2))


