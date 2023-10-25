# CmdLine-FreeCell-Solitaire
Simple command line implementation of FreeCell utilizing OOP Python programming principles

# FreeCell Solitaire

## The Game
 The goal of FreeCell is for a player to shuffle cards between deck and free cell piles in
 order to put the required card on foundation piles. 
 Victory is achieved when all four foundation piles are filled with their respective suits from Ace to King 
 i.e., Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King
 

 ## Freecell Class
 The Freecell class drives the main logic of the game. it calls on the 'Card' and 'Deck' class to generate a game of FreeCell using text and the terminal. 
 
 ### How it works:
     The game starts by initialising a Deck object built using the parameters of the constructor.
     It then declares the playing fields of the game by creating fixed arrays for the pile, foundation, and cell.
 
 ## Methods of the Class
 ### Display Methods
     These are methods used to print important game information to the player:
     
     display_game(self):
     display_pile(self):
     display_foundation(self):
     display_cell(self):
     welcome_message(self)
     
 ### Movement Check Methods
     Boolean checks to confirm whether the specified movements are legal.
     These methods operate by checking whether the proposed positions are first legal. then by checking
     whether the proposed movement meets the rules of the game. The methods are:
     
     check_pile_to_cell(self, pile_index, cell_index):
     check_cell_to_pile(self, cell_index, pile_index):
     check_pile_to_foundation(self, pile_index, foundation_index):
     check_pile_to_pile(self, pile1_index, pile2_index):
     check_cell_to_foundation(self, cell_index, foundation_index):
     
 ### Movement Methods
     These methods perform the action of moving a Card object from one game area to another.
     The main two functions called in these methods are the append() function and the pop() function.
     pop() removes the top card from an area and append() adds it to the top of thenew area.
     The methods are:
     
     move_pile_to_cell(self, pile_index, cell_index):
     move_cell_to_pile(self, cell_index, pile_index):
     move_pile_to_pile(self, pile1_index, pile2_index):
     move_cell_to_foundation(self, cell_index, foundation_index):
     move_pile_to_foundation(self, pile_index, foundation_index):

## Deck Class
The deck class will contain the logic of the implementing a deck of 53 cards. The deck class takes a parameter of the following values to build a custom deck: 

    A starting value ( Eg. 1 )
    An ending value  ( Eg. 13 )
    Number of suits  ( Eg. 4 )

## Card Class
The card class will contain the logic to represent a card within the game of FreeCell. Each card will have:

    A face value ( Ace, 1, 2, 3, 4 ...)
    A suit (♠ ♥ ♦ ♣)