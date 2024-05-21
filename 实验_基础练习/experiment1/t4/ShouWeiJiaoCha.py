'''
（1） 查找两个字符串首尾交叉的最大子串长度，连接两个字符串，首尾交叉部
分只保留一份。例如，1234 和2347 连接为12347
要求：程序中使用lambda 表达式以及函数
'''

def check(str1,str2):
    length = min(len(str1), len(str2))
    k = max(range(0, length + 1), key=lambda i: i if str1[len(str1) - i:] == str2[:i] else False)

    return (k, str1 + str2[k:])  # k为重复字符的个数（两个字符串首尾交叉的最大子串长度）

str1 = '12345'
str2 = '12345'
print(str1, str2)
print(check(str1, str2))