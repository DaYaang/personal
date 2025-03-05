"""
@Author  : liuyang
@Time    : 2025/3/5 12:47
@Content : 匿名函数
"""

# 定义匿名函数使用lambda关键字
# lambda x,y:x+y
# x和y代表形参，x+y是返回值
# 把匿名函数当做一个整体使用（）进行调用传递实参
# 有参数就需要传递参数
# 不需要使用return也有返回值
print((lambda x,y:x+y)(3,5))
# 将匿名函数的引用进行传递，然后调用
fun1 = lambda  x,y:x+y
print(fun1(4,7))
# 匿名函数主要的功能是完成简单的函数构造来实现简单的逻辑

