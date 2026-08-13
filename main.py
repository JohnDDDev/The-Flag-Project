import pygame
import consts
import Screen
import pygame

state = {
    'player_x' : 0,
    'player_y' : 0,
    'player_state' : 'healthy',
    'game_state' : 'running'
}

def create_matrix(rows,cols):
    matrix = [[ '0' for _ in range(consts.MATRIX_COLS)] for _ in range(consts.MATRIX_ROWS) ]
    return matrix

def player_movement(direction):
    pass

def main():
    matrix = create_matrix(consts.MATRIX_ROWS, consts.MATRIX_COLS)

    while state['game_state'] == 'running':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        Screen.draw_game(state)

if __name__ == "__main__":
    main()