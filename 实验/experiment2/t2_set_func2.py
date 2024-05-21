'''
(2) 集合的应用
问题描述：编写程序，输入两个集合setA与setB，分别输出它们两个交集的交、差、并。
要求：采用系统类与自定义集合类两种方法进行实现
'''
#自定义set类

import copy
class MySet:
    def __init__(self,alist):
        self.mylist = alist
    #并集
    def __or__(self,mySet):
        alist = copy.deepcopy(self.mylist)
        for item in mySet.mylist:
            if item not in self.mylist:
                alist.append(item)
        return MySet(alist)
    #交集
    def __and__(self,mySet):
        alist = list()
        for item in mySet.mylist:
            if item in self.mylist:
                alist.append(item)
        return MySet(alist)
    #差集
    def __sub__(self,mySet):
        alist = copy.deepcopy(self.mylist)
        for item in mySet.mylist:
            if item in alist:
                alist.remove(item)
        return MySet(alist)
    #输出
    def print(self):
        print('{',end='')
        for item in self.mylist:
            if self.mylist.index(item) != len(self.mylist)-1:
                print(item,end = ',')
            else:
                print(item,end='')
        print('}')


myset1 = MySet([1,2,3,4,5,6])
myset2 = MySet([4,5,6,7,8,9])
print('aset:',end='')
myset1.print()
print('bset:',end='')
myset2.print()
print('并集：',end='')
(myset1|myset2).print()
print('交集：',end='')
(myset1&myset2).print()
print('差集：',end='')
(myset1-myset2).print()
