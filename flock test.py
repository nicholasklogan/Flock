import pygame
import random
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
done = False
clock = pygame.time.Clock()
safe_distance = 10
max_safe_distance = 20
speed = .02
Flock = []

class Bird():

    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.z = random.randint(-100, 100)
        self.xd = 0
        self.yd = 0
        self.zd = 0
        self.xz = 0
        self.yz = 0
        self.zz = 0
        
    def run(self):
        if not self.spread_out():
            self.move_together()
        if self.xd < 0:
            self.xz = -speed
        else:
            self.xz = speed
        if self.yd < 0:
            self.yz = -speed
        else:
            self.yz = speed
        if self.zd < 0:
            self.zz = -speed
        else:
            self.zz = speed
        try:
            self.xz = self.xz / (self.xd != 0 + self.yd != 0 + self.zd != 0)
            self.yz = self.yz / (self.xd != 0 + self.yd != 0 + self.zd != 0)
            self.zz = self.zz / (self.xd != 0 + self.yd != 0 + self.zd != 0)
        except:
            pass
        
        self.x += self.xz
        self.y += self.yz
        self.z += self.zz
        if self.x <= 1:
            self.x = 1
        self.x = self.x % WINDOW_WIDTH
        self.y = self.y % WINDOW_HEIGHT
        self.xd = 0
        self.yd = 0
        self.zd = 0

    def spread_out(self):
        Hit = False
        for bird in Flock:
            if bird != self:
                x_dist = bird.x - self.x
                y_dist = bird.y - self.y
                z_dist = bird.z - self.z
                if safe_distance > abs(x_dist) and safe_distance > abs(y_dist) and safe_distance > abs(z_dist):
                    if x_dist > safe_distance:
                        self.xd += speed
                    elif x_dist < -safe_distance:
                        self.xd += -speed
                    if y_dist > safe_distance:
                        self.yd += speed
                    elif y_dist < -safe_distance:
                        self.yd += -speed
                    if z_dist > safe_distance:
                        self.zd += -speed
                    elif z_dist < -safe_distance:
                        self.zd += speed
                    Hit = True
        return Hit
                

    def move_together(self):
        for bird in Flock:
            if bird != self:
                x_dist = bird.x - self.x
                y_dist = bird.y - self.y
                z_dist = bird.z - self.z
                if max_safe_distance < abs(x_dist) and max_safe_distance < abs(y_dist) and max_safe_distance < abs(z_dist):
                    if x_dist > max_safe_distance:
                        self.xd += speed
                    elif x_dist < -max_safe_distance:
                        self.xd += -speed
                    if y_dist > max_safe_distance:
                        self.yd += speed
                    elif y_dist < -max_safe_distance:
                        self.yd += -speed
                    if z_dist > max_safe_distance:
                        self.zd += -speed
                    elif z_dist < -max_safe_distance:
                        self.zd += speed

NUMBER_OF_BIRDS = 20
for i in range(0, NUMBER_OF_BIRDS):
    Flock.append(Bird())

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        for bird in Flock:
            bird.run()
        screen.fill((0, 0, 0))
        for x, bird in enumerate(Flock):
            pygame.draw.rect(screen, (256/NUMBER_OF_BIRDS * x, 128, 255), pygame.Rect(bird.x , bird.y, 6, 6))
        pygame.display.flip()
