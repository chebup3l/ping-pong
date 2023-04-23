from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        sprite.Sprite.__init__(self)
 

        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
 

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

black = (255,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

clock = time.Clock()
FPS = 60
game = True 

ball = GameSprite('ball1.png', 200, 200, 45, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    ball.reset()

    display.update()
    clock.tick(FPS)
