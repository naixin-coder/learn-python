# 模块

# import fibo
# fibo.fib(100)
# print(fibo.fib2(100))
# print(fibo.__name__)

from packages.pageage01.hello import hello
from packages.pageage02.say import say
import fibo
# import fib, fib2
# fib(100)
# print(fib2(100))

print(__name__)
print(dir())

# 包


hello('python')

say("Python is easy")
