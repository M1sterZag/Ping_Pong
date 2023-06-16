from resources import *
import random

# Инициализация pygame
pg.init()

# Инициализация платформ и мячика
platform_width = 10
platform_height = 60
platform_speed = 5

ball_radius = 10
ball_x_speed = random.choice([-3, 3])
ball_y_speed = random.choice([-3, 3])

# Расположение платформ и мячика
platform1_x = 35
platform1_y = (HEIGHT - platform_height) // 2

platform2_x = WIDTH - platform_width - 35
platform2_y = (HEIGHT - platform_height) // 2

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Счетчики
bounce_count = 0
score_red = 0
score_blue = 0


def draw_platforms():
    """Функция отрисовки платформ"""
    pg.draw.rect(screen, RED, (platform1_x, platform1_y, platform_width, platform_height))
    pg.draw.rect(screen, BLUE, (platform2_x, platform2_y, platform_width, platform_height))


def draw_ball():
    """Функция отрисовки мяча"""
    pg.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)


def update_score():
    """Функция отрисовки счета"""
    FONT = pg.font.Font("fonts/Comfortaa-VariableFont.ttf", 56)
    score_red_text = FONT.render(str(score_red), True, RED)
    score_blue_text = FONT.render(str(score_blue), True, BLUE)
    screen.blit(score_red_text, ((WIDTH - score_red_text.get_width()) // 4, 10))
    screen.blit(score_blue_text, ((WIDTH - score_blue_text.get_width()) // 4 * 3, 10))


def draw_dashed_line():
    """Функция отрисовки поля"""
    dash_width = 5
    dash_height = 10
    dash_spacing = 20
    dash_y = 0

    while dash_y < HEIGHT:
        pg.draw.rect(screen, WHITE, ((WIDTH - dash_width) // 2, dash_y, dash_width, dash_height))
        dash_y += dash_height + dash_spacing


def draw_win(color):
    global is_playing_win_music
    """Функция отрисовки победы"""
    text = font.render(f"{color.upper()} выиграл!", True, RED if color == 'red' else BLUE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    text = font.render("Нажмите R для рестарта игры", True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45))
    screen.blit(text, rect)
    if not is_playing_win_music:
        pg.mixer.music.load('sounds/win.mp3')
        pg.mixer.music.play()  # Воспроизведение музыки победы
        is_playing_win_music = True


# Переменная для отслеживания воспроизведения музыки
is_playing_win_music = False
# Основной игровой цикл
game_start = False
game_over = False
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Обработка нажатий клавиш w/s и up/down
    keys = pg.key.get_pressed()
    if keys[pg.K_w] and platform1_y > 0:
        platform1_y -= platform_speed
    if keys[pg.K_s] and platform1_y < HEIGHT - platform_height:
        platform1_y += platform_speed
    if keys[pg.K_UP] and platform2_y > 0:
        platform2_y -= platform_speed
    if keys[pg.K_DOWN] and platform2_y < HEIGHT - platform_height:
        platform2_y += platform_speed

    # Рестарт игры
    if keys[pg.K_r]:
        platform1_x = 35
        platform1_y = (HEIGHT - platform_height) // 2

        platform2_x = WIDTH - platform_width - 35
        platform2_y = (HEIGHT - platform_height) // 2

        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        bounce_count = 0

        score_red = score_blue = 0
        game_over = False
        game_start = True
        is_playing_win_music = False
        pg.mixer.music.load('sounds/fon_music.mp3')
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(-1)

    if game_start:
        # Обновление позиции мячика
        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # Проверка столкновений мячика с платформами
        if ball_x <= platform1_x + platform_width and platform1_y <= ball_y <= platform1_y + platform_height:
            ball_x_speed = abs(ball_x_speed)
            bounce_count += 1
            hit_sound.play()
        if ball_x >= platform2_x - ball_radius and platform2_y <= ball_y <= platform2_y + platform_height:
            ball_x_speed = -abs(ball_x_speed)
            bounce_count += 1
            hit_sound.play()

        # Проверка столкновений мячика с верхней и нижней стенками
        if ball_y <= 0 or ball_y >= HEIGHT - ball_radius:
            ball_y_speed = -ball_y_speed
            hit_sound.play()

        # Обновление счета и перезапуск мячика, если он выходит за пределы игрового поля
        if ball_x < 0:
            score_blue += 1
            score_sound.play()
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_x_speed = random.choice([-3, 3])
            ball_y_speed = random.choice([-3, 3])
            bounce_count = 0
        if ball_x > WIDTH:
            score_red += 1
            score_sound.play()
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_x_speed = random.choice([-3, 3])
            ball_y_speed = random.choice([-3, 3])
            bounce_count = 0

        # Ускорение мячика после определенного количества отскоков
        if bounce_count >= 4:
            if ball_x_speed > 0:
                ball_x_speed += 1
            else:
                ball_x_speed -= 1
            if ball_y_speed > 0:
                ball_y_speed += 1
            else:
                ball_y_speed -= 1
            bounce_count = 0

        # Очистка экрана
        screen.fill(BLACK)

        # Проверка на победу
        if score_red == 5 or score_blue == 5:
            game_over = True
            game_start = False

        # Отрисовка поля
        draw_dashed_line()

        # Отрисовка платформ, мячика и счета
        draw_platforms()
        draw_ball()
        update_score()

    elif game_over:
        screen.fill(BLACK)
        if score_red == 5:
            draw_win('red')
        elif score_blue == 5:
            draw_win('blue')
        pg.display.update()

    else:
        # Отрисовка надписи
        text1 = font.render("Нажмите R для начала игры", True, WHITE)
        text_rect = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text1, text_rect)
        text2 = font.render("w/s", True, RED)
        text_rect = text2.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 45))
        screen.blit(text2, text_rect)
        text3 = font.render("up/down", True, BLUE)
        text_rect = text3.get_rect(center=(WIDTH // 4 * 2.8, HEIGHT // 2 + 45))
        screen.blit(text3, text_rect)

    # Обновление экрана
    pg.display.update()

    # Ограничение FPS
    clock.tick(60)

# Завершение игры
pg.quit()
