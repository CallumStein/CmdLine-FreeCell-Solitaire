#!/usr/bin/env python
# coding: utf-8

# ## Card Class
# The card class will contain the logic to represent a card within the game of FreeCell. Each card will have:
# 
#     A face value ( Ace, 1, 2, 3, 4 ...)
#     A suit (♠ ♥ ♦ ♣)

# In[ ]:


class Card:
    # An index of acceptable values for a card
    face_index = ['A', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K']
    
    # the value weight of each card
    face_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                  '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'J': 11, 'Q': 12, 'K': 13}
    
    # An index to refer to for card suits and emoji(unicode) number
    suit_index = ['s', 'h', 'd', 'c'] 
    emoji_index = {'s':'\u2660', 'h':'\u2665', 'd':'\u2666', 'c':'\u2663'}
    
    # Constructor method to create a card
    def __init__(self , face = None, suit = None):
        
        self.card_face = face
        self.card_suit = suit
        
    # Displays all values of the 'Card' object
    def display(self):
        print(self.card_suit + self.card_face)
    
    # Accessor method to return the face value of the card
    def get_face(self):
        return self.card_face
    
    # Accessor method to return the weight of a card based on face_dict
    def get_weight(self):
        return self.face_dict.get(self.card_face)
    
    # Accessor method to return the suit of the card
    def get_suit(self):
        if self.card_suit in Card.emoji_index.keys():
            return (Card.emoji_index.get(self.card_suit))
    
    # Method to return the colour of the card
    def get_colour(self):
        if self.card_suit == 'd' or self.card_suit == 'h':
            return 'R'
        elif self.card_suit == 's' or self.card_suit == 'c':
            return 'B'
    
    # Mutator method to set the face of the card
    def set_face(self, value):
        if self.verify_face(value) == True:
            self.card_face = value
    
    # Mutator method to set the suit of the card
    def set_suit(self, value):
        # Check to see if the value is valid than assign a colour
        if self.verify_suit(value) == True:
            self.card_suit = value
    
    # Returns true if the face value is acceptable
    def verify_face(self, face):
        if face in self.face_index:
            return True
        else:
            return False
    
    # Returns true if the suit value is acceptable
    def verify_suit(self, suit):
        if suit in self.suit_index:
            return True
        else:
            return False
        
    # Formatted string for print() function
    def __str__(self):
        formatted_str = ""
        
        # Switch the char value of the suit for a unicode emoji
        if self.card_suit in Card.emoji_index.keys():
            formatted_str = str(Card.emoji_index.get(self.card_suit))
            
        # Concatenate the suit and face together
        formatted_str += str(self.card_face)
        return formatted_str
    
    
    # main defined for testing purposes
    if __name__ == "__main__":
        
        #Instantiating 2 objects from the Card class
        card1 = Card()
        card2 = Card('Q','h')
        
        # Test the functionality of the Mutator methods
        card1.set_face('A')
        card1.set_suit('s')
        
        # Test the __str__ function of the card
        print(card1, end=" ")
        
        # Test the display() method of the card
        card1.display()
        
        # Test the functionality of the verify methods
        print(card1.verify_face(card1.card_face), end =" ")
        print(card1.verify_suit(card1.card_suit), end =" ")
        
        # Test the functionality of the accessor methods
        print(card1.get_face(), end=" ")
        print(card1.get_suit(), end=" ")
        print(card1.get_colour(), end =" ")
        print(card1.get_weight())
        
        # Test the __str__ function of the card
        print(card2, end=" ")
        
        # Test the display() method of the card
        card2.display()
        
        # Test the functionality of the verify methods
        print(card2.verify_face(card1.card_face), end =" ")
        print(card2.verify_suit(card1.card_suit), end =" ")
        
        # Test the functionality of the accessor methods
        print(card2.get_face(), end=" ")
        print(card2.get_suit(), end=" ")
        print(card2.get_colour(), end =" ")
        print(card2.get_weight())
    