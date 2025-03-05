class file:
    def __init__(self):
        self.name = input("输入电影名")
        self.director = input("输入导演")
        self.time = input("输入电影时长")

    def file_name(self):
        print("输入的电影名是：",self.name)

    def file_director(self):
        print("输入的电影导演是：",self.director)

    def file_time(self):
        print("输入的电影时长是：",self.time)

user1 = file()
user1.file_name()
user1.file_director()
user1.file_time()

class Coder:
    def __init__(self):
        self.money = 1000
    def woker(self):
        print("调用coder类工作方法")
    def sleep(self):
        print("调用coder类睡觉方法")
    def inmagine(self):
        print("调用coder类幻想方法")

class Xiaowang(Coder):
    def __init__(self):
        self.company = "程序员"

    def show_company(self):
        print("调用Xiaowang类的展示公司方法")
        self.woker()

xiaowang = Xiaowang()
xiaowang.show_company()
