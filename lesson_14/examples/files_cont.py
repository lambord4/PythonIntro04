# file = open('test.txt', 'r', encoding='utf-8')
#
# print(file)
# # txt = file.read()
# # print(txt)
# # ------------------------------
# # file.readline()
# # file.readline()
# # file.readline()
# # line = file.readline()
# # print(line)
# # ------------------------------
# # for line in file:
# #     print(line, end='')
# # ------------------------------
# print(file.tell())
# print(file.readline(), end='')
# print(file.tell())
# file.seek(0, 0)
#
# print(file.tell())
# print(file.readline(), end='')
# print(file.tell())
#
# file.seek(0, 2)
# print(file.tell())
#
# file.seek(0, 0)
# print(file.tell())
# file.seek(127, 0)
# print(file.tell())
# print(file.readline(), end='')
#
# '''
#     0 - of start (begin)
#     1 - of current position
#     2 - of end
#
#     seek() - change current position
#     tell() - get current position
# '''
#
# file.close()

'''
    r - read
    w - write
    x - exclusive
    a - append
    
    + - mix
    t - text
    b - binary
'''

# with open('test.txt', 'r', encoding='utf-8') as file:
#     print('File closed' if file.closed else 'File is open')
#     print(file.read())
#
# print('File closed' if file.closed else 'File is open')


size_buff = 1024
with open('40975e.jpg', 'rb') as src, open('result.jpg', 'wb') as dst:
    while True:
        data = src.read(size_buff)
        if data:
            dst.write(data)
        else:
            break
