# encoding=utf-8
# 迭代
f = open('base.md', 'r')
F = iter(f)
F.__next__()

# 列表推导
source = 'span'
# python2 diff from python 3
# 2 return a new list, but 3 map func returns a iterator
map(ord, source)
# 在map/reduce等函数，用到回调函数的地方便常出现lambda 匿名函数

new_list = [x+y+z for x in 'soe' for y in 'ef' for z in '12']
new_list = [x+y+z for x in 'soe' if x != 's' for y in 'ef' for z in '12']

# 生成器函数
