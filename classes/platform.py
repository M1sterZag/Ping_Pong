from config import *


class Platform:
    def __init__(self, x, width, height, speed, color):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = (HEIGHT - height) // 2
        self.speed = speed
        self.platform_rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.platform = pg.draw.rect(screen, self.color, self.platform_rect)

    def draw_platform(self):
        self.platform = pg.draw.rect(screen, self.color, self.platform_rect)

    def update_platform(self, vector):
        self.y = self.y + self.speed * vector
        if self.y <= 0:
            self.y = 0
        elif self.y + self.height >= HEIGHT:
            self.y = HEIGHT - self.height

        self.platform_rect = (self.x, self.y, self.width, self.height)

    @staticmethod
    def displayScore(score, color, coefficient):
        text = font_56.render(str(score), True, color)
        text_w = text.get_width()
        screen.blit(text, ((WIDTH - text_w) // 4 * coefficient, 10))

    def get_Rect(self):
        return self.platform_rect
