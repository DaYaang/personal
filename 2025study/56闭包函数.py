"""
@Author  : liuyang
@Time    : 2025/3/5 13:03
@Content : 闭包函数
闭包的构成条件
闭包的语法结构
闭包的定义和使用
"""
# 闭包的定义：在定义一个函数的时候，嵌套了另外的函数，而且内部函数使用了外部函数的变量，并且外部函数返回了内部函数的名字（内部函数的引用）
# 闭包的核心：是内部函数使用了外部函数的变量，这个过程叫闭包
# 意义：函数在被调用完之后，函数内部的局部变量会被销毁，为了方便保存以及使用函数外部的变量，可以使用闭包的形式进行调用

def func_out(num1):
    def func_inner(num2):
        result = num1+num2
        print(f"外部函数的num1：{num1}，内部函数的num2：{num2}，相加结果：{result}")
    return func_inner  # 外部函数返回内部函数的引用，不带（）代表引用

# 函数只有调用的时候才会执行，定义的时候不会执行
f1 = func_out(6) # 此时f1代表传递了num1=6，且f1等同于引用了func_inner函数
f1(8) # 此时 f1(8) 等同于调用func_inner(8)函数，且将num2传入8

# 简写
func_out(6)(8)
