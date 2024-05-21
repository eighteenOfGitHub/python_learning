'''
(5) 编写函数： 一年365 天， 每周工作5 天，休息2 天，休息日水平下降
0.01，工作日要努力到什么程度一年后的水平才与每天努力1%所取得的效果（即
37.78 倍）一样呢？
'''

def dayup(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1-0.01)
        else:
            dayup = dayup * (1+df)
    return dayup

dayfactor = 0.01
while (dayup(dayfactor)<37.78):
    dayfactor = dayfactor + 0.001
print("每天的努力参数是：{:.3f}.".format(dayfactor))
