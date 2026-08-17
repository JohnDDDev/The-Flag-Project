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

