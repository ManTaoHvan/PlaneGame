import pygame
from pygame.locals import *  #导入本地操作类库 比如键盘事件
from Hero import *
from Enemy import *
from checkWin import *

#游戏界面的主函数
def main():

    #窗口情况
    screen_wide=900
    screen_high=550
    screen = pygame.display.set_mode((screen_wide, screen_high), 0, 0) # 创建游戏窗口
    background = pygame.image.load("./feiji/background.png") # 加载一张背景图片

    #飞机对象(我方飞机和敌方飞机)
    hero=Hero(screen,screen_wide/2 - 100,screen_high-105) #x=,y=3初始飞机的位置
    enemy=Enemy(screen,screen_wide/2,0,screen_wide,screen_high) #飞机的初始位置

    while True:
       #窗口
       screen.blit(background,(0,0))    # 把背景图片填充到界面中

       #我方飞机行为
       pygame.key.set_repeat(10)
       hero.display()
       hero.keyController()

       #敌方飞机行为
       enemy.display()
       enemy.move()
       enemy.fire()

        #判断玩家胜负
       checkWin_hero(hero,enemy)
       checkWin_eanmy(hero,enemy)


       # 刷新界面
       pygame.display.update()

main()

