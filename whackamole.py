import pygame
import random

# Constants
GRID_WIDTH = 20
GRID_HEIGHT = 16
SQUARE_SIZE = 32
WINDOW_WIDTH = GRID_WIDTH * SQUARE_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * SQUARE_SIZE


def main():
    try:
        pygame.init()

        # Load mole image and initialize window
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (SQUARE_SIZE, SQUARE_SIZE))
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()

        # Set initial mole position in the top-left square
        mole_pos = (0, 0)

        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get mouse click position
                    mouse_x, mouse_y = event.pos
                    clicked_row = mouse_y // SQUARE_SIZE
                    clicked_col = mouse_x // SQUARE_SIZE
                    if (clicked_row, clicked_col) == mole_pos:
                        # Move mole to a new random square in the grid
                        mole_pos = (
                            random.randrange(0, GRID_HEIGHT),
                            random.randrange(0, GRID_WIDTH)
                        )

            # Fill screen background
            screen.fill("light green")

            # Draw grid
            for i in range(GRID_WIDTH + 1):
                pygame.draw.line(screen, "dark green", (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WINDOW_HEIGHT))
            for j in range(GRID_HEIGHT + 1):
                pygame.draw.line(screen, "dark green", (0, j * SQUARE_SIZE), (WINDOW_WIDTH, j * SQUARE_SIZE))

            # Draw mole at its current position
            mole_x, mole_y = mole_pos[1] * SQUARE_SIZE, mole_pos[0] * SQUARE_SIZE
            screen.blit(mole_image, (mole_x, mole_y))

            # Update display
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
