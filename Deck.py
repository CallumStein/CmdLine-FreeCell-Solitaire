#!/usr/bin/env python
# coding: utf-8

# ## Deck Class
# The deck class will contain the logic of the implementing a deck of 53 cards. The deck class takes a parameter of the following values to build a custom deck: 
# 
#     A starting value ( Eg. 1 )
#     An ending value  ( Eg. 13 )
#     Number of suits  ( Eg. 4 )

# In[ ]:


# Import the 'random' module of python. Used for shuffling
import random
from Card import *

class Deck:
    
    def __init__(self, value_start = 1, value_end = 13, number_of_suits = 4):
        
        self.deck = []
        
        # Perform a check on starting point to not be less than 0
        if value_start < 1:
            value_start = 1
            
        # Slice the card_indexs based on the parameters specified
        for suit in Card.suit_index[0:number_of_suits]:
            for face in Card.face_index[(value_start-1):(value_end)]:
                self.deck.append(Card(face, suit))
    
    # Shuffles the generated deck, uses the 'random' function shuffle()
    # shuffle(seq, func) -> Takes a sequence and returns the sequence in a random order
    # https://www.w3schools.com/python/ref_random_shuffle.asp
    def shuffle(self):
        random.shuffle(self.deck)
    
    #  Display method to print each card in the deck
    def display(self):
        for card in self.deck:
            print(card, end=" ")
    
    # Boolean check to see if the deck is empty
    def is_empty(self):
        if len(self.deck) == 0:
            return True
        else:
            return False
                
    # returns the card at a specific position in the deck
    def get_card(self, index):
        if self.is_empty() != True:
            if index > 0 and index < len(self.deck):
                return self.deck[index]
        else:
            return None
        
    # Removes the last element (Top Card) of the deck
    def draw_card(self):
        if self.is_empty() != True:
            return self.deck.pop()
        else:
            return None
    
    # Puts a card on the bottom of the deck
    def add_card(self, card):
        self.deck.insert(0, card)
    
    # Formatted string for print() function
    def __str__(self):
        formatted_str = ""
        
        # for each card in the deck, get the suit and face values
        for card in self.deck:
            formatted_str += str(card.get_suit()) + str(card.get_face()) + " "
        
        # return the string of all cards
        return formatted_str
    
    # Override length function to return the length of the object deck attribute
    def __len__(self):
        return len(self.deck)
    
    
    # main defined for testing purposes
    if __name__ == "__main__":
        #Instantiating an object from the Deck class
        deck1 = Deck(1,13,4)
        
        # Test the __str__ override method of the Deck Class
        print(deck1)
        
        # Test the __len__ override method of the Deck Class
        print("length of the deck is: " + str(len(deck1)))
        
        # Test the functionality of the shuffle() method
        print("shuffle the deck ->")
        deck1.shuffle()
        
        # Test the display method of the Deck Class
        deck1.display()
        
        # Test the accessor methods of the Deck Class
        print("is empty: " + str(deck1.is_empty()))
        print("get_card: " + str(deck1.get_card(10)))
        
        # Test the function of the draw_card() method
        print("draw a card ->", end=" ")
        card = deck1.draw_card()
        print(card)
        print("length of the deck is: " + str(len(deck1)))
        
        # Test the function of the add_card() method
        deck1.add_card(card)
        deck1.display()
        print("length of the deck is: " + str(len(deck1)))
    