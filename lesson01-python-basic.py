# number
num1 = 2 + 2
# 数字 加法 // 4
num2 = 50 - 5 * 6
# 数字 乘法 // 20
num3 = 8 / 5
# 数字 除法 // 1.6
num4 = 17 // 3
# 数字 整除舍弃小数部分 // 5
num5 = 17 % 3
# 数字 取余 // 2
num6 = 5 ** 2
# 数字 乘方 // 25


# 字符串
str1 = 'spam egg'
# 字符串 基本字符串 // spam egg
str2 = 'doesn\'t'
# 字符串 转义字符串 // doesn't
print(r'C:\some\name')
# 字符串 打印时禁止转义
word = 'Python'
word[0]  # P
word[5]  # n
word[0:2]  # Py
wordLen = len(word)
print(wordLen)

# 列表
squares = [1, 4, 9, 16, 25]
squares[-1:]  # 列表切片
print(squares[-1:])
squares + [36, 49, 64, 81]  # 列表合并 不是在原列表上面操作
print(squares + [36, 49, 64, 81])
squares[1]
print(squares[1])  # 列表 根据下标去数据
squares.append(36)
print(squares)  # 列表 在原数组中添加数据
