import pygame
from EnemyBullet import *
import random
import time

class Enemy:

    def __init__(self,screen,Enemy_x,Enemy_y,screen_wide,screen_high):
        self.screen=screen
        self.Enemy_x = Enemy_x
        self.Enemy_y = Enemy_y
        self.screen_wide =screen_wide
        self.screen_high= screen_high
        self.Enemy_image = pygame.image.load("./feiji/enemy0.png")
        self.direction="right"
        self.bulletList=[]
        self.isHit=False

        #爆炸图片
        self.enemy_blowupList=[]
        self.enemy_blowupList.append(pygame.image.load("feiji/enemy0_down1.png"))
        self.enemy_blowupList.append(pygame.image.load("feiji/enemy0_down2.png"))
        self.enemy_blowupList.append(pygame.image.load("feiji/enemy0_down3.png"))
        self.enemy_blowupList.append(pygame.image.load("feiji/enemy0_down4.png"))
        self.blowIndex=0;

        #游戏结束
        self.finish=[]
        self.finish.append(pygame.image.load("feiji/finish.jpg"))

    #飞机和子弹的显示
    def display(self):
        # 显示爆炸效果
        if self.isHit:
            # 敌方机器击中
            self.screen.blit(self.enemy_blowupList[self.blowIndex], (self.Enemy_x, self.Enemy_y))
            self.blowIndex += 1
            time.sleep(0.3) #延迟以下吧爆炸效果
            if self.blowIndex == 3:
                screen_wide = 900
                screen_high = 550
                self.screen.blit(self.finish[0], (screen_wide/4 - 50, screen_high/4 -10))
                pygame.display.update()  # 注意 这里要刷新下，不然 图片不会显示
                time.sleep(1)
                exit()
        else:
            self.screen.blit(self.Enemy_image,(self.Enemy_x,self.Enemy_y))
            for bullet in self.bulletList:  # 显示飞机的所有子弹
                self.screen.blit(bullet.EnemyBullet_image, (bullet.EnemyBullet_x, bullet.EnemyBullet_y))
                bullet.move()
                if bullet.EnemyBullet_y >= self.screen_high:  # 即让这个子弹 打完到地方的边框里面 就可以把它可以移除了,以免内存撑爆
                    self.bulletList.remove(bullet)

    #飞机左右移动
    def move(self):
        self.wide=self.screen_wide - 45
        if self.direction=="right":
            self.Enemy_x +=1
            if self.Enemy_x >= self.wide:
                self.direction ="left"
        else:
            self.Enemy_x -= 1
            if self.Enemy_x <= 0:
                self.direction ="right"

    #子弹发射频率
    def fire(self):
       num= random.randint(1,200) #产生随机整数
       if num==10 or num==20:
         bullet=EnemyBullet(self.screen,self.Enemy_x,self.Enemy_y);
         self.bulletList.append(bullet)
