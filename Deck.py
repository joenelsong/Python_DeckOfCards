# CIS 211 Spring 2014
# Project 2
# Author: Joseph Nelson
##
from Card import *
import random
from itertools import chain

class Deck(list):
    def __init__(self, n=1):
        for i in range (n):
            for i in range(52):
                self.append(Card(i))

    def shuffle(self, n=1):
        ''' My Custom Shuffle Function '''
        shufDeck=[]
        for i in range (n):
            print ('Shuffling ...')
            for ii in range (len(self)):
                randCard= round(random.random() * len(self)) # Random # between 1 and deck length
                shufDeck.append(self.pop(randCard-1))       # Append random card
        self.extend(shufDeck)

    
    def deal(self, cards=1, hands=1):
        data=[]
        data.append([list() for _i in range (hands)]) # Creating Hands
        
        for i in range (cards):
            for ii in range (hands):
                data[0][ii].append((self.pop()))
        if hands == 1:
            return data[0][0]
        else:
            return data[0]
        #for iii in range (hands):
        #    yield list(data[0][iii])
            
        #data = list(chain(*data))
        
    
    def restore(self, hand):
        if (type(hand) is list):
            print ('Returning', len(hand),'cards back to deck...')
            for i in range(len(hand)):
                self.append(hand.pop())
        else:
            raise Exception('restore only supports list data structures')
    @staticmethod
    def disabledmethods():
        raise Exception('Function not supported')
    
    #def append(self, x): Deck.disabledmethods()
    #def sort(self): Deck.disabledmethods()
    #def reverse(self): Deck.disabledmethods()
    #def __setitem__(self, loc, val): Deck.disabledmethods()

            
class PinochleDeck(Deck):
    cardList=[7, 8, 9, 10, 11, 12, 20, 21, 22, 23, 24, 25, 33, 34, 35, 36, 37, 38, 46, 47, 48, 49, 50, 51]
    def __init__(self):
        for i in (PinochleDeck.cardList):
            self.append(Card(i))
            self.append(Card(i))
            
if __name__ == '__main__':   
    d = PinochleDeck()
    d.shuffle()
    print ('>>> h = d.deal(5,3)')    
    h = d.deal(5,3)
    #print ('>>> d.restore(h)')
    #d.restore(h)

    


## <Decks.pdf Bullet # 1>
# print ('>>> d = Deck()')        
# d = Deck()
# print ('>>> d.shuffle')      
# d.shuffle()
# print ('>>> h = d.deal(5)')    
# h = d.deal(5)
# print ('>>> d.restore(h)')
# d.restore(h)
## </Decks.pdf Bullet # 1>