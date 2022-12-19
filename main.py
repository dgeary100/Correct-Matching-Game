import pygame
# import files
from Cards import *
from Play import *

# init
pygame.init()
bounds = (1000,700)
screen = pygame.display.set_mode(bounds)
# caption
pygame.display.set_caption("WildCards")
# The back of the cards
Back = pygame.image.load('Images/BlueCardBackground.png')
BackSize = (200,300)
Back = pygame.transform.scale(Back, BackSize)
# Engine
playEngine = MatchEngine()
# screen/text
def renderGame(screen):
    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial",40, True)
    screen.blit(Back, (100,200))
    screen.blit(Back, (700,200))

    text = font.render(str(len(playEngine.player1.hand)) + "cards",True, (255,255,255))
    screen.blit(text, (100,500))
    text = font.render(str(len(playEngine.player2.hand)) +'cards', True, (255,255,255))
    screen.blit(text, (700,500))

    top = playEngine.pile.see()
    if (top != None):
        screen.blit(top.image, (400, 200))
    if playEngine.state == GameState.PLAYING:
        text = font.render(playEngine.currentPlayer.name + " to flip", True, (255, 255, 255))
        screen.blit(text, (20, 50))

    if playEngine.state == GameState.MATCHING:
        result = playEngine.result
        if result["isMatch"] == True:
            message = "Winning by " + result["winner"].name
        else:
            message = "False Win by " + result["MatchCaller"].name + ". " + result["winner"].name + " wins!"
        text = font.render(message, True, (255, 255, 255))
        screen.blit(text, (20, 50))

    if playEngine.state == GameState.ENDED:
        result = playEngine.result
        message = "Game Over! " + result["winner"].name + " wins!"
        text = font.render(message, True, (255, 255, 255))
        screen.blit(text, (20, 50))

# Game Loop
run = True
while run:
    key = None;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # the key references to play the game
        if event.type == pygame.KEYDOWN:
            key = event.key

    playEngine.play(key)
    renderGame(screen)
    pygame.display.update()

    if playEngine.state == GameState.MATCHING:
        pygame.time.delay(3000)
        playEngine.state = GameState.PLAYING

