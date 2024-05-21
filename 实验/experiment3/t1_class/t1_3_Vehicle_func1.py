'''
（3）编程设计一个基类汽车类Vehicle，
包含最大速度MaxSpeed，weight两个实例私有属性； ok
    设计一个派生子类自行车（Bicycle）类，      ok
增加1个实例私有属性高度（height）和1个成员函数SetMaxSpeed实现给父类的实例属性MaxSpeed的赋值。 ok
要求：
1) 根据以上描述设计类，并在主函数中创建子类的实例化对象，并设置对象的MaxSpeed值。
2) 利用property将height设定为可读、可修改、可删除的属性。
'''

class Vehicle:
    def __init__(self, MaxSpeed, weight):
        self.__MaxSpeed = MaxSpeed
        self.__weight = weight
    def __getWeight(self):
        return self.__weight
    def __getMaxSpeed(self):
        return self.__MaxSpeed

class Bicycle(Vehicle):
    def __init__(self, MaxSpeed, weight, height):
        super().__init__(MaxSpeed, weight)
        self.__height = height
    def __getHeight(self):
        print("getter...")
        return self.__height
    def __setHeight(self, h):
        print("setter...")
        self.__height = h
    def __delHeight(self):
        print("deleter...")
        del self.__height
    height = property(__getHeight, __setHeight,__delHeight)
    def show(self):
        print('MaxSpeed：', self.MaxSpeed)
        print('height：', self.__height)
    def SetMaxSpeed(self, MaxSpeed):
        self.MaxSpeed = MaxSpeed

b = Bicycle(3, 5, 3)
b.height=5
b.SetMaxSpeed(100)
b.show()
b.height=1
print(b.height)
del b.height
