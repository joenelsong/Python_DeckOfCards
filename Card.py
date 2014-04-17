# CIS 211 Spring 2014
# Project 2
# Author: Joseph Nelson
from random import* # shuffle(<cardlist>)  #sample
from itertools import chain

class Card:
    # Class Variables   
    suitsdict = {0: 'C', 1: 'D', 2: 'H', 3: 'S'}  # 0: Clubs, 1: Diamonds, 2: Hearts, 3: Spades
    ranksdict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12}
    symbsdict = {0: "2", 1: "3", 2: "4", 3: "5", 4: "6", 5: "7", 6: "8", 7: "9", 8: "10", 9: "J", 10: "Q", 11: "K", 12: "A"}
    pointsdict = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "J": 1, "Q": 2, "K": 3, "A": 4 } # Default point scoring is bridge scoring
    # Class Methods 
    def __init__(self, n):
        '''the constructor (actually "initiator")'''
        self._id = n
        if n > 51:
            raise Exception('Invalid card id. Card ids mustbe between 0 and 51')
        
    def num(self):
        ''' a "getter" (return the value of an attribute)'''
        return (self._id)
        
    def rank(self):
        ''' identifies a card's rank'''
        return Card.ranksdict[(Card.num(self) % 13)]
        
    def suit(self):
        ''' identifies a card's suit'''
        return (Card.num(self) // 13)
        
    def symb(self):
        ''' identifies a card's rank'''
        return Card.symbsdict[(Card.num(self) % 13)]
    
    def points(self):
        ''' identifies a card's point value'''
        return Card.pointsdict[Card.symb(self)]
    
    def __repr__(self):
        return str(Card.symbsdict[Card.rank(self)]) + str(Card.suitsdict[Card.suit(self)])

    def __lt__(self, other):
        return self._id < other._id
    # Class Functions
    def shuffle(deck):
        print ('shuffling deck...')
        shuffle(deck)
        
class BlackjackCard(Card):
    # Class Variables 
    pointsdict = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11 } # Blackjack Points
    
    def __init__(self, n):
        self._id = n
        if n > 51:
            raise Exception('Invalid card id. Card ids mustbe between 0 and 51')
    
    def __lt__(self, other):
        return self.rank() < other.rank()
        
    def points(self):
        ''' identifies a card's point value'''
        return BlackjackCard.pointsdict[BlackjackCard.symb(self)]
        
    def hit(hand, deck):
        """ BlackjackCard.hit(hand, deck) to take a hit """
        hand.append(deck.pop(0))
        print("Hand: ", hand)
        print('Current score is: ', points(hand))
        if points(bjh) > 21:
            print ('Busted!, your hand has been discarded')
            for i in range(len(hand)):
                hand.pop()
            
        

# Other Functions    
def new_deck(Card, n=1): 
    """ Creates a deck from CardType(e.g. Card, BlackjackCard) with 'n' decks where n is an optional argument with a default of 1, note. blackjack is typically played with several decks """
    data = []
    for _i in range(n):
        data.append([Card(i) for i in range(51)])
    data = list(chain(*data))
    return data
    
def draw(hand, deck):
    """ Used to draw cards to hand from deck """
    hand.append(deck.pop(0))
    
def points(list):
    sumdata=[]
    for i in range (len(list)):
        sumdata.append(list[i].points())
    return sum(sumdata)
    

# Tests / Play
if __name__ == '__main__':

    #deck = new_deck(Card, 1)
    deck = new_deck(BlackjackCard, 6)
    Card.shuffle(deck)
    h=[]
    n_cards=[6, 2]
    #n_cards=input('How many cards would you like to draw? ')
    
    
    for i in range(int(n_cards[1])):
        draw(h, deck)
    print ('New', type(h[0]), 'Hand:', h)
    print('Current score is: ', points(h))


