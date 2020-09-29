import pygame
import random

import sys
"""initialise the pygame"""
pygame.init()          


width_screen = 820    
height_screen = 620

z = [width_screen,height_screen]
SCREEN_Display = pygame.display.set_mode(z)   #creating the screen using pygame and pass the tuple as 'width' and 'height' of screen



""" player size, position and color"""
Green = (0,128,0)        #green colour RGB
PLAYER = [400,500]       #set the parameters of player(400 = left, 305 = top) 'x' position and 'y' position
size_of_player = 55     # set the size of the player height, 55 = widht) 

""" Enemie size, position and color"""
size_of_enemy = 55 
red = (255,0,0)
Enemy = [random.randint(0,width_screen - size_of_enemy),0]               #set the parameters of Enimie(100 = left, 0 = top)

GAME_SCORE = 0  #initially game score is 0

SCREEN_COLOR = (255, 255, 255)      

Enemy_speed = 10

myFont = pygame.font.SysFont("monospace", 25)
"""set the speed of emnemy block after some score
As the score increases the speed of enemy to fall down is also increases."""
def SPEED_LEVEL(GAME_SCORE, Enemy_speed):
	if GAME_SCORE < 10:
		Enemy_speed = 2
	elif GAME_SCORE < 25:
		Enemy_speed = 10
	elif GAME_SCORE < 40:
		Enemy_speed = 15
	else:
		Enemy_speed = 25
	return Enemy_speed

"""if player wins give the score"""
def winner(GAME_SCORE,GAME_OVER):
        
    if GAME_SCORE >= 100: 
        print("you win!! your gameplay is amazing")
        print("your score: -", GAME_SCORE)         
    else:
        print("game is running:- '100' score is required to win the game ")

        
        
LIST_Enemy = [Enemy]    # Single enemy inside the list
"""UPDATES_ THE ENEMY_"""
def EnemyUpdat(LIST_Enemy, GAME_SCORE):
    for index, Enemy in enumerate(LIST_Enemy):                # 'enumerate' = to get the enemie position and index
        """enimies on the screen"""
        if Enemy[1] >= 0 and Enemy[1] < height_screen:
            Enemy[1] += Enemy_speed
        else:                       #"""enemies off the screen"""
            LIST_Enemy.pop(index)
            GAME_SCORE += 1         # each time the enmie blocks fall and go to the bottom we need to increase the score by 1.
    return GAME_SCORE




"""DRAW enemy Function"""
def EnemyDraw(LIST_Enemy):
    for Enemy in LIST_Enemy:
        """draw ellipse for the enemy 
        iterate through multiple enemies"""
        pygame.draw.ellipse(SCREEN_Display, red, (Enemy[0],Enemy[1],size_of_enemy,size_of_enemy))   # Representation of Enemy Block

"""TO DROP MULTIPLE ENIMIES FROM THE TOP"""

def enemy_fall(LIST_Enemy):            # This function look at the LIST_enemy
    DELAY = random.random()            # random.random() = generate random float value between 0 and 1
    if len(LIST_Enemy) < 10 and DELAY < 0.1:                              # Keep adding enemies until we have 10 total in our list(LIST_Enemy)
        Enemy_x_position = random.randint(0,width_screen) #generating the random number
        Enemy_y_position = 0                                              #top of the screen
        LIST_Enemy.append([Enemy_x_position,Enemy_y_position])

"""this function DETECT the collision of 'player' and 'enemy'"""    
def COLLI(PLAYER, Enemy):
    """Assigning the position of Enemy and player"""
    plyer_X_positin = PLAYER[0]
    player_y_positin = PLAYER[1]
    
    Enemy_x_positin = Enemy[0]
    Enemy_y_positin = Enemy[1]
    """This condition ckecks the 'X' overlap"""
    if (Enemy_x_positin >= plyer_X_positin and Enemy_x_positin < (plyer_X_positin + size_of_player)) or (plyer_X_positin >= Enemy_x_positin and plyer_X_positin < (Enemy_x_positin + size_of_enemy)):
        """This condition ckecks the 'Y' overlap"""    
        if (Enemy_y_positin >= player_y_positin and Enemy_y_positin < (player_y_positin + size_of_player)) or (player_y_positin >= Enemy_y_positin and player_y_positin < (Enemy_y_positin + size_of_enemy)):
            return True
    return False

""" CHECK the COLLISION  """
def Colli_c(LIST_Enemy,PLAYER):
    for Enemy in LIST_Enemy:
        if COLLI(Enemy, PLAYER):
            return True
    return False 

"""Gane is just started""" 
GAME_OVER = False
playerPosition_X = PLAYER[0]                #taking the current position of player
playerPosition_Y = PLAYER[1]
playerSpeed = 0
while not GAME_OVER:
    
    """ Watch for keyboard and mouse events"""
    for every_event in pygame.event.get():   #pygame 'event' track everything that we do on the screen
        if every_event.type == pygame.QUIT:   # To quit from the screen
            sys.exit() 
        if every_event.type == pygame.KEYDOWN:       #for making the movement of the player 

            
            if every_event.key == pygame.K_LEFT:
                playerSpeed = -10                   #Move the player to the left
            elif every_event.key == pygame.K_RIGHT:
                playerSpeed = 10                      #Move the player to the right

        if every_event.type == pygame.KEYUP:
            if every_event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerSpeed = 0

    playerPosition_X += playerSpeed
    PLAYER = (playerPosition_X, playerPosition_Y)  # new position of player

    # Boundaries to the Player
    if playerPosition_X >= (width_screen - size_of_player):
        playerPosition_X = (width_screen - size_of_player)  # if it comes at right end, stay at right end and does not exceed
    if playerPosition_X <= 0:
        playerPosition_X = 0  # if it comes at left end, stay at left end and does not exceed

    SCREEN_Display.fill(SCREEN_COLOR)  

    """ To move the block down in a loop"""
    """ UPDATW - the position of Enemy"""
    

    enemy_fall(LIST_Enemy)
    GAME_SCORE =  EnemyUpdat(LIST_Enemy, GAME_SCORE)
    
    Enemy_speed = SPEED_LEVEL(GAME_SCORE, Enemy_speed)
    
    """presenting the SCORE"""
    STRING = "Score:" + str(GAME_SCORE)         # 'str' represent the number in the form of string
    L = myFont.render(STRING,1, red)
    SCREEN_Display.blit(L,(600,580))      #attach the SCORE to the SCREEN 
    
    """Giving instruction to the player"""
    HEADING = "press ' > ' to move right, press '<' to move left"
    L1 = myFont.render(HEADING,1, Green)
    SCREEN_Display.blit(L1,(70,0))
    
    winner(GAME_SCORE,GAME_OVER)
      
    
    """if collision_ happen than stop the game and print the following"""
    if Colli_c(LIST_Enemy,PLAYER):
        GAME_OVER = True
        print()
        print("GAME OVER , your score is -" ,GAME_SCORE)
        print()
        print("try again you are a amazing player")
        break
    EnemyDraw(LIST_Enemy)
    pygame.draw.ellipse(SCREEN_Display, Green, (PLAYER[0],PLAYER[1],size_of_player,size_of_player))     # Representation of player Block
    
    """To slow down the speed of enemy block"""
    pygame.time.wait(30)
    pygame.display.update()