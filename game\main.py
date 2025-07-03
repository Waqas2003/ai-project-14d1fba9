import pygame
from .views import GameView

def main():
    pygame.init()
    game = GameView()
    game.run()

if __name__ == '__main__':
    main()