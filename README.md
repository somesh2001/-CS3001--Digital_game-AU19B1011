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

Technical requirements –
Module:
Pygame – 
The pygame library is an open-source module for the Python programming language specifically intended to help you make games.
1) You control your main loop - You call pygame functions, they don't call your functions.   This gives you greater control when using other libraries, and for different types of programs.      
2) Small amount of code - It does not have hundreds of thousands of lines of code for things you won't use anyway. The core is kept simple, and extra things like GUI libraries, and effects are developed separately outside of pygame.                                     
Sys module –
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
Random module –
Python has a built-in module that you can use to make random numbers.                 	  
The module has a sets of different – different method.

Design and implementation – 
•	How to display the screen
•	How to display player block and enemy Block on the screen
•	Player and Enemy block should have different colours
•	Move the player block left and right
•	Try to Fall down the enemy block
•	Set the position of enemy to a random value, so it appear randomly at any place on the screen at the top.
•	Bunch of Enemy fall down randomly on the player block. 
•	Try to detect collision between the player block and the Enemy block
•	If there is the collision between the player block and enemy block than stop the game
•	Try to display the score on the screen.
•	Score - We want our score to increase as we (player) successfully dodge each enemy block.
•	As the score reaches to 20 the speed of the enemy block to fall down is also increases.
•	Next incrementation in the speed when the score reaches to 40,60 and the last incrementation in the speed when the score reaches to 80.


