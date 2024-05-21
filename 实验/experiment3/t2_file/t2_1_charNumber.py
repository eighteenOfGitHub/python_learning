'''
（1） 问题描述：编写程序，生成多个字符串，将字符串写入文件，同时读取当前文件，并输出统计字符串的个数。
'''

import random
import string

x = string.ascii_letters+string.digits+string.punctuation;
with open('t2_1test.txt', 'w') as w:
    for i in range(random.randint(1, 10)):
        y = [random.choice(x) for j in range(10)]
        s = ''.join(y)
        s+=' '
        w.write(s)
with open('t2_1test.txt', 'r') as r:
    lst = r.readlines()
    x = lst[0]
    y = x.split()
    print(y)
    print(len(y))

'''
测试文件：t2_1test.txt
yClj56
'''
