import pygame
import sys
import random
pygame.init()          #initialise the pygame


width_screen = 820
height_screen = 620

"""screen"""

SCREEN_Display = pygame.display.set_mode((width_screen,height_screen ))   #creating the screen using pygame and pass the tuple as 'width' and 'height' of screen

""" player size, position and color"""
Green = (0,128,0)        #green colour RGB
PLAYER = [410,500]               #set the parameters of player(400 = left, 305 = right, 55)
size_of_player = 55    # set the size of the player height, 55 = widht) 

""" Enemie size, position and color"""
red = (255,0,0)
size_of_enemy = 55 
Enemy = [random.randint(0,width_screen),0]               #set the parameters of Enimie(100 = left, 0 = top)




def COLLI(PLAYER, Enemy):
    """Assigning the position of Enemy and player"""
    plyer_X_position = PLAYER[0]
    player_y_position = PLAYER[1]
    
    Enemy_x_position = Enemy[0]
    Enemy_y_position = Enemy[1]
    """This condition ckecks the 'X' overlap"""
    if (Enemy_x_position >= plyer_X_position and Enemy_x_position < (plyer_X_position + size_of_player)) or (plyer_X_position >= Enemy_x_position and plyer_X_position < (Enemy_x_position + size_of_enemy)):
        """This condition ckecks the 'Y' overlap"""    
        if (Enemy_y_position >= player_y_position and Enemy_y_position < (player_y_position + size_of_player)) or (player_y_position >= Enemy_y_position and player_y_position < (Enemy_y_position + size_of_enemy)):
            return True
    return False

GAME_OVER = False    
while not GAME_OVER:
    
    """ Watch for keyboard and mouse events"""
    for every_event in pygame.event.get():   #pygame 'event' track everything that we do on the screen
        if every_event.type == pygame.QUIT:   # To quit from the screen
            sys.exit() 
        if every_event.type == pygame.KEYDOWN:       #for making the movement of the player 
            playerPosition_X =  PLAYER[0]                #taking the current position of player 
            playerPosition_Y = PLAYER[1]
            
            if every_event.key == pygame.K_LEFT:
                playerPosition_X -= 55                   #Move the player to the left 
            elif every_event.key == pygame.K_RIGHT:
                playerPosition_X += 55                     #Move the player to the lef
                
            PLAYER = (playerPosition_X,playerPosition_Y)      #new position of player 
    
    SCREEN_Display.fill((0,0,0))
    
    pygame.time.wait(30)
        
    if Enemy[1] >= 0 and Enemy[1] < height_screen:
        Enemy[1] += 20
    else:
        Enemy[0] = random.randint(0,width_screen)
        Enemy[1] = 0

    if COLLI(PLAYER, Enemy):
        GAME_OVER = True
        
    pygame.draw.ellipse(SCREEN_Display, Green, (PLAYER[0],PLAYER[1],size_of_player,size_of_player))  
    pygame.draw.ellipse(SCREEN_Display, red, (Enemy[0],Enemy[1],size_of_enemy,size_of_enemy))
    pygame.display.update()
    
