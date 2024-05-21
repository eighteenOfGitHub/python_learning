'''
pygame  pip安装 下载速度问题
        环境变量问题
sys     用于监控设备

思想：面向对象
class：
蛇
属性： 1.初始化的长度
        2.头 方向
方法： 1.吃
        2.死亡
        3.移动
        4.改变方向
食物
'''
import random
import sys
import pygame

#全局变量
SCREEN_X = 600
SCREEN_Y = 600

class Snake(object):
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []  #[(25,0),(50,0),(75,0)]
        for x in range(5):
            self.addnode()
    #吃
    def addnode(self):
        left, top = (0,0)
        if self.body:
            left, top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left,top,25,25) #表示像素方格以25为一个单位
        if self.dirction == pygame.K_LEFT:
             node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)

    #删除尾部
    def delnode(self):
        self.body.pop()

    #死亡判断：
    def isdead(self):
        #撞墙
        if self.body[0].x not in range(SCREEN_X):
            return True
        if self.body[0].y not in range(SCREEN_Y):
            return True
        #撞自己
        if self.body[0] in self.body[1:]:
            return True
        return False

    #移动
    def move(self):
        self.addnode()
        self.delnode()

    #改变方向
    def changedirection(self,curkey):
         self.dirction = curkey

class Food:
    def __init__(self):
        self.rect = pygame.Rect(-25,0,25,25)
    def remove(self):
        self.rect.x = -25
    def set(self,snake):
        if self.rect.x == -25:
            allpos = []
            #不靠墙太近 25 ~ SCREEN_X - 25 之间,不在蛇身上
            for pos in range(25,SCREEN_X - 25, 25):
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top = random.choice(allpos)
            while (self.rect.left,self.rect.top) in snake.body:
                self.rect.left = random.choice(allpos)
                self.rect.top = random.choice(allpos)
            print(self.rect)

def show_text(screen,pos,text,color,font_bold=False,font_size = 60,font_italic = False):
    #获取系统字体，并设置字体大小
    cur_font = pygame.font.SysFont("宋体",font_size)
    #设置是否加粗属性
    cur_font.set_bold(font_bold)
    #设置是否斜体属性
    cur_font.set_italic(font_italic)
    #设置文字内容
    text_fmt = cur_font.render(text,1,color)
    #绘制文字
    screen.blit(text_fmt,pos)

def main():
    #游戏初始化
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)   # 设置大小
    pygame.display.set_caption("贪吃蛇")             # 设置标题
    clock = pygame.time.Clock()                     # 设置帧数

    # 加载音乐
    pygame.mixer.music.load("music.mp3")
    # 播放音乐
    pygame.mixer.music.play(-1)

    scores = 0                  # 分数
    isdead = False              # 判断是否死亡

    snake = Snake()
    food = Food()

    while True:
        i = 0
        for event in pygame.event.get():
            i+=1
            print(event)
            print(i)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                LR = [pygame.K_LEFT, pygame.K_RIGHT]
                UD = [pygame.K_UP, pygame.K_DOWN]
                if event.key in LR + UD:
                    if (event.key in UD) and (snake.dirction in LR):
                        snake.changedirection(event.key)
                        break
                    if (event.key in LR) and (snake.dirction in UD):
                        snake.changedirection(event.key)
                        break
                if event.key == pygame.K_SPACE and isdead:
                     return main()

        screen.fill((255,255,255))  #背景填充

        # 画蛇身
        if not isdead:
            snake.move()
        for rect in snake.body:
            if snake.body[0] == rect:
                pygame.draw.rect(screen, (20, 200, 39), rect, 0)
            else:
                pygame.draw.rect(screen, (20, 220, 39), rect, 0)

        # 显示死亡文字
        isdead = snake.isdead()
        if isdead:
            show_text(screen, (100, 200), 'YOU DEAD!', (227, 29, 18), False, 100)
            show_text(screen, (150, 260), 'press space to try again...', (0, 0, 22), False, 30)
            pygame.mixer.music.pause() #暂停播放

        # 食物处理 吃到+50 食物与蛇头 蛇长度+1 方块
        if food.rect == snake.body[0]:
            scores += 50
            food.remove()
            snake.addnode()
        food.set(snake)
        pygame.draw.rect(screen, (136, 0, 24), food.rect, 0)

        # 显示分数文字
        show_text(screen, (50, 500), 'Scores:' + str(scores), (223, 223, 223))

        pygame.display.update() #更新图层
        clock.tick(10) #控制时间

main()


'''
问题与改进：
Q：假设蛇方向向右，当快速按下方向下和方向左时，（想要执行的行为为在蛇头的上一行或下一行掉头），会出现直接判定为死亡
A：
基础内容介绍：
fps介绍：FPS是Frames Per Second的缩写，即每秒显示的帧数。较高的FPS意味着每秒绘制的图像数量更多，游戏画面更加流畅。
https://deepinout.com/pygame/pygame-questions/162_pygame_setting_a_fixed_fps_in_pygame_python_3.html

event介绍：Pygame 定义了一个专门用来处理事件的结构，即事件队列，该结构遵循遵循队列“先到先处理”的基本原则，通过事件队列，我们可以有
序的、逐一的处理用户的操作（触发事件）。下述表格列出了 Pygame 中常用的游戏事件：
https://www.jb51.net/article/279941.htm

查看pygame帮助文档：事件队列可以容纳的事件数量有上限。当队列满时，新事件将被悄悄丢弃。为了防止丢失事件，特别是发出退出命令信号的输
入事件，程序必须每帧处理事件(使用pygame.event.get()、pygame.event.pump()、pygame.event.wait()、pygame.event.peek()或
pygame.event.clear())并处理它们。

问题所在的猜测：
由于用户操作过快，在一个游戏帧中，eventlist中保存了两个事件，而代码中使用for循环将两个事件都执行了，而snake.move()执行所有
事件之后，所以才会出现蛇原地掉头死亡，调试时观察for循环中的事件数量即可，在控制台打印输出

调试过程中发现当按住方向键，蛇的方向会改变，在按住的同时，在按下另一个与之垂直的方向，方向也会改变，也就是说，event事件中用于判断的
变量是keydown，而不是keydown and keyup。找到变量，对其进行监测。

验证:根据控制台输出发现，正常的事件都是keydown后是keyup，且i都为1；而错误触发蛇的死亡是keydown，keydown，keyup，keyup，且i为
1,2,1,2,由此可以推断猜测正确，然后根据猜测优化程序

问题改正方案：
1.提高游戏帧数，从而减少两次keydown在同一帧出现的概率
2.让循环中只出现一次keydown，就是用每监测到一次keydown，就break循环

方案评估：
方案一：
提高游戏帧数就会使蛇前进（move()函数执行）速度变快，游戏难度提升，不可取。
方案二：
每次处理事件后，改变方向一次后，break循环，直接进行游戏界面刷新。

调整方案执行后调试与评估：监测到的数据结果为keydown，keyup，keyup，且i为1,1,2，也就是第二次的keydown消失了。现在要考虑何时消失。
猜测break循环后，第二次的keydown依然在消息队列中，刷新游戏屏幕后，系统会将事件队列清空，所以导致到第二帧时，keydown消失，使游戏的
流畅性降低。经过查找，并没有找到底层原理与解决方案。相较与之前，通过牺牲游戏手感换取游戏bug。


拓展：
1.双人小游戏
2.自动移动
'''

