'''
（1） 列表推导式与字典的应用
问题描述：编写程序，先生成包含1000个随机字符的字符串，然后统计每个字符出现的次数。
要求：查找资料编写至少2种不同的求解方法。
'''
#方法三：collections模块defaultdict类应用
import string
import random
#生成包含1000个随机字符的字符串
x = string.ascii_letters+string.digits+string.punctuation;
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
#统计每个字符串出现的次数
from collections import defaultdict
frequences = defaultdict(int)
for item in z:
    frequences[item]+=1
#显示结果
print(frequences)
print(frequences.items())


"""
i = 0
for key,value in d.items():
    if i == 10:
        print(f'{key}:{value}')
        i = 0
    else:
        print(f'{key}:{value}',end='\t')
        i += 1
"""