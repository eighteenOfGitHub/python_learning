'''
编写代码：利用if判断来制作一个猜数字的小游戏
问题描述：程序运行时，系统在指定范围内生成一个随机数字，然后用户进行猜测，
并根据用户输入进行必要的提示（right, too large, too small），
如果猜对则提前结束程序，如果未有猜对，提示游戏结束并给出正确答案。
'''
import random
objNum = random.randint(0,10)
print('欢迎进行猜数游戏！')
a = eval(input('请输入一个数（0~9）：'))
if a > objNum:
    print('too large!')
elif a < objNum:
    print('too small!')
else:
    print(f'right!The number is {objNum}.')
