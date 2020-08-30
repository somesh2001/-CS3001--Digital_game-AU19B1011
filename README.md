# -CS3001-Digital_game---AU19B1011
Description of game –
There are multiple Blue blocks which continuously falls on the single green block. The green block try to dodge the blue blocks and I set the score, as the game started the counting of score also started. And as the score increases the speed of the red blocks to fall down is also increases and as the speed increases it becomes difficult for the player to survive. 

Goal of the player – 
The goal of the player is not to collide with the enemies. Player goal is to survive from the  enemies.

Rules – 
•	Single player game.
•	Player can move the green block in the way he want. (left or right)
•	Player controls the green block and try to dodge blue block that are falling from the top.
•	As the game begin the score starts counting.
•	As the score increases the speed of the block to fall down is increases as well.
•	The goal of the player is not to collide with the enemies (blue block). Player goal is to survive from enemies.

Reference of documentation –
https://www.pygame.org/docs/ref/draw.html

![Image](https://github.com/somesh2001/-CS3001-Digital_game---AU19B1011/blob/master/Screenshot%20(892).png)
![Image](https://github.com/somesh2001/-CS3001-Digital_game---AU19B1011/blob/master/github.png)

import pygame

pygame.init()          #initialise the pygame


width_screen = 820
height_screen = 620

"""screen"""

SCREEN_Display = pygame.display.set_mode((width_screen,height_screen ))   #creating the screen using pygame and pass the tuple as 'width' and 'height' of screen

""" player size, position and color"""
Green = (0,128,0)        #green colour RGB
PLAYER = [410,500]               #set the parameters of player(400 = left, 305 = right, 55)
size_of_player = [55,55]         # set the size of the player height, 55 = widht) 

""" Enemie size, position and color"""
red = (255,0,0)
Enemy = [400,0]               #set the parameters of Enimie(100 = left, 0 = top)
size_of_Enemy = [55,55] 

pygame.draw.ellipse(SCREEN_Display, Green, (PLAYER[0],PLAYER[1],size_of_player[0],size_of_player[1])) 

pygame.draw.ellipse(SCREEN_Display, red, (Enemy[0],Enemy[1],size_of_Enemy[0],size_of_Enemy[1]))        
pygame.display.update()

