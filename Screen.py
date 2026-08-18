import time
import pygame
import consts
import random
# קורא לכל התמונות שאנחנו מתשמשים בהם
player = pygame.image.load(consts.PLAYER_IMAGE)
flag = pygame.image.load(consts.FLAG_IMAGE)
bush= pygame.image.load(consts.GRASS_IMAGE)
mine=pygame.image.load(consts.MINE_IMAGE)
pit = pygame.image.load(consts.PIT_IMAGE)
dinosaur = pygame.image.load(consts.Dinosaur)
#לספור את זמן הריצה של הקוד
clock = pygame.time.Clock()

def create_screen(): #יוצר את המסך
    global screen
    pygame.init() # הפעלה של המשחק
    screen= pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))# יוצרת מסך גרפי
    pygame.display.set_caption("the flag game ") # כותרת החלון
    return screen

def draw_background(screen,color):
    screen.fill(color)

def draw_grid(screen,mines_locations,pits_locations):#לצייר את המסך השחור עם המשבצות , המוקשים והחורים שחורים
    draw_background(screen,consts.GRID_COLOR)
    for x in range(0, consts.WINDOW_WIDTH, consts.TILE_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.TILE_SIZE):
            rect = pygame.Rect(x, y, consts.TILE_SIZE, consts.TILE_SIZE) # ליצור ריבוע
            pygame.draw.rect(screen, consts.LINES_COLOR, rect, 1) # איפה הוא מצויר, מה הצבע של הקוים , מה העובי של העט ואיזה צורה מצוירת
    for j in mines_locations:
        draw_mine(j[0], j[1])

    for j in pits_locations:
        draw_pit(j[0],j[1])

def random_bushes(amount_of_bushes): # רשימה של שיחים רנדומלים
    bushes=[]
    while amount_of_bushes > 0:
        bush_x = random.randrange(1, consts.MATRIX_COLS-2)
        bush_y = random.randrange(0, consts.MATRIX_ROWS-2)
        while ((0 <= bush_x <= 2 and 0 <= bush_y<= 4) or
               (bush_x>= consts.MATRIX_COLS - 4 and bush_y >= consts.MATRIX_ROWS - 3)): # שלא יחרוג מגבולות המטריצה, ושלא יהיה על השחקן
            bush_x = random.randrange(1, consts.MATRIX_COLS - 1)
            bush_y = random.randrange(0, consts.MATRIX_ROWS)
        bushes.append((bush_x, bush_y))
        amount_of_bushes -=1
    return bushes

def bush_surface():
    width = 2 * consts.TILE_SIZE
    height = 2 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(bush, (width, height)) # שינוי התמונה לגודל מסוים לפי הביקוש
    return sized_image

def drew_bush(x,y):
    bush_surface_place = bush_surface()
    pixel_x = x * consts.TILE_SIZE
    pixel_y = y * consts.TILE_SIZE
    screen.blit(bush_surface_place, (pixel_x, pixel_y)) # להתאים את התמונה לפי הפיקסלים שיש

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
    text_img = font.render(message, True, color) # להפוך את הטקסט לתמונה
    screen.blit(text_img, location)


def dinosaur_surface():
    width = 3 * consts.TILE_SIZE
    height = 4 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(dinosaur, (width, height))
    return sized_image

def draw_dinosaur(x, y):
    dinosaur_surface_place = dinosaur_surface()
    pixel_x = x * consts.TILE_SIZE
    pixel_y = y * consts.TILE_SIZE
    screen.blit(dinosaur_surface_place, (pixel_x, pixel_y))

def draw_lost_massage():
    draw_message('You Lost!',100,'red',(consts.WINDOW_WIDTH/3,consts.WINDOW_HEIGHT/3))

def draw_win_massage():
    draw_message('You won!',100,'green',(consts.WINDOW_WIDTH/3,consts.WINDOW_HEIGHT/3))

def wellcome_massage():
    draw_message('Wellcome To The Flag Game!\nHave Fun ', 15, 'white', (20,20))

screen = create_screen()
bushes_locations = random_bushes(consts.AMOUNT_OF_BUSHES)
start_time = time.time() # הזמן הנוכחי בו מתחילים

def pit_surface():
    width = 3 * consts.TILE_SIZE
    height = 1 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(pit, (width, height))
    return sized_image

def draw_pit(x, y):
    mine_surface_place = pit_surface()
    pixel_x = x * consts.TILE_SIZE
    pixel_y = y * consts.TILE_SIZE
    screen.blit(mine_surface_place, (pixel_x, pixel_y))

def mine_surface():
    width = 3 * consts.TILE_SIZE
    height = 1 * consts.TILE_SIZE
    sized_image = pygame.transform.scale(mine, (width, height))
    return sized_image

def draw_mine(x, y):
    mine_surface_place = mine_surface()
    pixel_x = x * consts.TILE_SIZE
    pixel_y = y * consts.TILE_SIZE
    screen.blit(mine_surface_place, (pixel_x, pixel_y))

def draw_game(state,mines_locations,pits_locations,dinosaur_location,bushes=bushes_locations):
    global player
    draw_background(screen,consts.BACKGROUND_COLOR)
    for i in bushes:
        drew_bush(i[0],i[1])

    if not state['is_screen_visible']:# להפוך את המסך לשחור
        draw_grid(screen , mines_locations,pits_locations)

    draw_flag(state['flag_x'],state['flag_y'])

    if state['player_state'] == 'injured':
        player = pygame.image.load(consts.INJURED_PLAYER_IMAGE)
        draw_lost_massage()
    elif state['player_state'] == 'soldier_nigth':
        player = pygame.image.load(consts.PLAYER_NIGTH)
    elif state['player_state'] == 'won':
        draw_win_massage()
    else:
        player = pygame.image.load(consts.PLAYER_IMAGE)

    draw_player(state['player_x'],state['player_y'])

    if not time.time() - start_time >5:
        wellcome_massage()

    if state['won_game']:
        state['won_game'] = False
        state['player_state'] = 'won'
        state['enable_input'] = False

    draw_dinosaur(dinosaur_location[0],dinosaur_location[1]-3)

    pygame.display.flip()
    clock.tick(60)
    return bushes