import pygame
from constants import TILE_SIZE, TILE_MARGIN, GRID_SIZE, TILE_COLORS, BACKGROUND_COLOR, WIDTH, HEIGHT

def draw_board(screen, board, score, FONT, SCORE_FONT):
    screen.fill(BACKGROUND_COLOR)
    score_text = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 10))

    tile_offset = 40
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            value = board[x][y]
            color = TILE_COLORS.get(value, (238, 228, 218))
            pygame.draw.rect(screen, color, (y * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN, x * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + tile_offset, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text_surface = FONT.render(f"{value}", True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(y * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + TILE_SIZE / 2, x * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + tile_offset + TILE_SIZE / 2))
                screen.blit(text_surface, text_rect)
    pygame.display.update()

def game_over_screen(screen, FONT):
    message = "Ещё раз? Y/N"  # буквы будут работать ТОЛЬКО на английском языке.
    text_surface = FONT.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()