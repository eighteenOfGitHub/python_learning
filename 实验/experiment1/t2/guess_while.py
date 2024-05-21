"""
编写代码：利用while循环判断来制作一个猜数字的小游戏
问题描述：程序运行时，系统在指定范围内生成一个随机数字，然后用户进行猜测，
并根据用户输入进行必要的提示（right, too large, too small），
如果猜对则提前结束程序，如果次数用完仍没有猜对，提示游戏结束并给出正确答案。
"""

import random
objNum = random.randint(0,100)
print('欢迎进行猜数游戏！请输入你要猜的数：')
times = 7
while times > 0:
    a = eval(input())
    if a > objNum:
        print('too large!请重新输入！')
    elif a < objNum:
        print('too small!请重新输入！')
    else:
        print('right!The number is', objNum,'.')
        break
    times -= 1
if times == 0:
    print('真遗憾！您的机会用完了。')

