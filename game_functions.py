import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():

        print(event.type)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                print('right down')
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                print('left down')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
                print('right up')
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                print('left up')


def update_screen(ai_settings, screen, ship):
    # 更新屏幕上的图像，并切换到屏幕
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
