'''
（2）编写程序以检查用户输入的密码的有效性。
检查密码的标准为：
1） [a-z]之间至少有 1 个字母
2） [0-9]之间至少有 1 个数字
3） [A-Z]之间至少有1个字母
4） [$＃@]中至少有 1 个字符
5） 最短交易密码长度：6
6） 交易密码的最大长度：12
问题描述：
程序接受一系列逗号分隔的密码，进行检查。
再输出符合条件的密码，每个密码用逗号分隔。
例如：程序的输入： abcdEF12＃@,ccword12 程序的输出： abcdEF12＃@
'''

import re

s = ',34tgwe5h4#,abcdEF12#@,ccword12,ds45dfgfgd#@yr1,12rgr33Av#'
pd = s.split(',')
result = []
for item in pd:
    if 12 >= len(item) >= 6:
        if re.findall('[a-z]',item):
            if re.findall('[0-9]',item):
                if re.findall('[A-z]',item):
                    if re.findall('[$#@]',item):
                        result.append(item)
print(result)