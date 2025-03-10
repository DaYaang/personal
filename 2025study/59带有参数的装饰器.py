#  带有参数的装饰器
# 目前使用的装饰器本身是有且仅有一个形参，这个形参用来接收被装饰的函数的引用

#目前加减法的函数，没有对应的符号进行判断再输出内容
def mark(flag):
    def out_func(need_func): # need_func 此时代表要运行的函数add、sub
        def inner_func(num1,num2):
            print(f"输入的装饰器实参为{flag}，正在计算中。。。")
            print(f"两个数字的运算结果为:{need_func(num1,num2)}")
        return inner_func
    return out_func

@mark("+")
def add(a,b):
    return a+b

@mark("-")
def sub(a,b):
    return a-b


add(3,4)
