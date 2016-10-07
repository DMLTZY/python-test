import hashlib

md5 = hashlib.md5()
md5.update('asdf'.encode())
print(md5.hexdigest())