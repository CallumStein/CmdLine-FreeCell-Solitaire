#!/usr/bin/env python
# coding: utf-8

# # FreeCell Solitaire

# ## The Game
# The goal of FreeCell is for a player to shuffle cards between deck and free cell piles in
# order to put the required card on foundation piles. 
# Victory is achieved when all four foundation piles are filled with their respective suits from Ace to King 
# (i.e., Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King
# 

# ## Freecell Class
# The Freecell class drives the main logic of the game. it calls on the 'Card' and 'Deck' class to generate a game of FreeCell using text and the terminal. 
# 
# ### How it works:
#     The game starts by initialising a Deck object built using the parameters of the constructor.
#     It then declares the playing fields of the game by creating fixed arrays for the pile, foundation, and cell.
# 
# ## Methods of the Class
# ### Display Methods
#     These are methods used to print important game information to the player:
#     
#     display_game(self):
#     display_pile(self):
#     display_foundation(self):
#     display_cell(self):
#     welcome_message(self)
#     
# ### Movement Check Methods
#     Boolean checks to confirm whether the specified movements are legal.
#     These methods operate by checking whether the proposed positions are first legal. then by checking
#     whether the proposed movement meets the rules of the game. The methods are:
#     
#     check_pile_to_cell(self, pile_index, cell_index):
#     check_cell_to_pile(self, cell_index, pile_index):
#     check_pile_to_foundation(self, pile_index, foundation_index):
#     check_pile_to_pile(self, pile1_index, pile2_index):
#     check_cell_to_foundation(self, cell_index, foundation_index):
#     
# ### Movement Methods
#     These methods perform the action of moving a Card object from one game area to another.
#     The main two functions called in these methods are the append() function and the pop() function.
#     pop() removes the top card from an area and append() adds it to the top of thenew area.
#     The methods are:
#     
#     move_pile_to_cell(self, pile_index, cell_index):
#     move_cell_to_pile(self, cell_index, pile_index):
#     move_pile_to_pile(self, pile1_index, pile2_index):
#     move_cell_to_foundation(self, cell_index, foundation_index):
#     move_pile_to_foundation(self, pile_index, foundation_index):

# In[ ]:

# Import the necessary classes

from Deck import *


class Freecell():
    
    # Create Class variables for game condition flags for use during the game
    win_flag = False
    quit_flag = False
    
    # Constructor method to declare the necessary play elements of the game FreeCell
    def __init__(self, value_start = 1, value_end = 13, number_of_suits = 4):
        
        # Create a deck based on the conditions from the player and store the size of the deck
        self.deck = Deck(value_start, value_end, number_of_suits)
        self.deck_size = len(self.deck)
        
        # Define the playing field for the user
        self.pile = [[],[],[],[],[],[],[],[]]
        self.foundation = [[],[],[],[]]
        self.cell = [[],[],[],[]]
    
    # Formatted string for print() function, returns the cards currently in all play fields
    def __str__(self):
        formatted_str = ""
        
        # Print the cards currently in the cells
        formatted_str += "Cell cards: "
        for cell in self.cell:
            for card in cell:
                formatted_str += str(card.get_suit()) + str(card.get_face()) + ' '
        
        # Print the cards currently in the piles
        formatted_str += '\n'
        formatted_str += "Pile cards: "
        for pile in self.pile:
            for card in pile:
                formatted_str += str(card.get_suit()) + str(card.get_face()) + ' '
        
        # Print the cards current in the foundations
        formatted_str += '\n'
        formatted_str += "Foundation cards: "
        for foundation in self.foundation:
            for card in foundation:
                formatted_str += str(card.get_suit()) + str(card.get_face()) + ' '
        
        # return the string of all cards
        return formatted_str
    
    # Prepares the game to be played and loads the piles for the player
    def game_start(self):
        
        # Shuffle the deck object
        self.deck.shuffle()
        
        # Create an index variable to keep track of the pile
        index = 0
        
        # While there are cards in the deck draw a card
        # and add it to the current pile
        while self.deck.is_empty() != True:
            self.pile[index].append(self.deck.draw_card())
            index += 1
            
            # if the pile index is greater than 7 move it back to start
            if index > 7:
                index = 0
    
    # Boolean condition to check if the foundations are full, if they are full set the win flag for the player
    def check_win(self):
        counter = 0
        
        # Scans all the cards currently in the foundations and keeps track of the number
        for suit in self.foundation:
            for cards in suit:
                counter += 1
        
        # If the number of cards in the foundations the same as the number of cards in play the player wins
        if counter == self.deck_size:
            self.win_flag = True
        else:
            return False
        
    """ ***   DISPLAY METHODS   *** """
    
    # display The board state of the game by calling on the other display methods
    def display_game(self):
        print()
        print("Cells: " + "\t\t\t\t\t" + "Foundation: ")
        self.display_cell()
        print(end="\t")
        self.display_foundation()
        print("-----------------------------------------------------------------------")
        self.display_pile()
        print("-----------------------------------------------------------------------")
    
    
    # display each card in the piles to the player
    def display_pile(self):    
        # iterate over each pile
        for i in range(len(self.pile)):
            print()
            print(f"pile {i}:", end="   ")
            # For each card in each pile, print the card value
            for j in self.pile[i]:
                print(" | " + j.get_suit() + j.get_face(), end=" | ")
            print()
    
    
    # display the top card of the foundation to the player
    def display_foundation(self):
        # iterate over each foundation
        for card in self.foundation:    
            # if the list is empty print a blank card
            if not card:
                print(" |...| ", end=" ")
            # else show the top of the foundation
            else:
                print("| " + str(card[-1]) + " |", end=" ")
        
        # Move to next line
        print()
    
    
    # display the current cards in the cells to the player
    def display_cell(self):
        # iterate over each cell
        for card in self.cell:    
            # if the list is empty print a blank card
            if not card:
                print(" |...| ", end=" ")
            # else show the top of the foundation
            else:
                print("| " + str(card[-1]) + " |", end=" ")
    
    
    # Print a welcome banner and the instructions of the game to the player
    def welcome_message(self):
        
        print("""
 _______  ______    _______  _______  _______  _______  ___      ___     
|       ||    _ |  |       ||       ||       ||       ||   |    |   |    
|    ___||   | ||  |    ___||    ___||       ||    ___||   |    |   |    
|   |___ |   |_||_ |   |___ |   |___ |       ||   |___ |   |    |   |    
|    ___||    __  ||    ___||    ___||      _||    ___||   |___ |   |___ 
|   |    |   |  | ||   |___ |   |___ |     |_ |   |___ |       ||       |
|___|    |___|  |_||_______||_______||_______||_______||_______||_______|
        """)
        print("""
The game follows the following rules:
● Only one card may be moved at a time.
    o move from deck pile to an empty free cell pile
        ▪ Any card may be placed in an empty free cell pile.
    o move from one deck pile to another deck pile or from free cell pile to deck pile
        ▪ it must be placed on a card of the opposite colour, and of a suit
            that is one higher than itself. E.g. a red 2 can be placed on a
            black 3, but not a red 3 or black 1. (i.e., descending order)
    o move from deck pile or free cell pile to foundation pile
        ▪ only Ace card can be placed in an empty foundation pile
        ▪ Each foundation must be built starting from the Ace of the
        appropriate suit, followed by the 2, then the 3 etc. until the King
        is placed. (i.e, ascending order)
    o move from foundation pile to free cell pile
        ▪ Cards from the foundations can not be placed back onto a deck
        pile.
● Only one card at a time can occupy a free cell pile.
""")
        
    """ ***   TURN CHOICE METHOD   *** """
    
    # Prompts the user with a menu of choices then asks for an input. the input is checked
    # to the menu options and if the input is valid, the appropiate movement method is called
    def turn_choice(self):
        
        print("""
        Player turn choices are:
            p2p --> pile to pile.
            p2f --> pile to foundation.
            p2c --> pile to cell.
            f2c --> foundation to cell.
            c2p --> cell to pile.
            c2f --> cell to foundation.
            ---------------------------
            or type 'q' to quit..
        """)
        
        # Take an input from the player and remove an extra empty space
        choice = input("Please choose your move: ")
        choice = choice.strip()
        
        # If the player chose 'p2p', prompt them to input 2 numbers then call the 'move_pile_to_pile' method
        if choice == "p2p":
            location_1 = input("Please choose the origin: ")
            location_2 = input("Please choose the destination: ")
            if location_1.isdigit() and location_2.isdigit():
                self.move_pile_to_pile(int(location_1), int(location_2))
            else:
                print("Please use only numbers")
        
        # If the player chose 'p2f', prompt them to input 2 numbers then call the 'move_pile_to_foundation' method
        if choice == "p2f":
            location_1 = input("Please choose the origin: ")
            location_2 = input("Please choose the foundation: ")
            if location_1.isdigit() and location_2.isdigit():
                self.move_pile_to_foundation(int(location_1), int(location_2))
            else:
                print("Please use only numbers")
        
        # If the player chose 'p2c', prompt them to input 2 numbers then call the 'move_pile_to_cell' method
        if choice == "p2c":
            location_1 = input("Please choose the origin: ")
            location_2 = input("Please choose the cell: ")
            if location_1.isdigit() and location_2.isdigit():
                self.move_pile_to_cell(int(location_1), int(location_2))
            else:
                print("Please use only numbers")
                
        # If the player chose 'f2c', prompt them to input 2 numbers then call the 'move_foundation_to_cell' method
        if choice == "f2c":
            location_1 = input("Please choose the origin: ")
            location_2 = input("Please choose the cell: ")
            if location_1.isdigit() and location_2.isdigit():
                self.move_foundation_to_cell(int(location_1), int(location_2))
            else:
                print("Please use only numbers")
        
        # If the player chose 'c2p', prompt them to input 2 numbers then call the 'move_cell_to_pile' method
        if choice == "c2p":
            location_1 = input("Please choose the cell: ")
            location_2 = input("Please choose the pile: ")
            if location_1.isdigit() and location_2.isdigit():
                self.move_cell_to_pile(int(location_1), int(location_2))
            else:
                print("Please use only numbers")
        
        # If the player chose 'c2f', prompt them to input 2 numbers then call the 'move_cell_to_foundation' method
        if choice == "c2f":
            location_1 = input("Please choose the cell: ")
            location_2 = input("Please choose the foundation: ")
            if location_1.isdigit() and location_2.isdigit():
                self.move_cell_to_foundation(int(location_1), int(location_2))
            else:
                print("Please use only numbers")
        
        # If the player chose 'q', double check they made the right choice then set the game flag for exiting the game
        if choice == 'q':
            print("Are you sure you want to quit? ")
            choice = input("Y / N :")
        
            if choice.lower() == "y":
                self.quit_flag = True
            else:
                return False
        
        
    """ ***   MOVEMENT CHECK METHODS   *** """
    
    # Boolean check to see if moving a card from a pile to cell is legal
    def check_pile_to_cell(self, pile_index, cell_index):
        
        # Check that the pile index is within range
        if pile_index >= 0 and pile_index < 8:
            pile = self.pile[pile_index]
        else:
            return False
        
        # Check if the pile is empty
        if pile == []:
            return False
        
        # Check that the cell index is within range
        if cell_index >= 0 and cell_index < 4:
            # Check if the specified cell is empty
            if self.cell[cell_index] == []:
                return True
            else:
                return False       
        
        return False
    
    # Boolean check to see if moving a card from a foundation to cell is legal
    def check_foundation_to_cell(self, foundation_index, cell_index):
        
        # Check that the foundation index is within range
        if foundation_index >= 0 and foundation_index < 4:
            foundation = self.foundation[foundation_index]
        else:
            return False
        
        # Check if the foundation is empty
        if foundation == []:
            return False
        
        # Check that the cell index is within range
        if cell_index >= 0 and cell_index < 4:
            # Check if the specified cell is empty
            if self.cell[cell_index] == []:
                return True
            else:
                return False       
        
        return False
    
    # Boolean check to see if moving a card from a cell to pile is legal
    def check_cell_to_pile(self, cell_index, pile_index):
        
        # Check that the cell index is within range
        if cell_index >= 0 and cell_index < 4:
            # Check if the cell is empty
            if self.cell[cell_index] == []:
                return False
            else:
                # Store the cell if it is legal and has a card
                cell = self.cell[cell_index]
        else:
            return False
        
        # Check that the pile index is within range
        if pile_index >= 0 and pile_index < 8:
            pile = self.pile[pile_index]
        else:
            return False
    
        # Check if the pile is empty
        if pile == []:
            return True
        
        # check if the colours of the cards are different
        else:
            if cell[-1].get_colour() != pile[-1].get_colour():
                # Check that the weight difference is one different
                if (cell[-1].get_weight() + 1) == pile[-1].get_weight():
                    return True
                else:
                    return False
            else:
                return False
    
    
    # Boolean check to see if moving a card from a pile to foundation is legal
    def check_pile_to_foundation(self, pile_index, foundation_index):
        
        # Check that the pile index is within range
        if pile_index >= 0 and pile_index < 8:
            pile = self.pile[pile_index]
        else:
            return False
        
        # Check that the foundation index is within range
        if foundation_index >= 0 and foundation_index < 4:
            foundation = self.foundation[foundation_index]
        else:
            return False
        
        # check if the pile is empty and return false if it is
        if pile == []:
            return False
        
        else:
            # Check if the foundation currently has no cards in it
            if foundation == []:
                # If there are no cards in the foundation and the top card is an Ace return true
                if pile[-1].card_face == 'A':
                    return True
                else:
                    return False
            
            # If there are cards in the foundation
            else:
                # Check that the suit of the top card in the pile matches
                if foundation[-1].card_suit == pile[-1].card_suit:
                    # Check if the weight of the top card is 1 higher than the foundation
                    if (foundation[-1].get_weight() + 1) == pile[-1].get_weight():
                        return True
                else:
                    return False
    
    
    # Boolean check for moving a card from one pile to another pile
    def check_pile_to_pile(self, pile1_index, pile2_index):
        
        # Check that the 1st pile index is within range
        if pile1_index >= 0 and pile1_index < 8:
            pile_origin = self.pile[pile1_index]
        else:
            return False
        
        # Check that the 2nd pile index is within range
        if pile2_index >= 0 and pile2_index < 8:
            pile_dest = self.pile[pile2_index]
        else:
            return False
        
        # Check if the origin is empty
        if pile_origin == []:
            return False
        
        # else if the destination is empty
        else:
            if pile_dest == []:
                return True
        
            # check if the colours of the cards are different
            else:
                if pile_origin[-1].get_colour() != pile_dest[-1].get_colour():
            # Check that the weight difference is one different
                    if (pile_origin[-1].get_weight() + 1) == pile_dest[-1].get_weight():
                        return True
                    else:
                        return False
                else:
                    return False
    
    
    # Boolean check to see if moving a card from a cell to foundation is legal
    def check_cell_to_foundation(self, cell_index, foundation_index):
    
        # Check that the cell index is within range
        if cell_index >= 0 and cell_index < 4:
            # Check if the cell is empty
            if self.cell[cell_index] == []:
                return False
            else:
                # Store the cell if it is legal and has a card
                cell = self.cell[cell_index]
        else:
            return False
        
        # Check that the foundation index is within range
        if foundation_index >= 0 and foundation_index < 4:
            foundation = self.foundation[foundation_index]
        else:
            return False
        
        # Check if the foundation is empty
        if foundation == []:
            # If the foundation is empty check that the cell card is an Ace
            if cell[-1].get_face() == 'A':
                return True
            else:
                return False
            
        # If the foundation isn't empty check the weight of the two cards
        else:
            # Check that the suit of the top card in the pile matches
            if foundation[-1].card_suit == cell[-1].card_suit:
                # Check if the weight of the top card is 1 higher than the foundation
                if (foundation[-1].get_weight() + 1) == cell[-1].get_weight():
                    return True
                else:
                    return False
            else:
                return False
    
    
    """ ***   CARD MOVEMENT METHODS   *** """
    
    # Move the specified card to cell if the move is legal
    def move_pile_to_cell(self, pile_index, cell_index):
        
        # call the check method, if it is True, append the top card of the pile to the cell
        if self.check_pile_to_cell(pile_index, cell_index) == True:
            self.cell[cell_index].append(self.pile[pile_index].pop())
        else:
            print("Chosen card can't be moved to the cell.")
    
    # Move the specified card to the cell if the move is legal
    def move_foundation_to_cell(self, foundation_index, cell_index):
        if self.check_foundation_to_cell(foundation_index, cell_index) == True:
            self.cell[cell_index].append(self.foundation[foundation_index].pop())
        else:
            print("Chosen card can't be moved to the cell.")
    
    # Move the specified cell to the pile if the move is legal
    def move_cell_to_pile(self, cell_index, pile_index):
        
        # call the check method, if it is True, append the card in the cell to the top of the pile
        if self.check_cell_to_pile(cell_index, pile_index) == True:
            self.pile[pile_index].append(self.cell[cell_index].pop())
        else:
            print("Chosen card can't be moved to the pile.")
    
    
    # Move the specified card to the pile if the move is legal
    def move_pile_to_pile(self, pile1_index, pile2_index):
        
        # call the check method, if it is True, append the top card of the pile to the specified pile
        if self.check_pile_to_pile(pile1_index, pile2_index) == True:
            self.pile[pile2_index].append(self.pile[pile1_index].pop())
        else:
            print("Chosen card can't be moved to the pile.")
    
    
    # Move the specified cell to the foundation if the move is legal
    def move_cell_to_foundation(self, cell_index, foundation_index):
        
        # call the check method, if it is True, append the top card of the cell to the foundation
        if self.check_cell_to_foundation(cell_index, foundation_index) == True:
            self.foundation[foundation_index].append(self.cell[cell_index].pop())
        else:
            print("Chosen card can't be moved to the foundation.")
    
    
    # Move the specified card to the foundation if the move is legal
    def move_pile_to_foundation(self, pile_index, foundation_index):
        
        # call the check method, if it is True, append the top card of the pile to the foundation
        if self.check_pile_to_foundation(pile_index, foundation_index) == True:
            self.foundation[foundation_index].append(self.pile[pile_index].pop())
        else:
            print("Chosen card can't be moved to the foundation.")
    
    
    """ ***   TESTING METHODS   *** """
    
    # This main method calls various other methods of the class for testing purposes
    def main(self):
        # Run the display methods before the game starts to show empty field
        self.display_game()
       
        # start the game and print the playing field
        self.game_start()
        self.display_game()
        
        # test each movement check multiple times using for loops
        for i in range(2):
            for j in range(2):
                print(f"p2c -> origin: {i} dest: {j} Is move legal?: {self.check_pile_to_cell(i,j)}")
                print(f"p2f -> origin: {i} dest: {j} Is move legal?: {self.check_pile_to_foundation(i,j)}")
                print(f"p2p -> origin: {i} dest: {j} Is move legal?: {self.check_pile_to_pile(i,j)}")
                print(f"c2f -> origin: {i} dest: {j} Is move legal?: {self.check_cell_to_foundation(i,j)}")
                print(f"c2p -> origin: {i} dest: {j} Is move legal?: {self.check_cell_to_pile(i,j)}")
        
        # test each movement method multiple times and check the outputs
        for i in range(2):
            for j in range(2):
                self.move_pile_to_cell(i, j)
                self.move_pile_to_foundation(i, j)
                self.move_pile_to_pile(i, j)
                self.move_cell_to_foundation(i, j)
                self.move_cell_to_pile(i, j)
        
        # Display the game again after moves
        self.display_game()
        
        
if __name__ == "__main__":    
    # Prompt the user for the range of cards
    end_face = int(input("Input highest card value: "))
    suits = int(input("Input number of suits: "))
        
    #Instantiating an object from the Deck class
    new_game = Freecell(1, end_face, suits)
    new_game.welcome_message()
    new_game.game_start()
        
    # While the goal flags are false, continue prompting the user for actions
    while (new_game.check_win() == False) and (new_game.quit_flag == False):
        new_game.display_game()
        new_game.turn_choice()
        
    # Check which flag was triggered and print the appropiate message    
    if new_game.win_flag == True:
        print("YOU WIN CONGRATULATIONS!")
        
    elif new_game.quit_flag == True:
        print("Thank you for playing!")
            
    input("")