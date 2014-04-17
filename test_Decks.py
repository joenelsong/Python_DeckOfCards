# Unit tests for Deck classes
#
# John Conery
# CIS 211 Project 3
# Spring 2014
#

import unittest

from Deck import *

class DeckTest(unittest.TestCase):
        
    def test_04_deck(self):
        d = Deck()
        self.assertEqual(52, len(d), "deck doesn't have 52 cards")
        suits = dict.fromkeys(range(4),0)
        ranks = dict.fromkeys(range(13),0)
        for x in d:
            suits[x.suit()] += 1
            ranks[x.rank()] += 1
        self.assertEqual(list(suits.values()), [13]*4, "didn't find 13 cards in each suit")
        self.assertEqual(list(ranks.values()), [4]*13, "didn't find 4 of each kind of card")
        
    def test_05_shuffle(self):
        d1 = Deck()
        d2 = Deck()
        d1.shuffle()
        self.assertFalse(same_cards(d1,d2), "deck wasn't shuffled")
        d1.sort()
        self.assertTrue(same_cards(d1,d2), "deck wasn't sorted")
        
    def test_06_hands(self):
        d = Deck()
        h = d.deal(5)
        self.assertEqual(5, len(h), "hand doesn't have 5 cards")
        self.assertEqual(47, len(d), "hand wasn't removed from deck")
        d.restore(h)
        self.assertEqual(52, len(d), "had wasn't put back in deck")
        d.sort()
        self.assertTrue(same_cards(d, Deck()), "restored deck incomplete")

    def test_07_pinochle(self):
        d = PinochleDeck()
        suits = dict.fromkeys(range(4),0)
        ranks = dict.fromkeys(range(7,13),0)
        for x in d:
            suits[x.suit()] += 1
            ranks[x.rank()] += 1
        self.assertEqual([12]*4, list(suits.values()), "didn't find 12 cards in each suit")
        self.assertEqual([8]*6, list(ranks.values()), "didn't find 8 of each kind of card")
        

def same_cards(d1,d2):
    if len(d1) != len(d2):
        return False
    for i in range(len(d1)):
        if d1[i].rank() != d2[i].rank() or d1[i].suit() != d2[i].suit():
            return False
    return True
