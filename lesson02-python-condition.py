# Python 流程
# x = int(input())
x = 65

# if 语句
if x < 60:
    print("不及格")
elif x >= 60 and x <= 90:
    print("及格")
else:
    print("优秀")

# for 语句
words = ['cat', 'window', 'defenestrate']
for w in words:
    if (w == 'cat'):
        print("cat")

# range函数
for i in range(0, 5):
    print(i)
# break continue else

for i in range(0, 5):
    for n in range(3, 7):
        if i == 2 and n == 4:
            break
        if i == 1:
            continue
    else:
        print(i, n)

# pass 语句
# while True:
#     pass

# match语句


def http_error(status):
    match status:
        case 400:
            return "服务器访问失败!"
        case 404:
            return "找不到服务器或者文件"
        case 500:
            return "服务器错误"
        case _:
            return "服务器发生不知名错误"


status = http_error(400)
print(status)

# 定义函数


def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print(fib(100))

# 解包
args = [3, 6]
list = list(range(*args))  # 列表解包
print(list)


def book(name, price):
    print("Book name:", name, ",Book price:", price)


args2 = {"name": "Python", "price": 50}
book(**args2)

# Lambda表达式


def make_incrementor(n):
    return lambda x: x+n


f = make_incrementor(42)
print(f(1))
