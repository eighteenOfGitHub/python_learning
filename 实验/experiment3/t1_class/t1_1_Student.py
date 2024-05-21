'''
（1） 编程设计学生信息类，
实例属性包括：学号、姓名、性别，年龄、n门课程成绩，
要求：
1) 利用文件读取，创建一个包含n个学生的班级;
2) n门课程成绩利用字典存储，支持成绩录入、修改;
3) 求解每个学生的三门成绩的平均值，及其平均值排名。
并按照成绩平均成绩排名正序输出功能：学号、姓名、性别、年龄，三门课程成绩，三门课程平均值，排名。
'''

class Student:
    def __init__(self,info):
        self.ID = info[0]
        self.name = info[1]
        self.sex = info[2]
        self.age = int(info[3])
        self.grade = dict()
        self.grade['Chinese'] = int(info[4])
        self.grade['Math'] = int(info[5])
        self.grade['English'] = int(info[6])
        self.allOfGrade = 0
        for item in self.grade.items():
            self.allOfGrade += item[1]
        self.average = int(self.allOfGrade/len(self.grade))
    def update(self):
        self.allOfGrade = 0
        for item in self.grade.items():
            self.allOfGrade += item[1]
        self.average = int(self.allOfGrade/len(self.grade))
class MyClass:
    def __init__(self):
        self.studentInfo = []
        self.count_student = 0
        f1 = open('StudentInfo.txt', 'r', encoding='UTF-8')
        while True:
            line = f1.readline()
            if line == '':
                break
            info = line.replace("\n",' ').split()
            student = Student(info)
            self.studentInfo.append(student)
            self.count_student += 1
        f1.close()
    def modGrade(self,name,subject,score):
        for stu in self.studentInfo:
            if name == stu.name:
                stu.grade[subject] = score
                stu.update()
                f1 = open('StudentInfo.txt', 'w', encoding='UTF-8')
                for stu in self.studentInfo:
                    f1.write(stu.ID+' '+stu.name+' '+stu.sex+' '+str(stu.age)+' '+str(stu.grade['Chinese'])+' '+str(stu.grade['Math'])+' '+str(stu.grade['English'])+'\n')
                f1.close()
                return True
        return False
    def printInfo(self):
        self.studentInfo.sort(key= lambda x:x.average,reverse=True)
        rank = 1
        preStuAverage = 0
        for stu in self.studentInfo:
            if stu.average == preStuAverage:
                rank -= 1
            print(f'学号:{stu.ID} 姓名:{stu.name} 性别:{stu.sex} 年龄:{stu.age} Chinese:{stu.grade["Chinese"]} Math:{stu.grade["Math"]} English:{stu.grade["English"]} 三门课程平均值:{stu.average} 排名:{rank}')
            preStuAverage = stu.average
            rank += 1

myclass = MyClass()
myclass.printInfo()
if not myclass.modGrade('玉麻子','Chinese',99):
    print('输入名字有误或本班级中没有该学生！请重新输入！')
if not myclass.modGrade('王麻子','Chinese',99):
    print('输入名字有误或本班级中没有该学生！请重新输入！')
myclass.printInfo()

'''
001 张三 男 18 88 78 87
002 王麻子 男 18 67 76 78
003 李四 男 19 90 98 97
'''

'''
思考：对于用户信息管理，
用户信息量大时，用列表管理，利于后续的信息的整体管理如输出，更新等
'''


