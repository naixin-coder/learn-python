# 列表
furits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(furits)
furits.append("grape")  # 在原列表中添加元素
print(furits)
furits.insert(1, "grape")  # 在原列表中指定下标添加元素
print(furits)
furits.remove('grape')  # 在原列表中删除第一个指定元素
print(furits)
furits.pop()  # 在原列表中删除最后一个元素
print(furits)

del furits[0]  # 指定下标删除列表元素

furits.reverse()  # 在原列表中翻转列表
print(furits)

furits.sort()
print(furits)


print(furits.index("apple"))

print(furits.count('apple'))  # 返回列表中存在apple的次数


furits.clear()  # 清除列表
print(furits)


# 元组
t = 123, 321, "hello"
print(t[0])
print(t)
print(len(t))


# 集合  数据唯一性->去重
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('apple' in basket)
basket2 = {'apple', 'orange', 'grade', 'watermelon'}

print(basket | basket2)  # 并集
print(basket & basket2)  # 交集
print(basket - basket2)  # 差集
print(basket2 - basket)  # 差集
print(basket ^ basket2)  # 两个差集的并集

# 字典
tel = {'jack': '4396', 'mark': '4093'}
print(tel['jack'])
tel['tomas'] = '1920'
print(tel)
print('tomas' in tel)

for k, v in tel.items():
    print(k, v)
