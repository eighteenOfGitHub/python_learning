'''
（7） 正则表达式的应用
问题描述：用户输入一段英文，然后输出这段英文中所有长度为 3 个字母
的单词。
（提示：可以调用 findall 函数，也可以先调用 split 函数将字符串进行分
隔，再搜索长度为 3 的单词。）
'''

#split方法
def count_words(sentence):
    words = sentence.split()
    word_countisthree = []
    for word in words:
        if len(word) == 3:
            word_countisthree.append(word)
    return word_countisthree
sentence = input('请输入句子：')
result = count_words(sentence)
print(result)