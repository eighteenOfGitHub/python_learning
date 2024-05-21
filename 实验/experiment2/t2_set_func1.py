'''
(2) 集合的应用
问题描述：编写程序，输入两个集合setA与setB，分别输出它们两个交集的交、差、并。
要求：采用系统类与自定义集合类两种方法进行实现
'''
#系统类
aset = set([1,2,3,4,5,6])
bset = set([5,6,7,8,9,10])
#并集
print('并集:')
print(aset | bset)
print(aset.union(bset))
#交集
print('交集:')
print(aset & bset)
print(aset.intersection(bset))
#差集
print('差集:')
print(aset - bset)
print(aset.difference(bset))
#对称差
print('对称差')
print(aset ^ bset)
print(aset.symmetric_difference(bset))