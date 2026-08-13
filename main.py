import time
import consts
import Screen
import pygame
import random

state = {
    'player_x' : 0,
    'player_y' : 0,
    'player_state' : 'healthy',
    'game_state' : 'running',
    'is_screen_visible' : True
}

player = {
    'body' : [
        (state['player_y'],state['player_x']), #0,0
        (state['player_y'],state['player_x']+1),#0,1
        state['player_y']
    ]
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


def random_mines(matrix,amount_of_mines):

    while amount_of_mines >0:
        mine_x = random.randrange(1,consts.MATRIX_COLS-1)
        mine_y = random.randrange(0,consts.MATRIX_ROWS)

        while 0 <= mine_x <= 2 and 0 <= mine_y <= 4:
            mine_x = random.randrange(1, consts.MATRIX_COLS - 1)
            mine_y = random.randrange(0, consts.MATRIX_ROWS)

        if 'mine' in (matrix[mine_y][mine_x],matrix[mine_y][mine_x]):
            continue

        matrix[mine_y][mine_x] = 'mine'
        matrix[mine_y][mine_x-1] = 'mine'
        matrix[mine_y][mine_x+1] = 'mine'

        amount_of_mines -= 1

    for row in matrix:
        print(row)

def main():
    pygame.init()
    matrix = create_matrix(consts.MATRIX_ROWS, consts.MATRIX_COLS)
    matrix = random_mines(matrix,consts.AMOUNT_OF_MINES)

    while state['game_state'] == 'running':

        handle_input()

        Screen.draw_game(state)

if __name__ == "__main__":
    main()