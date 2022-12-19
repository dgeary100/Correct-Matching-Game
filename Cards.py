from enum import Enum
# import pygame and random for the cards
import pygame
import random
# card color class, describes the different types
class Colors(Enum):
  Purple = 0
  Green = 1
  Blue = 2



class Card:
    color = None
    value = None
    image = None
# define
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.image = pygame.image.load('images/' + self.color.name + '-' + str(self.value) + '.png')


class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for color in Colors:
            for value in range(1, 10):
                self.cards.append(Card(color, value))
# calls random
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def length(self):
        return len(self.cards)


class Pile:
    cards = None

    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def see(self):
        if (len(self.cards) > 0):
            return self.cards[-1]
        else:
            return None

    def popAll(self):
        return self.cards

    def clear(self):
        self.cards = []
# test if the cards match
    def isMatch(self):
        if (len(self.cards) > 1):
            return (self.cards[-1].value == self.cards[-2].value)
        return False


class Player:
    hand = None
    flipKey = None
    MatchKey = None
    name = None

    def __init__(self, name, flipKey, MatchKey):
        self.hand = []
        self.flipKey = flipKey
        self.MatchKey = MatchKey
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)
