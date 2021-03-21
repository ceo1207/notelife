# encoding=utf-8
# 迭代
with open('base.md', 'r') as f:
    F = iter(f)
# F.__next__()
# pythonic的文件读写方式，一次循环返回一行，延迟读取
for line in open('base.md', 'r'):
    pass

# 列表推导
source = 'span'
# python2 diff from python 3
# 2 return a new list, but 3 map func returns a iterator
map(ord, source)
# 在map/reduce等函数，用到回调函数的地方便常出现lambda 匿名函数

new_list = [x+y+z for x in 'soe' for y in 'ef' for z in '12']
new_list = [x+y+z for x in 'soe' if x != 's' for y in 'ef' for z in '12']

# 生成器语句
new_list = (x+y+z for x in 'soe' for y in 'ef' for z in '12')
