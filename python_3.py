# coding=utf-8
# author: kayi
# date: 2021/3/21
# 异常相关
def fetch_value(a, index):
    return a[index]


tmp_string = 'father'
# print fetch_value(a, 10)

# try:
    # 主动触发异常
    # raise IndexError
    # assertion error
    # assert 1 != 1
# except IndexError as index_error:
#     print 'there is an IndexError'


# 不写except 就不会捕获异常
# try:
#     raise IndexError
# finally:
#     print 'Done'

try:
    raise IndexError
except IndexError as e:
    print 'IndexError'
    print e
except:
    print 'any error'
else:
    print 'no error'
finally:
    print 'Done'

