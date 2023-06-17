from config import *
import random


class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.start_speed = speed
        self.speed = speed
        self.bounce = 0
        self.x_vector = random.choice([-1, 1])
        self.y_vector = random.choice([-1, 1])
        self.ball = pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        self.score = 1

    def draw_ball(self):
        self.ball = pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update_ball(self):
        self.x += self.speed * self.x_vector
        self.y += self.speed * self.y_vector

        if self.y <= 0 or self.y >= HEIGHT - self.radius:
            self.y_vector *= -1
            hit_sound.play()

        if self.x <= 0 and self.score:
            self.score = 0
            return 1
        elif self.x >= WIDTH and self.score:
            self.score = 0
            return -1
        else:
            return 0

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_vector = random.choice([-1, 1])
        self.y_vector = random.choice([-1, 1])
        self.bounce = 0
        self.speed = self.start_speed
        self.score = 1

    def hit(self):
        self.x_vector *= -1
        hit_sound.play()

    def get_Rect(self):
        return self.ball
