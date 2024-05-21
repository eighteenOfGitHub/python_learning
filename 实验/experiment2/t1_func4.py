'''
（1） 列表推导式与字典的应用
问题描述：编写程序，先生成包含1000个随机字符的字符串，然后统计每个字符出现的次数。
要求：查找资料编写至少2种不同的求解方法。
'''
#方法四：collections模块Counter类应用
import string
import random
#生成包含1000个随机字符的字符串
x = string.ascii_letters+string.digits+string.punctuation;
y = [random.choice(x) for i in range(1000)]
z = ''.join(y)
#统计每个字符串出现的次数
from collections import Counter
frequences = Counter(z)
#显示结果
print(frequences.items())
print(frequences.most_common(1))
print(frequences.most_common(3))

'''
1.	python高级容器collections-defaultdict。地址：
https://blog.csdn.net/qq_43745578/article/details/125650363
2.	from collections import Counter计数器
https://blog.csdn.net/weixin_43956958/article/details/118415018
'''
