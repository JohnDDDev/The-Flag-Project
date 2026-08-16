import consts
import Screen
import pygame
import random
import time
import soldier

state = {
    'player_x' : 0,
    'player_y' : 0,
    'player_state' : 'healthy',
    'enable_input' : True,
    'game_state' : 'running',
    'is_screen_visible' : True,
    'Timer' : 0,
    'Timer_exit' : 0,
    'flag_x' : consts.MATRIX_COLS-4,
    'flag_y' : consts.MATRIX_ROWS-3,
}

def create_matrix(rows,cols):
    matrix = [[ '0' for _ in range(consts.MATRIX_COLS)] for _ in range(consts.MATRIX_ROWS) ]
    return matrix

def random_mines(matrix,amount_of_mines):
    while amount_of_mines >0:
        mine_x = random.randrange(1,consts.MATRIX_COLS-1)
        mine_y = random.randrange(0,consts.MATRIX_ROWS)

        while 0 <= mine_x <= 2 and 0 <= mine_y <= 4:
            mine_x = random.randrange(1, consts.MATRIX_COLS - 1)
            mine_y = random.randrange(0, consts.MATRIX_ROWS)

        if 'mine' in (matrix[mine_y][mine_x-1],matrix[mine_y][mine_x+1],matrix[mine_y][mine_x]):
            continue

        matrix[mine_y][mine_x] = 'mine'
        matrix[mine_y][mine_x-1] = 'mine'
        matrix[mine_y][mine_x+1] = 'mine'

        amount_of_mines -= 1

    return matrix

def append_player(player,matrix):
    for location in player['body']:
        if matrix[location[0]][location[1]] == 'flag':
            print("You Won")

        matrix[location[0]][location[1]] = 'body'

    for location in player['legs']:
        if matrix[location[0]][location[1]] == 'mine':
            print('mine')
            state['player_state'] = 'injured'
            Screen.draw_lost_massage()
            state['enable_input'] = False
            state['Timer_exit'] = time.time()

        matrix[location[0]][location[1]] = 'legs'

    return matrix

def clean_player_location(player,matrix):
    for location in player['body']:
        matrix[location[0]][location[1]] = '0'

    for location in player['legs']:
        matrix[location[0]][location[1]] = '0'

    return matrix

def add_flag():
    pass

def main():
    pygame.init()
    matrix = create_matrix(consts.MATRIX_ROWS, consts.MATRIX_COLS)
    matrix = random_mines(matrix,consts.AMOUNT_OF_MINES)

    while state['game_state'] == 'running':

        player = soldier.get_player_location(state)
        matrix = clean_player_location(player, matrix)

        soldier.handle_input(state)

        if state['is_screen_visible'] == False and time.time() - state['Timer']  > 1:
            state['is_screen_visible'] = True
            state['player_state'] = 'healthy'

        if state['Timer_exit'] and time.time() - state['Timer_exit'] > 3:
            quit()

        player = soldier.get_player_location(state)
        matrix = append_player(player,matrix)

        Screen.draw_game(state)

if __name__ == "__main__":
    main()