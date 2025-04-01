from pygame import*
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, self.rect)



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 -  80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_wight - 50:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update2(self):
        if self.rect.y <= 20:
            self.direction = 'down'
        if self.rect.y >= 150:
            self.direction  = "up"
        
        if self.direction == "down":
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed


class Wall(sprite.Sprite):
    def __init__(self, color1,color2, color3, wall_x, wall_y, wall_width, wall_heidth):
        super().__init__()
        self.image = Surface((wall_width, wall_heidth))
        self.image.fill((color1, color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x , self.rect.y))


    



win_wight = 700
win_hight = 500
window = display.set_mode((win_wight,win_hight))
display.set_caption("maze")

background = transform.scale(image.load("Screen_Shot_2019-03-14_at_2.43.33_PM.jpg"),(win_wight,win_hight))


player = Player("images.jpg", 5 , 420 , 4)
monster1 = Enemy("photo_2025-02-25_18-39-50.jpg", 620, 280 , 2)
monster2 = Enemy("photo_2025-02-25_18-39-47.jpg", 420, 60, 2)
final = GameSprite("photo_2025-02-25_18-34-56.jpg", 580 , 420 , 0)

w1 = Wall(139, 0, 139, 100, 20, 530, 10)
w2 = Wall(139, 0, 139, 100, 480, 280, 10)
w3 = Wall(139, 0, 139, 100, 20, 10, 380)
w4 = Wall(139, 0, 139, 100, 20, 10, 380)
w5 = Wall(139, 0, 139, 190, 110, 10, 370)
w6 = Wall(139, 0, 139, 280, 30, 10, 370)
w7 = Wall(139, 0, 139, 370, 110, 10, 370)
w8 = Wall(139, 0, 139, 370, 110, 180, 10 )
w9 = Wall(139, 0, 139, 540, 120, 10, 390)
w10 = Wall(139, 0, 139, 630, 20, 10, 370)





game = True
clock = time.Clock()

mixer.music.load("AQYLA - Москва.mp3")
mixer.music.play()
mixer.music.set_volume(1)

money = mixer.Sound("money.ogg")
kick = mixer.Sound("kick.ogg")

font.init()
font = font.SysFont("Arial", 70)
win = font.render('YOU WIN', True,(0 ,255, 0))
lose = font.render("YOU LOSE", True, (255, 0, 0))





walls = [w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        if sprite.collide_rect(player, final):
            finish = True
            kick.play()
            window.blit(win, (200,200))
        if sprite.collide_rect(player, monster1) or sprite.collide_rect(player, monster2):
            finish = True
            kick.play()
            window.blit(lose, (200,200))
        for i in walls:
            if sprite.collide_rect(player, i):
                finish = True
                kick.play()
                window.blit(lose, (200,200))
        
            
            
            

        
        player.reset()
        monster1.reset()
        monster2.reset()
        final.reset()
        player.update()
        monster1.update()
        monster2.update2()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()

   
    
    display.update()
    clock.tick(60)
display.update()   








































