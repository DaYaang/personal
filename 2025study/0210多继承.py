"""
@Author  : liuyang
@Time    : 2025/2/10 12:47
@Content : 
"""


class A:
    num = 100
    def __init__(self):
        self.name = "A类的属性"

    def a(self):
        print("A类的a方法被调用")

    def b(self):
        print("A类的b方法被调用")

    @classmethod
    def c(cls):
        print("A类中的c类方法被调用")

    @staticmethod
    def d():
        print("A类中的d静态方法被调用")

class B():
    num = 100

    def e(self):
        print("B类中的e方法被调用")

class C(A,B): #多继承

    def f(self):
        print("C类中的f方法被调用")

    def e(self):
        "如果一定要使用父类里面的方法，必须使用super函数调用"
        #在子类的e方法中调用父类a方法
        super().a()

c1 = C()
print(c1.num) #得到的值=100，当遇到属性同名，跟C类继承类的顺序有关，取先继承的类的属性
# 通过 类名.__mro__，或者 类名.mro()方法可以查询类的继承顺序
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(C.mro())

