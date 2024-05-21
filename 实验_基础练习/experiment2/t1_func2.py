'''
（1） 列表推导式与字典的应用
问题描述：编写程序，先生成包含1000个随机字符的字符串，然后统计每个字符出现的次数。
要求：查找资料编写至少2种不同的求解方法。
'''
#方法二：字典的get()应用
import random
import string
#生成包含1000个随机字符的字符串
x = string.ascii_letters+string.digits+string.punctuation;
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
#统计每个字符串出现的次数
d = dict()
for ch in z:
    d[ch] = d.get(ch,0)+1
#显示结果
i = 0
for key,value in d.items():
    if i == 10:
        print(f'{key}:{value}')
        i = 0
    else:
        print(f'{key}:{value}',end='\t')
        i += 1