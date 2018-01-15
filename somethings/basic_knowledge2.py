# if语句
if 5 < 2:
    print("山重水复疑无路")
print("柳暗花明又一村")
'''运行结果：柳暗花明又一村'''


if 5 < 2:
    print('我是if内部语句')
else:
     print('我是else内部语句')
'''运行结果：我是else内部语句'''


if 5 > 2:
    print('我是if内部语句')
else:
    print('我是else内部语句')
'''运行结果：我是if内部语句'''


a = '小花'
if a == '小花':
    print('我是if内部语句')
else:
    print('我是else内部语句')
'''运行结果：我是if内部语句'''


a = 0
if a:
    print('我是if内部语句')
else:
    print('我是else内部语句')

a = None
if a:
    print('我是if内部语句')
else:
    print('我是else内部语句')

a = ''
if a:
    print('我是if内部语句')
else:
    print('我是else内部语句')

a = ' '
if a:
    print('我是if内部语句')
else:
    print('我是else内部语句')
# elif语句
# 将字符串a转换成整型
a = int(input('输入变量a的值：'))
# 打印变量类型
print(type(a))
print(type(2))
if a == 2:
    print('今天是星期一，猴子穿新衣')
elif a == 3:
    print('今天是星期二，猴子有点二')
elif a == 4:
    print('今天是星期三，猴子爬雪山')
else:
    print('猴子干嘛去了？')


# 序列
# 1.列表[]:列表是有序的对象集合
list = [7, 2, 8, 2, 'x', 'y']
for i in list:
    print(i)
    print('zzzzzzzzzz')
    print(list[2])
    print(list[0])
    # 修改变量的值
    list[0] = 5
    print(list[0])
# 追加函数append（）,下标索引从0开始
list.append(9)
print(list[6])
for a in list:
    print(a)


# 2.元组（）
tuple = (7, 8, 2, 'x', 'y')
for i in tuple:
    print(i)
    print(tuple[0])
    # 元组元素不允许修改
    # tuple[0] = 1
    print(tuple[0])


# 3.字典{}：无序的对象集合，由key：values组成
dict = {'a': 111, 'b': 222, 'c': 333, 'd': 444}
for i in dict:
    print(i)  # 打印key值
    print(dict[i])  # 打印values值
    print(dict['b'])    # 只打印b的值
    print(dict)     # 打印所有的值
for k, v in dict.items():
    print(k, ':', end='')
    print(v)

print(dict.items())


# range()函数
for i in range(1, 10, 1):   # 1:初始值，10：终止数，1：步长
    print(i)
for i in range(10):   # 初始值不选默认为0，步长不选默认为1
    print(i)
# 100以内（包括100）的基数？
for i in range(1, 100, 2):
    print(i)
# 100以内（包括100）的偶数？
for i in range(0, 101, 2):
    print(i)

# continue用法     # 跳出当前循环，循环继续
for i in range(6):
    print(i)
    if i == 2:
        print(10*'2.5 ')
        continue
    print(10*'*')

# break语句:跳出这个循环
for i in range(6):
    print(i)
    if i == 2:
        print(10*'2.5 ')
        continue
    if i == 4:
        break
    print(10*'*')

# pass用法:使语法完整，空字符
for i in range(10):
    pass

# 格式符
print('i`m %s i`m %d years old' % ('xiaoming',18))
print('i`m %(name)s i`m %(age)d years old' % {'name':'xiaoming', 'age': 18})


# item方法
dict_1 = {'name': 'zhangsan', 'age': '22'}
dict_1.items()
print(dict_1)
# 增
dict = {'name': 'zhangsan', 'age': 22}
print(dict)
dict['Sex'] = 'male'
print(dict)
# 删除
dict_1 = {'name': 'zhangsan', 'age': 22}
# 删除方法1
del dict_1['name']
print(dict_1)
# 结果：{'age': 22}
# 删除方法2：
dict_1.pop('name')
print(dict_1)
# 结果：{'age': 22}
# 删除方法3
dict_1.popitem()  # 属于随机删除
print(dict_1)
# 结果：{'age': 22}
# formkeys方法,快速生成一个字典
dict3 = dict.fromkeys([1, 2, 3], 'keys')
print(dict3)

# setdefault方法
# 如果键在字典中，返回这个键所对应的值。如果键不在字典中，向字典 中插入这个键，并且以default为这个键的值，并返回 default。default的默认值为None
dict_1 = {'name': 'zhangsan', 'age': '20', 'sex': 'f', 'male': 111}
dict_1.setdefault("sex", "male")
print(dict_1)
