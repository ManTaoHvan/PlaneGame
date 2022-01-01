
# 判断玩家是否中弹
def checkWin_hero(hero,enemy):
   for bullet in enemy.bulletList:
       #敌方子弹x方向上和我们飞机x方向上的比较 and 敌方子弹y方向上和我们飞机y方向上的比较
       if bullet.EnemyBullet_x >= hero.Hero_x and bullet.EnemyBullet_x <= hero.Hero_x+100 \
               and bullet.EnemyBullet_y>=hero.Hero_y and bullet.EnemyBullet_y<=hero.Hero_y+120:
           hero.isHit=True

#判断敌方是否中弹
def checkWin_eanmy(hero,enemy):
   for bullet in hero.bulletList_middle:
       #敌方子弹x方向上和我们飞机x方向上的比较 and 敌方子弹y方向上和我们飞机y方向上的比较
       if bullet.HeroBullet_middle_x >= enemy.Enemy_x and bullet.HeroBullet_middle_x <= enemy.Enemy_x+100  \
               and bullet.HeroBullet_middle_y >= enemy.Enemy_y and  bullet.HeroBullet_middle_y <= enemy.Enemy_y+120:
           enemy.isHit=True