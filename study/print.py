import math
print('hello,world')
#会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('one','two','three')
print('100+200=',300)
name=input("please enter your name")
print('hello',name)
#列表list
classmates=['Michael','Bob','Tracy']
print(classmates)
# tuple
t=(1,2)
# dict 效率更高
d={'michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# 函数默认参数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#可变参数，可变参数就是传入的参数个数是可变的
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
