import random
import consts

def add_pits(matrix,AMOUNT_OF_PITS):
    pits_locations = []
    while AMOUNT_OF_PITS>0:
        pit_x = random.randrange(1,consts.MATRIX_COLS-1)
        pit_y = random.randrange(0,consts.MATRIX_ROWS)

        while ((0 <= pit_x <= 2 and 0 <= pit_y <= 4) or
               (pit_x >= consts.MATRIX_COLS - 4 and pit_y >= consts.MATRIX_ROWS - 3)): # בדיקה אם המיקום של הפצצה נמצא במיקום שהשקן מתחיל בו ומבטל אותו

            pit_x = random.randrange(1, consts.MATRIX_COLS - 1)
            pit_y = random.randrange(0, consts.MATRIX_ROWS)

        if 'mine' in (matrix[pit_y][pit_x-1],matrix[pit_y][pit_x+1],matrix[pit_y][pit_x]) or \
                'pit' in (matrix[pit_y][pit_x-1],matrix[pit_y][pit_x+1],matrix[pit_y][pit_x]) :# בודק שהמקום שהפצצות לא אחד על השני
            continue

        matrix[pit_y][pit_x] = 'pit'
        matrix[pit_y][pit_x-1] = 'pit'
        matrix[pit_y][pit_x+1] = 'pit'
        pits_locations.append((pit_x-1,pit_y))
        AMOUNT_OF_PITS -= 1
    return matrix , pits_locations




