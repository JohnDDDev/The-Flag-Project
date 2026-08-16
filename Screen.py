import pygame
import consts

player = pygame.image.load(consts.PLAYER_IMAGE)
flag = pygame.image.load(consts.FLAG_IMAGE)
clock = pygame.time.Clock()

def create_screen():
    global screen
    pygame.init()
    screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("the game ")
    return screen

def draw_background(screen,color):
    screen.fill(color)

def draw_grid(screen):
    draw_background(screen,consts.GRID_COLOR)
    for x in range(0, consts.WINDOW_WIDTH, consts.TILE_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.TILE_SIZE):
            rect = pygame.Rect(x, y, consts.TILE_SIZE, consts.TILE_SIZE)
            pygame.draw.rect(screen, consts.LINES_COLOR, rect, 1)

def player_surface():
    width = 2 * consts.TILE_SIZE
    height = 4 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(player, (width, height))
    return sized_image

def draw_player(x,y):
    player_surface_place = player_surface()
    pixel_x= x * consts.TILE_SIZE
    pixel_y= y * consts.TILE_SIZE
    screen.blit(player_surface_place, (pixel_x, pixel_y))

def flag_surface():
    width= 4 * consts.TILE_SIZE
    height= 3 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(flag, (width, height))
    return sized_image

def draw_flag(x1,y1):
    flag_surface_place = flag_surface()
    pixel_1 = x1 * consts.TILE_SIZE
    pixel_2 = y1 * consts.TILE_SIZE
    screen.blit(flag_surface_place,(pixel_1, pixel_2))

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont('arial', font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_lost_massage():
    draw_message('You Lost',100,'red',(consts.WINDOW_WIDTH/3,consts.WINDOW_HEIGHT/3))

def draw_win_massage():
    draw_message('you Won',100,'green',(consts.WINDOW_WIDTH/3,consts.WINDOW_HEIGHT/3))

def wellcome_massage():
    draw_message('WellCome To The Flag Game!\nHave Fun ', 15, 'white', (20,20))

screen = create_screen()

def draw_game(state):
    global player

    if state['won_game']:
        draw_win_massage()

    draw_background(screen,consts.BACKGROUND_COLOR)
    if not state['is_screen_visible']:
        draw_grid(screen)

    draw_flag(state['flag_x'],state['flag_y'])

    if state['player_state'] == 'injured':
        player = pygame.image.load(consts.INJURED_PLAYER_IMAGE)
        draw_lost_massage()
    elif state['player_state'] == 'soldier_nigth':
        player = pygame.image.load(consts.PLAYER_NIGTH)
    else:
        player = pygame.image.load(consts.PLAYER_IMAGE)

    draw_player(state['player_x'],state['player_y'])
    wellcome_massage()

    pygame.display.flip()

    clock.tick(60)

