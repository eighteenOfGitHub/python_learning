'''
（1）设计函数用来计算斐波那契数列中小于参数n的所有值。
'''

def f():
    a,b = 1,1
    while True:
        yield a
        a, b = b, a+b

n = eval(input('请输入斐波那契数列上限：'))
Fibonacci = f()
a = Fibonacci.__next__()
while a < n:
    print(a,end=' ')
    a = Fibonacci.__next__()