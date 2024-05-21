'''
（6） 字典的应用
问题描述：编写程序，输入任意长度的字符串,统计每个单词出现的次数并存储到字典进行输出。
例如：
输入：
“I love China”，
输出：
I：1
love: 1
China: 1
'''

def count_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word,0)+1
    return word_count
sentence = input('请输入句子：')
print(count_words(sentence))