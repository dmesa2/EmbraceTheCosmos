# Embrace The Cosmos
Copyright (c) 2019 Jeff Lund, Dennis Mesanovic, Mirko Draganic


A space based roguelike deckbuilder. 
The goal is to make it to the end of each sector fighting enemies and building up your ship.

## Gameplay Concepts
The player starts with a 10 card deck of 5 of each basic cards (attack and defense). The player will traverse up nodes completing encounters. 
Encounters include fighting an enemy, a shop, a rest station, or an event.

Enemy: Starts an encounter with turn based combat. Upon defeat the player is given a reward and the option to add an additionaly card to their deck.

Shop: The player can spend gold earned to buy cards from a fixed offering.

Rest station: The player can repair their ship, restoring health.

Event: Triggers a special event or enemy encounter.


### Combat
The player can spend cards to perform offensive or defensive actions. The cards the play is limited by how much energy their ship has to expend each turn. After the player completes their turn each enemy will take their action. At the end of each turn the player discards their hand and draws new cards up to full. Whenever the players deck is exhausted then their discard pile is reshuffled back into their deck.
 Enemy actions are defined by a fixed set of actions. 

Combat ends when all enemies are reduced to 0 or when the player reaches 0. 



## Run Information
Pygame 1.9.6 is required to run this program.  
[www.pygame.org/](https://www.pygame.org/)    
All dependencies can be installed through the reqirements file `pip3 install -r requirements.txt`  

There can be compatability issues with Mac. More information [here](https://github.com/pygame/pygame/issues/555)    
[Potential fix](https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave)    

To run `python3 main.py`

## Tutorial
Coming soon!

## Acknowledgments
[Free Pixel Art Enemy Spaceship 2D Sprites](https://free-game-assets.itch.io/free-enemy-spaceship-2d-sprites-pixel-art)
Icons made by [delapouite](http://delapouite.com), [lorc](http://lorcblog.blogspot.com), sourced from [game-icons.net](https://game-icons.net).  


## License
This program is licensed under the "MIT License". Please see the `LICENSE` file in source distribution for license terms.



