# 报错和异常
while True:
    try:
        x = int(input("Please enter a number:"))
    except ValueError:
        print("oops! 请输入一个数字")
