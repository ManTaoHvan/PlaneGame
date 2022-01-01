import pygame
class HeroBullet:
    def __init__(self,screen,Hero_x,Hero_y):
        self.screen=screen

        #中间子弹位置
        self.HeroBullet_middle_x=Hero_x + 41
        self.HeroBullet_middle_y=Hero_y + 10
        #左边子弹位置
        self.HeroBullet_left_x=Hero_x + 8
        self.HeroBullet_left_y=Hero_y + 17
        #右边子弹位置
        self.HeroBullet_right_x=Hero_x + 70
        self.HeroBullet_right_y=Hero_y + 17
        #子弹图片
        self.HeroBullet_image = pygame.image.load("./feiji/bullet.png")
        self.HeroBullet_image_middle = pygame.image.load("./feiji/bullet0.png")

    #中间子弹向前移动的速度
    def move_middle(self):
        self.HeroBullet_middle_y -= 5
    #左边子弹向前移动的速度
    def move_left(self):
        self.HeroBullet_left_y -= 3
    #右边边子弹向前移动的速度
    def move_right(self):
        self.HeroBullet_right_y -= 3