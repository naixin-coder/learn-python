# 作用域和命名空间
# spam = ""


# def scope_test():

#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         spam = "nonlocal spam"

#     def do_global():
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)


# scope_test()
# print("In global scope:", spam)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  # nonlocal 会立即绑定值，作用域在上一级的作用域
        spam = "nonlocal spam"

    def do_global():
        global spam  # global 会作用于全局作用域，不会立即绑定值
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


# 无参数构造器
class MyClass:
    i = 12345

    def f(self):
        return "hello world"


myclass = MyClass()
print(myclass.f())


class Area:
    area = 0

    def __init__(self, width, height):
        self.area = width * height


area = Area(10, 10)

print(area.area)


# 继承
class Animal:
    def run(self):
        print("run ~~~")

    def eat(self):
        print("eat ~~~")


class Dog(Animal):
    __name = ''

    def __init__(self, name):
        self.__name = name

    def hello(self):
        print(f'{self.__name} say: Hello')

    def run(self):
        print('dog run ~~~')


dog = Dog('docky')
# print(dog.__name)
dog.run()
dog.eat()
dog.hello()
