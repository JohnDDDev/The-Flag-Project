import pygame
import consts

player = pygame.image.load(consts.PLAYER_IMAGE)
flag = pygame.image.load(consts.FLAG_IMAGE)
clock = pygame.time.Clock()

def create_screen(): # יוצרים את המסך
    global screen
    pygame.init()
    screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("the game ")
    return screen

def draw_background(screen,color):# לצבוע את הרקע
    screen.fill(color)

def draw_grid(screen): #צובע את הרקע בשחוק , עובר על כל הריבועים ומצייר ריבועים בגודל של 1
    draw_background(screen,consts.GRID_COLOR)
    for x in range(0, consts.WINDOW_WIDTH, consts.TILE_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.TILE_SIZE):
            rect = pygame.Rect(x, y, consts.TILE_SIZE, consts.TILE_SIZE)
            pygame.draw.rect(screen, consts.LINES_COLOR, rect, 1)

def player_surface(): # ליצור את גודל השחקן
    width = 2 * consts.TILE_SIZE
    height = 3 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(player, (width, height))
    return sized_image

def draw_player(x,y): # לצייר את השחקן על המסך
    player_surface_place = player_surface()
    pixel_x= x * consts.TILE_SIZE
    pixel_y= y * consts.TILE_SIZE
    screen.blit(player_surface_place, (pixel_x, pixel_y))

def flag_surface(): #להגדיר גודל של הדגל
    width= 4 * consts.TILE_SIZE
    height= 3 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(flag, (width, height))
    return sized_image

def draw_flag(x1,y1): #לצייר את הדגל על המסך
    flag_surface_place = flag_surface()
    pixel_1 = x1 * consts.TILE_SIZE
    pixel_2 = y1 * consts.TILE_SIZE
    screen.blit(flag_surface_place,(pixel_1, pixel_2))

def draw_message(message, font_size, color, location): # לצייר את כל ההודעות המוקדמות
    font = pygame.font.SysFont('arial', font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_lost_massage(): #הודעת הפסד
    draw_message('You Lost',100,'red',(consts.WINDOW_WIDTH/3,consts.WINDOW_HEIGHT/3))

def draw_win_massage():
    pass

def wellcome_massage():
    draw_message('wellcome to the game', 10 , 'white', (10,10))

screen = create_screen() #ליצור מסך

def draw_game(state):# לצבוע ולנהל את המשחק
    global player
    draw_background(screen,consts.BACKGROUND_COLOR)
    if not state['is_screen_visible']:
        draw_grid(screen)

    draw_player(state['player_x'],state['player_y'])
    draw_flag(state['flag_x'],state['flag_y'])

    if state['player_state'] == 'injured':
        player = pygame.image.load(consts.INJURED_PLAYER_IMAGE)
        draw_lost_massage()
    elif state['player_state'] == 'soldier_nigth':
        player = pygame.image.load(consts.PLAYER_NIGTH)
    else:
        player = pygame.image.load(consts.PLAYER_IMAGE)

    pygame.display.flip()

    clock.tick(60)

