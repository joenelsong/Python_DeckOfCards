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
        for i in range (n):
            print ('Shuffling ...')
            random.shuffle(self)
    
    def deal(self, n=1):
        data=[]
        data.append((self.pop()) for i in range (n))
        data = list(chain(*data))
        return data
    
    def restore(self, hand):
        print ('Returning', len(hand),'cards back to deck...')
        for i in range(len(hand)):
            self.append(hand.pop())
            
class PinochleDeck(Deck):
    cardList=[7, 8, 9, 10, 11, 12, 20, 21, 22, 23, 24, 25, 33, 34, 35, 36, 37, 38, 46, 47, 48, 49, 50, 51]
    def __init__(self):
        for i in (PinochleDeck.cardList):
            self.append(Card(i))
            self.append(Card(i))
        
p = PinochleDeck()

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