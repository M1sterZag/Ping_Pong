import pygame as pg

pg.init()
# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Определение размеров окна
WIDTH = 900
HEIGHT = 700

# Создание игрового окна
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ping-Pong")
clock = pg.time.Clock()

# Шрифт
font = pg.font.Font("fonts/Comfortaa-VariableFont.ttf", 40)

# Загрузка музыки
hit_sound = pg.mixer.Sound('sounds/hit.mp3')
score_sound = pg.mixer.Sound('sounds/score.mp3')
win_sound = pg.mixer.Sound('sounds/win.mp3')
