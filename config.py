import pygame as pg

pg.init()

# Шрифт
font_56 = pg.font.Font("fonts/Comfortaa.ttf", 56)
font_46 = pg.font.Font("fonts/Comfortaa.ttf", 46)

# Определение цветов
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Определение размеров окна
WIDTH = 900
HEIGHT = 700

# Создание игрового окна
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ping-Pong")
clock = pg.time.Clock()
FPS = 60

# Загрузка музыки
hit_sound = pg.mixer.Sound('sounds/hit.mp3')
score_sound = pg.mixer.Sound('sounds/score.mp3')
win_sound = pg.mixer.Sound('sounds/win.mp3')
pg.mixer.music.load('sounds/fon_music.mp3')
