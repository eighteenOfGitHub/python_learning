'''
（4） 编程设计一个队列类Myqueue，主要的类成员包括：
3个数据成员（队列的最大长度size，队列所有数据data，队列的元素个数current）和6个成员方法如下：
1) 初始化 ：设置队列为空;
2) 判断队列为空：若为空，则返回TRUE，否则返回FALSE.
3) 判断队列为满：若为满，则返回TRUE，否则返回FALSE.
4) 取队头元素：取出队头元素;
条件：队列不空。
否则，应能明确给出标识，以便程序的处理.
5) 入队：将元素入队，即放到队列的尾部
6) 出队：删除当前队头的元素
要求：根据以上描述设计类，并在主函数中创建类的实例化对象，构建一个长度为N的队列，分别调用上述成员方法。
'''
import random

class MyQueue:
    def __init__(self, size):
        self.size = size
        self.current = 0
        self.data = []
    def isEmpty(self):
        return self.data == []
    def isFull(self):
        return self.current == self.size

    def get_top(self):
        if not self.isEmpty():
            return self.data[0]
        else:
            print('队列为空')

    def push(self,n):
        if self.isFull():
            print('队列已满')
        else:
            self.data.append(n)
            self.current += 1

    def pop(self):
        if self.isEmpty():
            print('队列已空，无法出队')
        else:
            return self.data.pop()
            self.current -= 1

q=MyQueue(10)
print(q.isEmpty())
for i in range(6):
    q.push(random.randint(1,10))
print(q.pop())
print(q.data)
print(q.get_top())
print(q.isFull())
