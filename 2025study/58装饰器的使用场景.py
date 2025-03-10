import time

# 编写一个装饰器，统计 func_print 函数的执行时间
def get_time(need_func):
    def get_local_time():
        start_time = time.time()
        need_func()
        end_time = time.time()
        print(f"函数执行的时间为：{end_time - start_time}")

    return get_local_time

# 装饰器的语法糖格式，用来被装饰的函数定义的上面
@get_time # 语法糖格式等同于func_print = get_time(func_print)
def func_print():
    list1 = []
    for i in range(1, 100001):
        list1.append(i)
    else:  # for循环结束后返回list1列表
        print(len(list1))


func_print()



