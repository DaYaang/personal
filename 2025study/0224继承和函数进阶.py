"""
@Author  : liuyang
@Time    : 2025/2/24 12:58
@Content : 
"""

class A:
    """当子类和父类都有__init__方法时，只会调用子类的init不会调用父类的
        父类中有实例属性：init中有实例属性
        子类中也有实例属性，那么默认父类中的实例属性不能获取，需要手动调用父类中的init方法才能获取父类的实例属性"""
    num = 100
    def __init__(self):
        self.name = "A类的name属性"
        self.age = "A类的age属性"

    def a(self):
        print("A类的a方法被调用")


class B(A):
    def __init__(self):
        self.sex = "B类的sex属性"
        self.englishname = "B类的age属性"
        # 需要调用父类中的init时需要通过 super 引用
        super().__init__()


b1 = B()
print(b1.name)
