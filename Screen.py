import pygame
from pygame.gfxdraw import pixel

import consts

consts.PLAYER_IMAGE = pygame.image.load(consts.PLAYER_IMAGE)
clock = pygame.time.Clock()

def create_screen():
    global screen
    pygame.init()
    screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("the game ")
    return screen

def draw_background(screen):
    screen.fill(consts.BACKGROUND_COLOR)

def draw_grid(screen):
    for row in range(consts.WINDOW_HEIGHT):
        for col in range(consts.WINDOW_WIDTH):
            x = col * consts.TILE_SIZE
            y = row * consts.TILE_SIZE
            rect = pygame.Rect(x, y, consts.TILE_SIZE, consts.TILE_SIZE)
            pygame.draw.rect(screen, consts.BACKGROUND_COLOR, rect)

def player_surface():
    player = pygame.image.load('pictures/bin/soldier.png')
    width = 2 * consts.TILE_SIZE
    height = 3 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(player, (width, height))
    return sized_image

def draw_player(x,y):
    player_surface_place = player_surface()
    pixel_x= x * consts.TILE_SIZE-1
    pixel_y= y * consts.TILE_SIZE-1
    screen.blit(player_surface_place, (pixel_x, pixel_y))

def flag_surface():
    flag = pygame.image.load('pictures/bin/flag.png')
    width= 4 * consts.TILE_SIZE
    height= 3 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(flag, (width, height))
    return sized_image

def draw_flag(x1,y1):
    flag_surface_place = flag_surface()
    pixel_1 = x1 * consts.TILE_SIZE
    pixel_2 = y1 * consts.TILE_SIZE
    screen.blit(flag_surface_place,(pixel_1, pixel_2))

# def create_player(player_image):
#     player_image=pygame.image.load(player_image)
#     sized_player_image = pygame.transform.scale(player_image, (2,6))
#     player_image_box= pygame.Surface((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT*2),)
#     player_image_box.blit(sized_player_image, (0, 0))
#     print(player_image_box)
#     return player_image_box

#הפונקציה הראשית של המשחק על הלוח(הציור של המשחק)

screen = create_screen()

def draw_game(state):
    if state['is_screen_visible']:
        draw_background(screen)
    else:
        draw_grid(screen)

    draw_player(state['player_x'],state['player_y'])
    draw_flag(state['flag_x'],state['flag_y'])
    pygame.display.flip()
    clock.tick(60)