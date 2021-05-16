import pygame
import random
pygame.init()

class Color:
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    blue = (0,0,255)
    yellow = (255,255,0)

class Rocket:
    def __init__(self , x, y , color):
        self.w = 10
        self.h = 50
        self.x = x
        self.y = y
        self.color = color
        self.speed = 10
        self.score = 0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x  , self.y , self.w , self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x , self.y , self.w , self.h])

    def move(self , b):
        if self.y <b.y:
            self.y += self.speed

        elif self.y > b.y:
            self.y -= self.speed

        # # limitation
        if self.y < 0 :
            self.y = 0
        if self.y > Game.height- self.h :
            self.y = Game.height - self.h

class Ball:
    def __init__(self):
        self.r = 10
        self.x = Game.width/2
        self.y = Game.height/2
        self.speed = 10
        self.color = Color.yellow
        self.x_direction = int(random.choice([1,-1]))
        self.y_direction = int(random.choice([1,-1]))
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x ,self.y], self.r)


    def show(self):
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x,self.y], self.r)

    def move(self):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction

        if self.y > Game.height or self.y <0:
            self.y_direction *= -1
    def new(self):
        self.x = Game.width/2
        self.y = Game.height/2

class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width , height))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    fps = 30
    @staticmethod
    def play():
        pygame.mouse.set_visible(False)
        me = Rocket(15, Game.height/2 -25, Color.red)
        computer = Rocket(Game.width - 25, Game.height/2 - 25, Color.blue)
        ball = Ball()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    me.y = pygame.mouse.get_pos()[1]

                    if me.y > Game.height - me.h :
                        me.y = Game.height - me.h

            ball.move()
            computer.move(ball)

            # backend
            if ball.x <0 :
                computer.score += 1
                ball.new()
            elif ball.x > Game.width:
                me.score += 1
                ball.new()
            if me.area.collidepoint(ball.x,ball.y) or computer.area.collidepoint(ball.x , ball.y):
                ball.x_direction *= -1

            # frontend
            Game.screen.fill(Color.black)
            pygame.draw.rect(Game.screen, Color.white, [0 , 0 , Game.width , Game.height] , 10)
            pygame.draw.aaline(Game.screen, Color.white, [Game.width/2 , 0 ] ,[Game.width/2 , Game.height])

            me.show()
            computer.show()
            ball.show()
            font = pygame.font.SysFont('Arial', 100)
            text_me=font.render(str(me.score),True,(125,0,125))
            Game.screen.blit(text_me,(Game.width/4,Game.height/2 - 75))
            text_com=font.render(str(computer.score),True,(125,0,125))
            Game.screen.blit(text_com,(Game.width/4 *3 ,Game.height/2 -75))

            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__ == "__main__":
    Game.play()