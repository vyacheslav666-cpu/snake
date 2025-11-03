import pygame
import sys
import random
# библиотеки ок да

def position_food():
    border = 2
    food_x = snake_size * random.randint(border, width // snake_size - border)
    food_y = snake_size * random.randint(border, height // snake_size - border)

    return food_x, food_y




pygame.init()
# запустили движок, мб

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")
# загрузили экран

# ЗМЕЯ

snake_color = (0, 255, 0)
snake_size = 20
snake_x, snake_y = (width // 2, height // 2)
# задали цвет, размер и положение змейки

snake_speed = 10
# скорость змейки

dx, dy = 1, 0
# движение по Х, У (вправо)


# ЕДА

food_x, food_y = position_food() 
# положение

food_color = (255, 0, 0)
# цвет

food_size = snake_size


clock = pygame.time.Clock()
# таймер

while True:
# основной ццикл игры
    for event in pygame.event.get():
    # обработчик событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # выход из игры
   
    screen.fill((30, 30, 30))
    # заполняем экран, хз
        
        # управление
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            dx, dy = 0, -1
        elif event.key == pygame.K_DOWN:
            dx, dy = 0, 1
        elif event.key == pygame.K_LEFT:
            dx, dy = -1, 0
        elif event.key == pygame.K_RIGHT:
            dx, dy = 1, 0

    snake_x += dx * snake_speed
    snake_y += dy * snake_speed
    # двигаем змейку

    if abs(snake_x - food_x)  <= snake_size and abs(snake_y - food_y) <= snake_size:
        food_x, food_y = position_food() 
    
    # условие столкновения

    pygame.draw.rect(screen, snake_color, (snake_x, snake_y, snake_size, snake_size))
    # отрисовываем змейку

    pygame.draw.rect(screen, food_color, (food_x, food_y, food_size, food_size))
    # рисуем еду

    pygame.display.flip()
    # обновляем экран

    clock.tick(10)
    # десять ФПС
