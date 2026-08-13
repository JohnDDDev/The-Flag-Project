import time
import consts
import Screen
import pygame

state = {
    'player_x' : 0,
    'player_y' : 0,
    'player_state' : 'healthy',
    'game_state' : 'running',
    'is_screen_visible' : True
}

def create_matrix(rows,cols):
    matrix = [[ '0' for _ in range(consts.MATRIX_COLS)] for _ in range(consts.MATRIX_ROWS) ]
    return matrix

def handle_input():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state['player_x'] -= 1
            elif event.key == pygame.K_RIGHT:
                state['player_x'] += 1
            elif event.key == pygame.K_UP:
                state['player_y'] += 1
            elif event.key == pygame.K_DOWN:
                state['player_y'] -= 1

            # כוח לעשות את הלוח שקוף ולראות את המוקשים
            elif event.key == pygame.K_RETURN:
                state['is_screen_visible'] = False
                time.sleep(1)


def random_mines(matrix,amount):
    pass

def main():

    matrix = create_matrix(consts.MATRIX_ROWS, consts.MATRIX_COLS)
    matrix = random_mines(matrix,consts.AMOUNT_OF_MINES)
    while state['game_state'] == 'running':

        handle_input()

        Screen.draw_game(state)

if __name__ == "__main__":
    main()