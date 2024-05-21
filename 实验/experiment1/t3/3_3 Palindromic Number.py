'''
（3）编写函数：判断回文，也就是正读反读都一样的字符串
'''
#方法一 切片法
def isPalindromic_1(str):
    lista = list(str)
    listb = lista[::-1]
    for i in range(lista.__len__()):
        if lista[i] != listb[i]:
            return False
    return True

#方法二 双指针
def isPalindromic_2(str):
    alist = list(str)
    left = 0
    right = alist.__len__()-1;
    while left<right:
        if alist[left] != alist[right]:
            return False
        left += 1
        right -= 1
    return True

#方法三：递归法
def isPalindromic_3(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return isPalindromic_3(str[1:-1]) #[1:-1]表示去除字符串的第一个字符和最后一个字符

str = input('请输入所需要检测的字符串：')
print(isPalindromic_1(str))
print(isPalindromic_2(str))
print(isPalindromic_3(str))

'''
[:-1]：就是去除了这行文本的最后一个字符（换行符）后剩下的部分。
line = “abcde”
line[:-1]
结果为：‘abcd’

[::-1]：反转
line = “abcde”
line[::-1]
结果为：‘edcba’

a = [0,1,2,3,4,5,6,7,8,9]
b = a[i:j] 表示复制a[i]到a[j-1]，以生成新的list对象
b = a[1:3] 那么，b的内容是 [1,2]

当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
当i,j都缺省时，a[:]就相当于完整复制一份a了

b = a[i:j:s]这种格式呢，i,j与上面的一样，s表示步进，缺省为1.
所以a[i:j:1]相当于a[i:j]
当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
'''


