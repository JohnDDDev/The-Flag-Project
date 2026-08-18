import time
import pygame
import consts
import Screen

dinosaur = pygame.image.load(consts.Dinosaur)

def dinosaur_surface():
    width = 2 * consts.TILE_SIZE
    height = 4 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(dinosaur, (width, height))
    return sized_image

def draw_dinosaur(x, y):
    dinosaur_surface_place = dinosaur_surface()
    pixel_x = x * consts.TILE_SIZE
    pixel_y = y * consts.TILE_SIZE
    Screen.screen.blit(dinosaur_surface_place, (pixel_x, pixel_y))


def find_empty_row(matrix):
    for i in range(consts.MATRIX_ROWS-1,1,-1):
        if 'mine' in matrix[i] or 'pit' in matrix[i]:
            continue
        return [47,i]
    else:
        print("no Empty Row on board")
        return [47,2]

def walk_dinosaur(matrix,x,y,is_right,state):
    if is_right:
        if 'legs' in (matrix[y][x], matrix[y][x + 1], matrix[y][x + 2]):
            print('Enemy')
            state['player_state'] = 'injured'
            Screen.draw_lost_massage()
            state['enable_input'] = False
            state['Timer_exit'] = time.time()

        matrix[y][x] = 'mine'
        matrix[y][x + 1] = 'mine'
        matrix[y][x + 2] = 'mine'

    else:
        if 'legs' in (matrix[y][x], matrix[y][x + 1], matrix[y][x + 2]):
            print('Enemy')
            state['player_state'] = 'injured'
            Screen.draw_lost_massage()
            state['enable_input'] = False
            state['Timer_exit'] = time.time()

        matrix[y][x] = 'mine'
        matrix[y][x - 1] = 'mine'
        matrix[y][x - 2] = 'mine'