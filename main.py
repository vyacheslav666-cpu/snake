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


# ЕДА

class Food:

    # консруктор
    def __init__(self, x=0, y=0, size=20, color=(255, 0, 0), border=2):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.border = border

    # случайная позиция
    def position_food(self, snake):
    
        self.x = snake.size * random.randint(self.border, width // snake.size - self.border)
        self.y = snake.size * random.randint(self.border, height // snake.size - self.border)


    # отрисовка
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))




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

food = Food()
food.position_food(snake)

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


    if snake.check_collision(food.x, food.y) == True:
        food.position_food(snake)
    # условие столкновения

    snake.move()

    snake.draw(screen)
    # отрисовываем змейку

    food.draw(screen)
    # рисуем еду

    pygame.display.flip()
    # обновляем экран

    clock.tick(10)
    # десять ФПС
