import pygame
import consts

screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def create_player(player_image):
    player_image=pygame.image.load(player_image)
    sized_player_image = pygame.transform.scale(player_image, (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    player_image_box= pygame.Surface((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT*2),)
    player_image_box.blit(sized_player_image, (0, 0))
    print(player_image_box)



def change_size():
    pass

#הפונקציה הראשית של המשחק על הלוח(הציור של המשחק)
def draw_game():
    pass

