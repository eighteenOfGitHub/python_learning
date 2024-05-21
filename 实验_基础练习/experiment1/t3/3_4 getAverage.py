'''
编写函数：随机产生包含n 个整数的列表，返回一个元组，其中第一个
元素为所有参数的平均值，其他元素为所有参数中大于平均值的整数。
'''

import random
def getAverage():
    alist = [random.randint(0, 100) for i in range(10)]
    '''for item in range(10):
        alist.append(random.randint(0, 100))'''
    average = 0
    for item in alist:
        average += item
    average /= 10
    aver_list = [item for item in alist if item>average]
    aver_list.insert(0,average)
    return tuple(aver_list)
print(getAverage())
print(getAverage())
print(getAverage())


