from pizza import pizza233, fun
pizza233('meat', 'pork', 'fish')
fun()
# import pizza
# pizza.pizza233('meat', 'pork', 'fish')

# U1-字符串操作
'''
a = "test 1 by mcfate"
# b = 'test 1 by mcfate'
print(a.title())  # 大小写转换
print(a.upper())
print(a.lower())
print('Mes: [\t' + a + "\t]")  # 字符串拼接
b = '   233  '
print(b + "/")
print(b.lstrip() + "/")  # 去除行首空格
print(b.rstrip() + "/")  # 去除行末空格
print(b.strip() + "/")  # 去除首尾空格
'''

# U2-数字操作
'''
c = (1 + 2 - 3) + 4 * 0 + 5 / 2 + 2 ** 2  # **乘方
print("num is " + str(c))  # 数字转换为字符串
'''

# U3-列表操作
'''
array = ['ele0', 'ele1', 'ele2']
print(array)
print(array[0])
print(array[-1])  # 列表最后一个元素
array.append('ele3')  # 入栈
print(array)
array.insert(0, 'ex')  # 插入元素
print(array)
del array[0]  # 删除元素
print(array)
ele = array.pop(-1)  # 出栈
# ele = array.pop()
print(array)
print(ele)
array.remove('ele1')  # 删除指定的第一个元素
print(array)

# 列表排序
cars = ['bmw', 'audi', 'byd', 'benz']
print(sorted(cars))  #  按字母顺序排序(临时)
print(sorted(cars, reverse=True))  #  按字母顺序排序(临时)
print(cars)
cars.sort()  # 按字母顺序排序(永久)
print(cars)
cars.sort(reverse=True)  # 倒序排序
print(cars)
num = [2, 3, 5, 1]
num.reverse()  # 翻转列表
print(num)
num.reverse()
print(num)
print(len(num))  # 列表长度
'''

# U4-操作列表
'''
name = ['wj', 'zhy', 'mcfate', 'hanhan', 'hanyi']
for i in name:
    print(i)

for i in range(1, 5):
    print(i)

num = list(range(1, 6, 2))  # 生成数字列表
print(num)

squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

list1 = [3, 7, 2, 4, 5, 1]
print('max:' + str(max(list1)) + '\tmin:' + str(min(list1)) + '\tsum:' + str(sum(list1)))

s2 = [i**2 for i in range(1, 11)]  # 列表解析
print(s2)

print(name)
print(name[2:4])  # 切片
print(name[:4])
print(name[2:])
print(name[-2:])

ex1 = [1, 2, 3]
ex2 = ex1  # 指向相同列表
ex3 = ex1[:]  # 生成一个副表
ex1.append(10)
ex2.append(99)
ex3.append(0)
print(ex1)
print(ex2)
print(ex3)

dimensions = (200, 50)  # 元组，其内容不可修改，可访问
'''

# U5-if语句
'''
d = 'wj'
print(d == 'wj')
print(d == 'wj2')
e = 'hh'
if d == 'wj' and e == 'hh':  # and &&  or ||
    print('yes!')
else:
    print("no!")

users = ['su', 'wangjie', 'guest']
ban_users = ['null']
name = 'wangjie'
if name in users:
    print("login right!")
if name not in ban_users:
    print("post ok!")

age = 12
if age < 4:
    print("child")
elif age < 18:
    print("teen")
else:
    print("adult")

user_list = ['su', 'admin', 'wj', 'zhy', 'guest']
if user_list:
    for i in user_list:
        if i == 'admin':
            print("hello admin,this is right~")
        else:
            print("hello " + i + "!")
else:
    print("empty!")

def list_lower(s):
    return [i.lower() for i in s]


current_users = ["sss", "su", "Wj", "233", "John"]
new_users = ["sss", "john", "666", "WJ", "zhy"]
for i in new_users:
    if i.lower() in list_lower(current_users):
        print("name: " + i + " is used!!!")
    else:
        print("name: " + i + " can be use~~")
'''

# U6-字典
'''
alien = {'color': 'green', 'points': 5}
print(alien['color'])
alien['x'] = 0
alien['y'] = 25
alien['speed'] = 'medium'
print(alien)
print("time 0: x = " + str(alien['x']))
if alien['speed'] == 'slow':
    a = 1
elif alien['speed'] == 'medium':
    a = 2
else:
    a = 3

alien['x'] = alien['x'] + a
print("time 1: x = " + str(alien['x']))

del alien['points']

language = {
    'wj': 'python',
    'zhy': 'R',
    'mc': 'C++',
    '233': 'python'
    }

for key, value in language.items():
    print(key + " loves: " + value)

print(language.keys())

print(sorted(language.values()))  # 字典排序
print(set(language.values()))  # 集合，去除重复值

print(language.items())
print(language)

# 列表内存储字典
user_list = []
for i in range(1, 5):
    new_user = {'name': i, 'money': 2**i}
    user_list.append(new_user)
print(user_list)

# 字典内存储列表
pizza = {
    's': 'pork',
    'm': ['pork', 'fish'],
    'l': ['pork', 'fish', 'meat'],
    }

# 字典内存储字典
users = {
    'wj': {
        'name': 'wangjie',
        'num': '1114',
        'call': '5391',
        },
    'zhy': {
        'name': 'hanyi',
        'num': '1111',
        'call': '9045',
        },
    }
'''

# U7-用户输入
'''
message = input("please input!\n")
mes = int(message)  # 输入默认为字符串，转换为数字

i = 1
while i <= 5:
    print(str(i))
    i += 1

# flag = True
# while flag:
#     mes = input(">>  ")
#     if mes == "quit":
#         flag = False
#     else:
#         print("\n" + mes)

# while True:
#     mes = input(">>  ")
#     if mes == "quit":
#         break
#     else:
#         print("\n" + mes)

num = 0
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue

    print(num)

# 查找删除
pets = ['cat', 'dog', 'cat', 'fish', 'dog', 'pig', 'cat']
while 'cat' in pets:
    pets.remove('cat')

print(pets)
'''

# U8-函数
'''

def hello(name='admin', age='16'):  # 默认值形参
    # 文档字符串
    print(name + "'s age is " + str(age))
    return "right"


hello("wj", 20)  # 位置实参
hello(age=18, name="hh")  # 关键字实参
a = hello()
print(a)


def get_name(f, l, m=''):
    if m:
        name = f + ' ' + m + ' ' + l
    else:
        name = f + ' ' + l
    print(name.title())


get_name('wang', 'jie')
get_name('wang', 'jie', 'cool')


def delete(list):  # 对于列表，函数将直接改变（指针调用的，不存在副本）
    del list[-1]


l = ['233', 'aaa', 'ggg']
delete(l[:])  # 手动创造副本
print(l)
delete(l)
print(l)


# def pizza(*item):  # *数量不定实参,放入元组中
#     # 打印用户所有的配料
#     print(item)






def profile(f, l, **info):
    pro = dict()
    pro['f'] = f
    pro['l'] = l
    for k, v in info.items():
        pro[k] = v
    return pro


mes = profile('wang', 'jie', money='18K',place='hangzhou')
print(mes)

'''
