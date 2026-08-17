import sys
import pygame
import consts
import time
import Database
import main

keys_timer = {}

def get_player_location(state): #מיקום השחקן
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

def handle_input(state): #בדיקת מקשים
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return

        elif event.type == pygame.KEYDOWN and state['enable_input']:

            if not state['is_screen_visible']:
                continue

            if event.key == pygame.K_RETURN:
                state['Timer'] = time.time()
                state['is_screen_visible'] = False
                state['player_state'] = 'soldier_nigth'
                continue

            if event.key == pygame.K_LEFT:
                if state['player_x'] > 0:
                    state['player_x'] -= 1

            elif event.key == pygame.K_RIGHT:
                if state['player_x'] < consts.MATRIX_COLS - 2:
                    state['player_x'] += 1

            elif event.key == pygame.K_UP:
                if state['player_y'] > 0:
                    state['player_y'] -= 1

            elif event.key == pygame.K_DOWN:
                if state['player_y']  < consts.MATRIX_ROWS - 4:
                    state['player_y'] += 1

            elif pygame.K_1 <= event.key <= pygame.K_9:
                slot = event.key - pygame.K_0
                keys_timer[event.key] = time.time()

            elif event.key == pygame.KEYUP:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    slot_num = event.key - pygame.K_0

                    if event.key in keys_timer:
                        press_time=(time.time() - keys_timer[event.key])
                        del keys_timer[event.key]

                        if press_time<=1.0:
                            print(f"short press {press_time}")
                            Database.save_game(slot_num,main.current_game)

                        else:
                            print(f"long press {press_time}")
                            load_data = Database.load_game(slot_num)
                            if load_data:
                                print(f"data to aply :{load_data}")