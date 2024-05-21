'''
（4） 列表与切片的应用
问题描述：编写程序，生成一个整型列表，
输出包含原列表中所有元素的新列表、
包含原列表中所有元素的逆序列表，
以及输出具有偶数位置的元素列
表。
'''

import random

alist = [random.randint(0, 100) for i in range(10)]
print('alist:', alist)
print('原列表：', alist[::])
print('逆序列表：', alist[::-1])
print('偶数序列列表：', alist[::2])
