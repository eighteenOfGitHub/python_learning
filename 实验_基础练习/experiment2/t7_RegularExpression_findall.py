'''
（7） 正则表达式的应用
问题描述：用户输入一段英文，然后输出这段英文中所有长度为 3 个字母
的单词。
（提示：可以调用 findall 函数，也可以先调用 split 函数将字符串进行分
隔，再搜索长度为 3 的单词。）
'''

import re
x = input('请输入句子：')
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(x))