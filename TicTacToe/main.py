from cmath import rect
from turtle import pen
import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TicTacToe")

LINE_WIDTH = 6
markers = []
clicked = False
pos = []
player = 1
game_over = False
winner = 0


green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

def draw_grid():
    bg = (255,255,200)
    grid = (50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x*100),(screen_width,x*100),LINE_WIDTH)
        pygame.draw.line(screen,grid,(x*100,0),(x*100,screen_width),LINE_WIDTH)


for i in range(3):
    row = [0] * 3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,green, (x_pos*100 + 15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),LINE_WIDTH)
                pygame.draw.line(screen,green, (x_pos*100 + 15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),LINE_WIDTH)
            elif y == -1:
                pygame.draw.circle(screen,red,(x_pos*100+50,y_pos*100+50),38,LINE_WIDTH)
            
            y_pos += 1
        
        x_pos += 1

def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        elif sum(x) == -3:
            winner = 2
            game_over = True
        
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        elif markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True

        y_pos += 1

    #check cross
    if markers[0][0] + markers[1][1] + markers[2][2] ==  3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    elif  markers[0][0] + markers[1][1] + markers[2][2] ==  3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

font = pygame.font.SysFont(None,40)
play_again_rect = Rect(screen_width // 2-80,screen_height//2,160,50)
def draw_winner(winner):
    win_text = f"Player {winner} wins!"
    win_img = font.render(win_text,True,blue)
    pygame.draw.rect(screen,green,(screen_width // 2-100,screen_height // 2-60,200,50))
    screen.blit(win_img,(screen_width // 2 - 100,screen_height // 2 -50))

    again_text = "Play Again !"
    again_img = font.render(again_text,True,blue)
    pygame.draw.rect(screen,green,play_again_rect)
    screen.blit(again_img,(screen_width//2-80,screen_height//2+10))




run = True
while run:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

        if game_over == False:

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            elif event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False

                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]

                if markers[cell_x // 100 ][cell_y // 100] == 0:
                    markers[cell_x // 100 ][cell_y // 100] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if play_again_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0]*3
                    markers.append(row)
                



    pygame.display.update()

pygame.quit()