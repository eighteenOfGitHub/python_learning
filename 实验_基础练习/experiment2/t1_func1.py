'''
（1） 列表推导式与字典的应用
问题描述：编写程序，先生成包含1000个随机字符的字符串，然后统计每个字符出现的次数。
要求：查找资料编写至少2种不同的求解方法。
'''
#方法一：c语言逻辑法
import random
import string
#生成包含1000个随机字符的字符串
str = ''
str_len = 1000
x = string.ascii_letters+string.digits+string.punctuation
len = len(x);
for n in range(str_len):
    i = random.randint(0,len-1);
    str += x[i]
#统计每个字符串出现的次数
char_dict = dict()
for n in range(str_len):
    c = str[n]
    if char_dict.get(c) == None:
        char_dict[c] = 1;
    else:
        char_dict[c] += 1
#显示结果
i = 0
for key,value in char_dict.items():
    if i == 10:
        print('{0}:{1}\t'.format(key,value))
        i = 0
    else:
        print(f'{key}:{value}',end='\t')
        i += 1

