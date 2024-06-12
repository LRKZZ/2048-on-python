import pygame
from display import draw_board, game_over_screen
from game_functions import init_game, move, game_over
from constants import WIDTH, HEIGHT

pygame.init()
FONT = pygame.font.SysFont("comicsansms", 28)
SCORE_FONT = pygame.font.SysFont("comicsansms", 24)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    board = init_game()
    score = 0
    running = True

    while running:
        draw_board(screen, board, score, FONT, SCORE_FONT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    score = move(board, 'left', score)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    score = move(board, 'right', score)
                elif event.key in (pygame.K_UP, pygame.K_w):
                    score = move(board, 'up', score)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    score = move(board, 'down', score)

        if game_over(board):
            if not game_over_screen(screen, FONT):
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
