'''
（5） 元组的应用
问题描述：编写程序，利用生成器推导式生成包含n 个整数元素的元组，每
个元素值不大于m，并过滤掉偶数整数，并输出。
'''

import random
m,n = 50,10
atuple = tuple([random.randint(0, m) for i in range(n)])
print('过滤前:', atuple)
print('过滤后:', tuple(filter(lambda x: x % 2 != 0, atuple)))
print('过滤后:', tuple([item for item in atuple if item % 2 != 0]))