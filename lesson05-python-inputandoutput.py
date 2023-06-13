# 输出
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')


yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))


# 读写文件
with open('input-text.txt', 'w', encoding="utf-8") as f:
    f.write("input========text1")
f.close()

with open('input-text.txt', encoding='utf-8') as f:  # 读取文件
    read_data = f.read()
    print(read_data)
f.close()
