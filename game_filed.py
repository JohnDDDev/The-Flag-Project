import consts
from consts import MATRIX_COLS

game_filed = []
def create_game_filed():
    global game_filed
    game_filed= [
        create_fild_row(row , row_start=0 ,row_length= consts.MATRIX_COLS)
        for row in range(consts.MATRIX_ROWS)
    ]
