'''
（2）利用列表实现筛选法求素数
问题描述：编写程序，输入一个大于2的自然数，然后输出小于该数字的所有素数组成的列表。
'''

def getPrimeNumber(n):
    alist = [True]*(n+1)

    limit = int(pow(n,1/2))+1       #最大
    alist[0] = alist[1] = False
    for i in range(2,limit):
        if alist[i]:
            for j in range(i*i,n+1,i):
                alist[j] = False
    return [x for x in range(n+1) if alist[x]]

n = int(input('请输入一个大于2的自然数：'))
result = getPrimeNumber(n)
print(result)

'''
1.求根号的方法
    方法一     9**(0.5)
    方法二     import math
               math.sqrt(9)
    方法三     pow(9,0.5)       
2.筛选法求素数：每找到一个素数，将它的倍数从列表中剔除
'''