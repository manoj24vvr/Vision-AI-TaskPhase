import pygame
import random

# Calling all the functions of pygame
pygame.init()
width = 600   # initializing width and height of display screen
height = 400
snake_block = 10
dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game by Manoj")
pygame.display.update()

# Giving the RGB values for the colour.
red = (128,0,0)
black = (0,0,0)
white = (255,255,255)
grey = (150,50,150)
orange = (255,150,20)
fo = (0,200,255)

dis.fill(grey)  # To fill the screen or surface with required colour.
game_over = False
snake_speed = 20
x=300
y=200
x_change=0
y_change=0
clock = pygame.time.Clock()
game_close = False

# Assigning font style.
font_style = pygame.font.SysFont("freesans",25)
lost_img = font_style.render("You lost! Press P-Play Again or Q-Quit",True,red)
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orange,(x[0],x[1],snake_block,snake_block))
        
# Function to display score.
def thescore(score):
    value = font_style.render("Your Score: " + str(score), True, fo)
    dis.blit(value, [0,0])

# The main code of the game.
def game_loop():
    game_over =False
    game_close=False
    x = int(width/2)
    y = int(height/2)
    x_change = 0
    y_change = 0
    foodx = snake_block*random.randint(0,(width/snake_block-1))
    foody = snake_block*random.randint(0,(height/snake_block-1))
    snake_list=[]
    length_of_snake=1
    
    while (game_over == False):
        while(game_close==True):
            dis.fill(white)
            dis.blit(lost_img,[100,100])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close =False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key ==pygame.K_p:
                        game_loop()
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:   # to check if the keys on keyboard are being pressed.
                if event.key==pygame.K_UP:
                    x_change =0
                    y_change =-10

                elif event.key==pygame.K_DOWN:
                    x_change = 0
                    y_change = 10

                elif event.key==pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0

                elif event.key==pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
        if x>= width or x<0 or y>=height or y<0:
            game_close = True
        x += x_change
        y += y_change
        dis.fill(grey)
        
        #pygame.draw.rect(dis,orange,(x,y,10,10))
        #pygame.draw.rect(dis,fo,(foodx,foody,10,10))
        pygame.draw.rect(dis,fo,(foodx,foody,snake_block,snake_block))
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list)>length_of_snake:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        our_snake(10,snake_list)
        if x ==foodx and y ==foody:
            length_of_snake += 1
            foodx = snake_block*random.randint(0,(width/snake_block-1))
            foody = snake_block*random.randint(0,(height/snake_block-1))
        thescore(length_of_snake-1)
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    
game_loop()