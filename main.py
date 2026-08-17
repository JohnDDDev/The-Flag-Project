import Database
import consts
import Screen
import random
import soldier
import pygame
import time
import sys

state = {     #המצב הרגעי של המשחק
    'player_x' : 0,
    'player_y' : 0,
    'won_game' : False,
    'player_state' : 'healthy',
    'enable_input' : True,
    'game_state' : 'running',
    'is_screen_visible' : True,
    'Timer' : 0,
    'Timer_exit' : 0,
    'flag_x' : consts.MATRIX_COLS-4,
    'flag_y' : consts.MATRIX_ROWS-3,
}

current_game = {}
keys_timer = {}

def create_matrix(rows,cols): # ליצור מטריקס
    matrix = [[ '0' for _ in range(consts.MATRIX_COLS)] for _ in range(consts.MATRIX_ROWS) ]
    return matrix

def random_mines(matrix,amount_of_mines): # ליצור את הפצצות בצורה רנדומלית
    mines_locations = []
    while amount_of_mines >0:
        mine_x = random.randrange(1,consts.MATRIX_COLS-1)
        mine_y = random.randrange(0,consts.MATRIX_ROWS)

        while ((0 <= mine_x <= 2 and 0 <= mine_y <= 4) or
               (mine_x >= consts.MATRIX_COLS - 4 and mine_y >= consts.MATRIX_ROWS - 3)): # בדיקה אם המיקום של הפצצה נמצא במיקום שהשקן מתחיל בו ומבטל אותו

            mine_x = random.randrange(1, consts.MATRIX_COLS - 1)
            mine_y = random.randrange(0, consts.MATRIX_ROWS)

        if 'mine' in (matrix[mine_y][mine_x-1],matrix[mine_y][mine_x+1],matrix[mine_y][mine_x]):# בודק שהמקום שהפצצות לא אחד על השני
            continue

        matrix[mine_y][mine_x] = 'mine'
        matrix[mine_y][mine_x-1] = 'mine'
        matrix[mine_y][mine_x+1] = 'mine'
        mines_locations.append((mine_x-1,mine_y))
        amount_of_mines -= 1

    return matrix ,mines_locations

def append_player(player,matrix): # בודק את המיקום של גוף השחקן ורגליו ומכניס אותם למטריקס
    for location in player['body']:
        if matrix[location[0]][location[1]] == 'flag':
            state['won_game'] = True

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

def clean_player_location(player,matrix): #מנקה את מיקום השחקן במיקום הקודם שהיה
    for location in player['body']:
        matrix[location[0]][location[1]] = '0'

    for location in player['legs']:
        matrix[location[0]][location[1]] = '0'

    return matrix

def add_flag(matrix):
    for row in range(consts.MATRIX_ROWS-3,consts.MATRIX_ROWS):
        for col in range(consts.MATRIX_COLS-4,consts.MATRIX_COLS):
            matrix[row][col] = 'flag'
    return matrix

def main():
    global current_game,state
    pygame.init()

    matrix  = create_matrix(consts.MATRIX_ROWS, consts.MATRIX_COLS)
    matrix , mines_locations = random_mines(matrix,consts.AMOUNT_OF_MINES)
    bushes_locations = Screen.random_bushes(consts.AMOUNT_OF_BUSHES)

    while state['game_state'] == 'running':

        player = soldier.get_player_location(state)
        matrix = clean_player_location(player, matrix)
        matrix = add_flag(matrix)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state['game_state'] = 'exit'

            elif event.type == pygame.KEYDOWN:

                soldier.handle_input(state,event.key)

                if pygame.K_1 <= event.key <= pygame.K_9:
                    keys_timer[event.key] = time.time()

            elif event.type == pygame.KEYUP:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    slot_num= event.key - pygame.K_0
                    if event.key in keys_timer:
                        press_time = (time.time() - keys_timer[event.key])
                        del keys_timer[event.key]

                        if press_time <= 1.0:
                            print(f"short press {press_time}")
                            Database.save_game(slot_num, current_game)
                        else:
                            print(f"long press {press_time}")
                            load_data = Database.load_game(slot_num)
                            if load_data:
                                state = load_data['state']
                                matrix = load_data['matrix']
                                bushes_locations = load_data['bushes_locations']
                                mines_locations = load_data['mines_locations']
                                print("game loaded successfully")


        if state['is_screen_visible'] == False and time.time() - state['Timer']  > 1:
            state['is_screen_visible'] = True
            state['player_state'] = 'healthy'

        if state['Timer_exit'] and time.time() - state['Timer_exit'] > 3:
            quit()

        player = soldier.get_player_location(state)
        matrix = append_player(player,matrix)

        current_game = {
            'state': state,
            'matrix': matrix,
            'bushes_locations': bushes_locations,
            'mines_locations': mines_locations
        }

        Screen.draw_game(state,mines_locations)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()