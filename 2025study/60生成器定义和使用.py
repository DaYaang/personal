def func1():
    print(1)
    print(2)
    print(3)
    print(4)
    return 5
    print(6)
    print(7)

# 函数一旦被调用，会从头开始执行函数里面的代码块
# 函数里面一旦有return，那么会结束当前函数的执行并携带返回值
# print(func1())

# 当函数中有yield关键字时，就是生成器
def func2():
    print(1)
    print(2)
    print(3)
    print(4)
    yield 5
    # 执行到 yield 时，会结束本次生成器的执行，并携带返回值
    # 当使用生成器对象通过next内建函数调用时，下次调用会从yield下面开始
    print(6)
    print(7)
    yield 8
    print(9)
    yield 10

# 生成器的需要使用next()函数进行调用
# next(func2())

# 一般会将生成器引用进行赋值，然后再使用next()内建函数调用，下次调用会从 yield 下面开始
fn2 = func2()
print("第一次调用生成器")
print(next(fn2))
print("第二次调用生成器")
print(next(fn2))
