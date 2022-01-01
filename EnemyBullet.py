import pygame
class EnemyBullet:

    def __init__(self,screen,Enemy_x,Enemy_y):
        self.screen=screen
        self.EnemyBullet_x= Enemy_x + 22
        self.EnemyBullet_y= Enemy_y - 5
        self.EnemyBullet_image = pygame.image.load("./feiji/bullet1.png")

    #子弹发射的移动速度
    def move(self):
        self.EnemyBullet_y += 3