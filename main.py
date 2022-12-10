import pygame
import time
import random

pygame.init()

#Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Переменные для разрешения экрана
dis_width = 600
dis_height = 400


snake_block = 10
snake_speed = 15

#Создание экрана
dis = pygame.display.set_mode((dis_width, dis_height))

#обновление экрана
pygame.display.update()

#Название
pygame.display.set_caption('PROGWARTS WORK')

clock = pygame.time.Clock()

#Вывод текста на экран
font_style = pygame.font.SysFont("Arial", 30)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [50, dis_height/2 - 50])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    # начальные координаты
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10

    #основной цикл игры
    game_close = False
    game_over = False
    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("YOULOSE!! press q - quit or c - play again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = +10

        #Проверка на столкновения
        if x1 > dis_width or x1 < 0 or y1 > dis_height or y1 < 0:
            #game_over = True
            game_close = True

        #заливка фона
        dis.fill(blue)

        #координаты змейки
        x1 += x1_change
        y1 += y1_change
        #
        #pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10
            Length_of_snake += 1

        clock.tick(snake_speed)

    #закрытие
    pygame.quit()
    quit()

gameLoop()