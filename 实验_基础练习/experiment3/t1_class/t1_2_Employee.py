'''
编程设计一个雇员基类Employee，
包括姓名，编号，月薪三个实例属性，月薪计算pay()和信息显示show()两个函数成员；
派生两个子类manager类和salesman类，重载相应的2个函数成员。
要求：根据以上描述设计类，并在主函数创建两个子类的实例化对象，分别调用其成员方法。
'''

class Employee:
    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary
    def pay(self):
        pass
    def show(self):
        pass
class Manager(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID, salary)
    def pay(self):
        print('Manager\tsalary：' + self.salary)
    def show(self):
        print('Manager\t姓名：' + self.name + ' ' + 'ID:' + self.ID + ' ' + '月薪：' + self.salary)

class Salesman(Employee):
    def __init__(self, name, ID, salary):
        super().__init__(name, ID, salary)
    def pay(self):
        print('Salesman\tsalary：' + self.salary)
    def show(self):
        print('Salesman\t姓名：' + self.name + ' ' + 'ID:' + self.ID + ' ' + '月薪：' + self.salary)


m = Manager('张三', '1', '100')
s = Salesman('李四', '2', '100')
for item in (m, s):
    item.pay()
    item.show()





