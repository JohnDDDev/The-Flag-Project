import consts
import Screen
import pygame
import random
import time

state = {
    'player_x' : 0,
    'player_y' : 0,
    'player_state' : 'healthy',
    'game_state' : 'running',
    'is_screen_visible' : True,
    'flag_x' : consts.MATRIX_COLS-4,
    'flag_y' : consts.MATRIX_ROWS-3,
}

def get_player_location(state):
    player = {
        'body': [
            (state['player_y'], state['player_x']),
            (state['player_y'], state['player_x'] + 1),
            (state['player_y'] + 1, state['player_x']),
            (state['player_y'] + 1, state['player_x'] + 1),
            (state['player_y'] + 2, state['player_x']),
            (state['player_y'] + 2, state['player_x'] + 1),
        ],
        'legs': [
            (state['player_y'] + 3, state['player_x']),
            (state['player_y'] + 3, state['player_x']+1),
        ]
    }

    return player


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
                state['player_y'] -= 1
            elif event.key == pygame.K_DOWN:
                state['player_y'] += 1

            # כוח לעשות את הלוח שקוף ולראות את המוקשים
            elif event.key == pygame.K_RETURN:
                state['is_screen_visible'] = False

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
            print("You Lost")

        matrix[location[0]][location[1]] = 'legs'

    return matrix

def clean_player_location(player,matrix):
    for location in player['body']:
        matrix[location[0]][location[1]] = '0'

    for location in player['legs']:
        matrix[location[0]][location[1]] = '0'

    return matrix


def main():
    pygame.init()

    matrix = create_matrix(consts.MATRIX_ROWS, consts.MATRIX_COLS)
    matrix = random_mines(matrix,consts.AMOUNT_OF_MINES)

    while state['game_state'] == 'running':

        player = get_player_location(state)
        matrix = clean_player_location(player, matrix)

        handle_input()

        player = get_player_location(state)
        matrix = append_player(player,matrix)

        Screen.draw_game(state)

        if state['is_screen_visible'] == False:
            time.sleep(1)
            state['is_screen_visible'] =True


if __name__ == "__main__":
    main()