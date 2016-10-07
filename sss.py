import os

# print(os.getcwd())

# fileinfo = os.stat(r'C:\Users\zy\Desktop\新建文件夹 (2)\新建文件夹\1.txt')
# for i in (fileinfo.st_ctime_ns, fileinfo.st_atime_ns, fileinfo.st_mtime_ns):
#     print(i)

# os.utime(r'C:\Users\zy\Desktop\新建文件夹 (2)\新建文件夹\1.txt',
#          ns=(1470569671895096400, 1470570999060686000))


# *********************检索文件获取原始时间************************************************
for a, b, c in os.walk(r'C:\Users\zy\Desktop\新建文件夹 (2)'):
    print()
    # print('{}--{}--{}'.format(a, b, c))
    for d in b + c:
        dd = a + '\\' + d
        fileinfo = os.stat(dd)
        print(dd + '--------' + str(fileinfo.st_atime_ns) + '----' + str(fileinfo.st_mtime_ns))
# *********************************************************************

# from urllib.request import urlopen
#
# with urlopen('http://www.baidu.com') as re:
#     for line in re:
#         line = line.decode('utf-8')
#         print(line)
