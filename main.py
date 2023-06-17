from classes.platform import Platform
from classes.ball import Ball
from config import *
import random


def game():
    winner = False
    running = True
    game_start = False
    pg.mixer.music.set_volume(0.2)
    pg.mixer.music.play()

    red_platform = Platform(35, 10, 70, 5, RED)
    blue_platform = Platform(WIDTH - 10 - 35, 10, 70, 5, BLUE)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10, 4, WHITE)
    platform_list = [red_platform, blue_platform]

    red_score = blue_score = 0
    red_y_vector = blue_y_vector = 0

    while running:
        screen.fill(BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # Обработка нажатий клавиш w/s и up/down
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and red_platform.y > 0:
            red_platform.y -= red_platform.speed
        if keys[pg.K_s] and red_platform.y < HEIGHT - red_platform.height:
            red_platform.y += red_platform.speed
        if keys[pg.K_UP] and blue_platform.y > 0:
            blue_platform.y -= blue_platform.speed
        if keys[pg.K_DOWN] and blue_platform.y < HEIGHT - blue_platform.height:
            blue_platform.y += blue_platform.speed

        if keys[pg.K_r]:
            if winner:
                red_platform = Platform(35, 10, 70, 5, RED)
                blue_platform = Platform(WIDTH - 10 - 35, 10, 70, 5, BLUE)
                ball = Ball(WIDTH // 2, HEIGHT // 2, 10, 4, WHITE)
                platform_list = [red_platform, blue_platform]
                red_score = blue_score = 0
                red_y_vector = blue_y_vector = 0
            winner = False
            game_start = True

        if not game_start:
            text1 = font_46.render("Нажмите R для начала игры", True, WHITE)
            text_rect = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text1, text_rect)
            text2 = font_46.render("w/s", True, RED)
            text_rect = text2.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 45))
            screen.blit(text2, text_rect)
            text3 = font_46.render("up/down", True, BLUE)
            text_rect = text3.get_rect(center=(WIDTH // 4 * 2.8, HEIGHT // 2 + 45))
            screen.blit(text3, text_rect)
        else:
            if not winner:
                for platform in platform_list:
                    if pg.Rect.colliderect(ball.get_Rect(), platform.get_Rect()):
                        ball.hit()

                red_platform.update_platform(red_y_vector)
                blue_platform.update_platform(blue_y_vector)
                point = ball.update_ball()

                if point == -1:
                    red_score += 1
                    random.choice(playlist[1]).play()
                elif point == 1:
                    blue_score += 1
                    random.choice(playlist[1]).play()

                if point:
                    ball.reset()

                dash_width = 5
                dash_height = 10
                dash_spacing = 20
                dash_y = 0

                while dash_y < HEIGHT:
                    pg.draw.rect(screen, WHITE, ((WIDTH - dash_width) // 2, dash_y, dash_width, dash_height))
                    dash_y += dash_height + dash_spacing

                red_platform.draw_platform()
                blue_platform.draw_platform()
                ball.draw_ball()

                red_platform.displayScore(red_score, RED, 1)
                blue_platform.displayScore(blue_score, BLUE, 3)

                if blue_score == 5 or red_score == 5:
                    if blue_score == 5:
                        winner_color = BLUE
                        winner_text = 'Blue win!'
                    else:
                        winner_color = RED
                        winner_text = 'Red win!'
                    winner = True
                    win_sound.play()

            else:
                text = font_46.render(winner_text, True, winner_color)
                rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(text, rect)
                text = font_46.render("Нажмите R для рестарта игры", True, WHITE)
                rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45))
                screen.blit(text, rect)

        pg.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    game()
    pg.quit()
