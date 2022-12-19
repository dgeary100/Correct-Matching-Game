from enum import Enum
import pygame
# import file
from Cards import *
#game play class
class GameState(Enum):
  PLAYING = 0
  MATCHING = 1
  ENDED = 2

# variables
class MatchEngine:
    deck = None
    player1 = None
    player2 = None
    pile = None
    state = None
    currentPlayer = None
    result = None

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Player 1", pygame.K_q, pygame.K_w)
        self.player2 = Player("Player 2", pygame.K_o, pygame.K_p)
        self.pile = Pile()
        self.deal()
        self.currentPlayer = self.player1
        self.state = GameState.PLAYING
        # split up the deck and draw
    def deal(self):
        half = self.deck.length() // 2
        for i in range(0, half):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)
            # two players, switch code
    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
    def winRound(self, player):
        self.state = GameState.MATCHING
        player.hand.extend(self.pile.popAll())
        self.pile.clear()


    def play(self, key):
        if key == None:
            return

        if self.state == GameState.ENDED:
            return

        if key == self.currentPlayer.flipKey:
            self.pile.add(self.currentPlayer.play())
            self.switchPlayer()
        MatchCaller = None
        nonMatchCaller = None
        isMatch = self.pile.isMatch()

        if (key == self.player1.MatchKey):
            MatchCaller = self.player1
            nonMatchCaller = self.player2
        elif (key == self.player2.MatchKey):
            MatchCaller = self.player2
            nonMatchCaller = self.player1
        if isMatch and MatchCaller:
            self.winRound(MatchCaller)
            self.result = {
                "winner": MatchCaller,
                "isMatch": True,
                "MatchCaller": MatchCaller
            }
            self.winRound(MatchCaller)
        elif not isMatch and MatchCaller:
            self.result = {
                "winner": nonMatchCaller,
                "isMatch": False,
                "MatchCaller": MatchCaller
            }
            self.winRound(nonMatchCaller)
        if len(self.player1.hand) == 0:
            self.result = {
                "winner": self.player2,
            }
            self.state = GameState.ENDED
        elif len(self.player2.hand) == 0:
            self.result = {
                "winner": self.player1,
            }
            self.state = GameState.ENDED