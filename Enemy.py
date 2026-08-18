import time
import consts
import Screen



def find_empty_row(matrix):
    for i in range(consts.MATRIX_ROWS-1,1,-1):
        if 16 <= i <= 24: continue
        if 'mine' in matrix[i] or 'pit' in matrix[i]:
            continue
        return [47,i]
    else:
        print("no Empty Row on board")
        return [47,2]

def walk_dinosaur(matrix,x,y,is_right,state):
    for h in range(len(matrix[0])):
        if matrix[y][h] != 'legs' or matrix[y][h] != 'body':
            matrix[y][h] = '0'

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

    return matrix