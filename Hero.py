import pygame
from pygame.locals import *
from  HeroBullet import *
import time

class Hero:


    def __init__(self,screen,Hero_x,Hero_y):
        self.screen=screen
        self.Hero_x=Hero_x
        self.Hero_y=Hero_y
        self.Hero_image=pygame.image.load("./feiji/hero1.png")
        self.bulletList_middle=[]  #英雄机的子弹列表，注意 主方法里面 有刷新方法(即属性界面)，所以 这个列表其实刻其实时刻显示一颗子弹，如果即使列表里面有很多子弹
        self.bulletList_left=[]  #英雄机的子弹列表，注意 主方法里面 有刷新方法(即属性界面)，所以 这个列表其实刻其实时刻显示一颗子弹，如果即使列表里面有很多子弹
        self.bulletList_right=[]  #英雄机的子弹列表，注意 主方法里面 有刷新方法(即属性界面)，所以 这个列表其实刻其实时刻显示一颗子弹，如果即使列表里面有很多子弹
        self.isHit=False
        #爆炸图片
        self.hero_blowupList=[]
        self.hero_blowupList.append(pygame.image.load("feiji/hero_blowup_n1.png"))
        self.hero_blowupList.append(pygame.image.load("feiji/hero_blowup_n2.png"))
        self.hero_blowupList.append(pygame.image.load("feiji/hero_blowup_n3.png"))
        self.hero_blowupList.append(pygame.image.load("feiji/hero_blowup_n4.png"))
        self.blowIndex=0;
        #游戏结束
        self.finish=[]
        self.finish.append(pygame.image.load("feiji/finish.jpg"))

    #飞机和子弹的显示
    def display(self):
        # 显示爆炸效果
        if self.isHit:
            # 玩家机器击中
            self.screen.blit(self.hero_blowupList[self.blowIndex], (self.Hero_x, self.Hero_y))
            self.blowIndex += 1
            time.sleep(0.3) #延迟以下吧爆炸效果
            if self.blowIndex ==3:
                screen_wide = 900
                screen_high = 550
                self.screen.blit(self.finish[0], (screen_wide/4 - 50, screen_high/4 -10))
                pygame.display.update() #注意 这里要刷新下，不然 图片不会显示
                time.sleep(1)
                exit()
        else:
            self.screen.blit(self.Hero_image,(self.Hero_x,self.Hero_y))
            #中间的子弹
            for bullet in self.bulletList_middle: #显示飞机的所有子弹,注意 这里面会遍历所有子弹，但由于刷新界面，所以，所以以前的旧值不显示，只显示最后的一个子弹。当然清空一下
                self.screen.blit(bullet.HeroBullet_image_middle, (bullet.HeroBullet_middle_x, bullet.HeroBullet_middle_y))
                bullet.move_middle()
                if bullet.HeroBullet_middle_y <= 0: #即让这个子弹 打完到地方的边框里面 就可以把它可以移除了，以免内存撑爆
                    self.bulletList_middle.remove(bullet)
            #左边的子弹
            for bullet in self.bulletList_left:  # 显示飞机的所有子弹,注意 这里面会遍历所有子弹，但由于刷新界面，所以，所以以前的旧值不显示，只显示最后的一个子弹。当然清空一下
                self.screen.blit(bullet.HeroBullet_image, (bullet.HeroBullet_left_x, bullet.HeroBullet_left_y))
                bullet.move_left()
                if bullet.HeroBullet_left_y <= 0:  # 即让这个子弹 打完到地方的边框里面 就可以把它可以移除了，以免内存撑爆
                    self.bulletList_left.remove(bullet)
            #右边子弹
            for bullet in self.bulletList_right:  # 显示飞机的所有子弹,注意 这里面会遍历所有子弹，但由于刷新界面，所以，所以以前的旧值不显示，只显示最后的一个子弹。当然清空一下
                self.screen.blit(bullet.HeroBullet_image, (bullet.HeroBullet_right_x, bullet.HeroBullet_right_y))
                bullet.move_right()
                if bullet.HeroBullet_right_y <= 0:  # 即让这个子弹 打完到地方的边框里面 就可以把它可以移除了，以免内存撑爆
                    self.bulletList_right.remove(bullet)

    #控制飞机的操作键盘
    def keyController(self):
        #移动速度
        rate=20
        for even in pygame.event.get():
            if even.type==QUIT:
                exit()
            elif even.type==KEYDOWN:
                if even.key == K_LEFT:
                    self.Hero_x -= rate
                elif even.key == K_RIGHT:
                    self.Hero_x += rate
                elif even.key == K_UP:
                    self.Hero_y -= rate
                elif even.key == K_DOWN:
                    self.Hero_y += rate
                elif even.key==K_SPACE: #按一个空格键 发射一个子弹
                    bullet=HeroBullet(self.screen,self.Hero_x,self.Hero_y)
                    self.bulletList_middle.append(bullet)
                    self.bulletList_left.append(bullet)
                    self.bulletList_right.append(bullet)
