'''
（1） 列表推导式与字典的应用
问题描述：编写程序，先生成包含1000个随机字符的字符串，然后统计每个字符出现的次数。
要求：查找资料编写至少2种不同的求解方法。
'''

#方法五：字典推导式
import random
import string
#生成包含1000个随机字符的字符串
x = string.ascii_letters+string.digits+string.punctuation;
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
#统计每个字符串出现的次数
lista = [] #key
listb = [] #value
for i in range(len(z)):
    if z[i] in lista:
        listb[lista.index(z[i])] += 1
    else:
        lista.append(z[i])
        listb.append(1);
char_dict = {i:j for i,j in zip(lista,listb)}
#显示结果
i = 0
for key,value in char_dict.items():
    if i == 10:
        print('{0}:{1}\t'.format(key, value))
        i = 0
    else:
        print(f'{key}:{value}',end='\t')
        i += 1
