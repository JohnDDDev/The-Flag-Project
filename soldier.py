# import sys
import pygame
import consts
import time



# import Database
# import main
# from Database import save_game, load_game
# from main import current_game


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

            elif event.key == pygame.K_DOWN :
                if state['player_y']  < consts.MATRIX_ROWS - 4:
                    state['player_y'] += 1

