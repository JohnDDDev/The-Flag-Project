import pygame
import consts

def create_screen():
    global screen
    pygame.init()
    screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("the game ")
    return screen

def drew_background(screen):
    screen.fill(consts.BACKGROUND_COLOR)

def drew_grid(screen):
    for row in range(consts.WINDOW_HEIGHT):
        for col in range(consts.WINDOW_WIDTH):
            x = col * consts.TILE_SIZE
            y = row * consts.TILE_SIZE
            rect = pygame.Rect(x, y, consts.TILE_SIZE, consts.TILE_SIZE)
            pygame.draw.rect(screen, consts.BACKGROUND_COLOR, rect)


# def create_player(player_image):
#     player_image=pygame.image.load(player_image)
#     sized_player_image = pygame.transform.scale(player_image, (2,6))
#     player_image_box= pygame.Surface((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT*2),)
#     player_image_box.blit(sized_player_image, (0, 0))
#     print(player_image_box)
#     return player_image_box



def change_size():
    pass

# #הפונקציה הראשית של המשחק על הלוח(הציור של המשחק)
# def draw_game(state):
#     create_player(consts.PLAYER_IMAGE)
#     pygame.display.flip()
