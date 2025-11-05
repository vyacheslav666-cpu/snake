import pygame
import sys
import random
# библиотеки ок да

# ЗМЕЯ
class Snake:
    
    # конструктор
    def __init__(self, x, y, dx=1, dy=1, size=20, speed=10, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.dx = dx
        self.dy = dy
    
    # отрисовка
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    # движение
    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed


    # условие столкновения (в дальнейшем передавать экземпляр food в параметры)
    def check_collision(self, food_x, food_y):

        if abs(self.x - food_x)  <= self.size and abs(self.y - food_y) <= self.size:
            return True
        else:
            return False


def position_food(snake):
    border = 2
    food_x = snake.size * random.randint(border, width // snake.size - border)
    food_y = snake.size * random.randint(border, height // snake.size - border)

    return food_x, food_y




pygame.init()
# запустили движок, мб

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")
# загрузили экран

# ЗМЕЯ

# создаем обьект
snake = Snake(width // 2, height // 2)

# ЕДА

food_x, food_y = position_food(snake) 
# положение

food_color = (255, 0, 0)
# цвет

food_size = snake.size


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
            snake.dx, snake.dy = 0, -1
        elif event.key == pygame.K_DOWN:
            snake.dx, snake.dy = 0, 1
        elif event.key == pygame.K_LEFT:
            snake.dx, snake.dy = -1, 0
        elif event.key == pygame.K_RIGHT:
            snake.dx, snake.dy = 1, 0


    if snake.check_collision(food_x, food_y) == True:
        food_x, food_y = position_food(snake) 
    # условие столкновения

    snake.move()

    snake.draw(screen)
    # отрисовываем змейку

    pygame.draw.rect(screen, food_color, (food_x, food_y, food_size, food_size))
    # рисуем еду

    pygame.display.flip()
    # обновляем экран

    clock.tick(10)
    # десять ФПС
