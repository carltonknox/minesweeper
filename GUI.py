import pygame

def init_game(game):
    # Initialize Pygame
    pygame.init()
    global BLACK,WHITE,GRAY,BLUE,RED,SCREEN_HEIGHT,SCREEN_WIDTH,screen,CELL_SIZE,FONT
    # Define the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    BLUE = (0, 0, 255)
    RED = (255,0,0)

    # Set the dimensions of the screen
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the title of the game
    pygame.display.set_caption("Minesweeper")

    # Define the size of each cell
    CELL_SIZE = int(min(SCREEN_WIDTH/game.cols,SCREEN_HEIGHT/game.rows))

    # Define the font for the text
    FONT = pygame.font.Font(None, 32)

# Define the game loop
def run_game(game):
    running = True
    gameover = False
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                i, j = y // CELL_SIZE, x // CELL_SIZE
                if(i < game.rows and j < game.cols and not gameover):
                    if event.button == 1: # left mouse button
                        gameover = game.test(i, j) or not any("?" in c for c in game.gameboard)
                    elif event.button == 3: # right mouse button
                        game.flag(i, j)
        
        for i in range(game.rows):
            for j in range(game.cols):
                x, y = j * CELL_SIZE, i * CELL_SIZE
                cell = game.gameboard[i][j]
                if cell == "?":
                    pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
                elif cell == "x":
                    pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen,RED,(x+CELL_SIZE/4,y+1*CELL_SIZE/5,CELL_SIZE/10,CELL_SIZE*3/4))
                    pygame.draw.polygon(screen,RED,((x+CELL_SIZE/4,y+1*CELL_SIZE/5),(x+CELL_SIZE/4,y+3*CELL_SIZE/5),(x+3*CELL_SIZE/4,y+2*CELL_SIZE/5)))
                elif cell == "o":
                    pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                    pygame.draw.circle(screen, BLACK, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 4)
                else:
                    pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                    text = FONT.render(cell, True, BLACK)
                    text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text, text_rect)

        
        # Update the screen
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
