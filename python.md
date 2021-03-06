# python
如今，python广泛用于游戏和机器学习。经翻阅 《python 学习手册》、github上一些python内容，整理而得本文。
## 基础
+ 循环
特殊的循环-else

+ 字符串
编码，在cmd运行时，常常需要使用系统使用的编码，比如windows的cmd需要将字符，encoding为gbk。

## 要点
### 迭代

+ 迭代

`iter(variable)`获得对象的迭代器（iterator），用来迭代该对象。
iterator迭代器实现了next函数（python3 是 `__next__`）， 到达末尾时，返回stopiteration异常。使用iterator.next()获取迭代对象的下一个元素。循环语句会自动获取对象的迭代器，并调用迭代器的方法。

+ 列表推导

可以嵌套，且可以伴随一个判断语句。是循环嵌套的语法糖。
```
new_list = [x+y+z for x in 'soe' for y in 'ef' for z in '12']
new_list = [x+y+z for x in 'soe' if x != 's' for y in 'ef' for z in '12']
```
+ 生成器函数（yield）生成器表达式

生成器表达式与列表推导的不同：前者是惰性语法，延迟计算，而后者不是。

生成器函数会被自动编译为生成器对象，添加`__next`成员函数。

### 函数

返回函数的函数成为高阶函数。相当于是对某一函数的加工处理。

**匿名函数的语法**
匿名函数不管多复杂，只能写一行，且执行完结果就是返回值。

```
匿名函数的调用
(lambda x: 2 * x)(8)
```

**函数式编程**

可接收其他函数作为参数的函数称为高阶函数。
```
map/reduce/filter
map(int, ['1', '2',])

```
**闭包 closure**
一个函数返回了一个内部函数，该内部函数引用了外部函数的相关参数和变量，我们把该返回的内部函数称为闭包（Closure）。内部函数为闭包。

函数中定义函数，变量的作用域问题。函数可以访问函数外部的变量。
```
def make_pow(n):
    def inter_func(x):
        return pow(x, n)
    return inter_func
```

使用场景：
1. 需要对一个函数做加工额外的处理。
2. 函数本身需要存储一些参数。相当于类的实例成员函数。

！！使用误区：
a = int(i1) 
```
def count():
    funcs = []
    for i in [1, 2, 3]:
        def f():
            return i
        funcs.append(f)
    return funcs

>>> f1, f2, f3 = count()
>>> f1()
3
>>> f2()
3
>>> f3()
3
```

**装饰器**
用的不多，用的时候经常略有模糊的概念。

### 模块
 
import的逻辑



+ 多线程

Windows 的进程模型和 Linux 不一样，Windows 下没有 os.fork，但是unix有。
Python 提供了一个 multiprocessing 模块，利用它，我们可以来编写跨平台的多进程程序，但需要注意的是 multiprocessing 在 Windows 和 Linux 平台的不一致性。

### 异常处理

**语法简述**

ELSE 是没有异常时运行的代码。python2的语法还允许使用逗号语法，`Exception, e:`.
```
try:
    raise IndexError
except IndexError as e:
    print 'IndexError'
except:
    print 'any error'
else:
    print 'no error'
finally:
    print 'Done'
```

**RAISE**

`raise IndexError`和`raise IndexError()`是等价的，当遇到自定义exception需要传入值进行init时，就使用后者。

在except语句中，可以单独使用`raise`，会向上抛出异常。   

**查看调用栈**

使用traceback，可以清晰地查看python的调用栈。非常有用！！
```
import traceback
traceback.print_stack()
```

+ 源码解读
读、写逻辑是不同的。在类继承等结构中尤其注意。


python的热更

+ 面向对象

slot, super, 类方法


## 杂知识点
+ zip
```
a = [[1,2,3], [1,2,3], [1,2,3]]
b = [[1,2,], [1,2,], [1,2,],]
for i, j in zip(a,b):
    print i, j
```


