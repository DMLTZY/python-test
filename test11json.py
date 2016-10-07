# import pickle
#
# d = dict(name='zy', age=12)
# f = open('a.txt', 'wb')
# pickle.dump(d, f)
# f.close()
#
#
# f = open('a.txt', 'rb')
# c = pickle.load(f)
# f.close()
# print(c)
# ----------------------------------------------
import json

d = dict(name='zy', age=23)
f = open('a.txt', 'w')
json.dump(d, f)
f.close()


f = open('a.txt', 'r')
c = json.load(f)
f.close()
print(c)
