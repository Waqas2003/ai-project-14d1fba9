import pygame
import sys
from .models import Snake, Food
from .constants import WIDTH, HEIGHT, BLOCK_SIZE, SPEED

class GameView:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.food.generate()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Game')

    def draw(self):
        self.screen.fill((0, 0, 0))
        for pos in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                    self.snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                    self.snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                    self.snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                    self.snake.direction = 'RIGHT'

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.snake.move()
            if self.snake.eat(self.food.position):
                self.food.generate()
            self.draw()
            clock.tick(SPEED)