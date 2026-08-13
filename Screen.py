import pygame
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
    width = 2 * consts.TILE_SIZE
    height = 3 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(consts.PLAYER_IMAGE, (width, height))
    return sized_image

def draw_player(x,y):
    player_surface_place = player_surface()
    pixel_x= x * consts.TILE_SIZE
    pixel_y= y * consts.TILE_SIZE
    screen.blit(player_surface_place, (pixel_x, pixel_y))

# def create_player(player_image):
#     player_image=pygame.image.load(player_image)
#     sized_player_image = pygame.transform.scale(player_image, (2,6))
#     player_image_box= pygame.Surface((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT*2),)
#     player_image_box.blit(sized_player_image, (0, 0))
#     print(player_image_box)
#     return player_image_box

#הפונקציה הראשית של המשחק על הלוח(הציור של המשחק)

def draw_game(state):
    screen = create_screen()
    if state['is_screen_visible']:
        draw_background(screen)
    else:
        draw_grid(screen)

    draw_player(state['player_x'],state['player_y'])
    pygame.display.flip()
    clock.tick(10)