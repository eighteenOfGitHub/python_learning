'''
ListComprehension:列表推导式
（3） 字符串与列表推导式的应用
问题描述： 编写程序，生成含有 n 个元素的嵌套列表，
即列表的每个元素仍是列表，
要求列表中的元素是长度不超过m 的数字或字符组成的字符串，
并按照字符串长度降序输出结果。
'''

import random
import string

def getLen(alist):
    length = 0
    for item in alist:
        length += len(item)
    return length

ch = string.digits + string.ascii_letters
n, m = 3, 10
a = [[''.join(random.sample(ch,random.randint(1, m)))for j in range(n)] for i in range(n)]
print('生成嵌套列表：', a)
i = 0
for row in a:
    row.sort(key=lambda x: len(x))
    print(f'第{i}个字符串列表中各字符串长度总和为：', getLen(row))   # 测试使用方便观察
    i += 1
a.sort(key=lambda x: getLen(x))
print('排序后的列表：', a)

'''
random.sample(x,random.randint(1, m)是从列表x中选N个随机且不重复的元素
random.choice(x)是从中选取一个
'''

