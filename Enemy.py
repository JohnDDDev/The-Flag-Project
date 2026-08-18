import time
import consts
import Screen

def find_empty_row(matrix): # למצוא שורה ריקה עליה הדינוזאור ירוץ בשביל שהחורים והשיחים והמוקשים לא ימחקו ברגע שהוא יעלה עליהם
    for i in range(consts.MATRIX_ROWS-1,1,-1):
        if 16 <= i <= 24: continue # הטווח שאנחנו רוצים בפונקציות
        if 'mine' in matrix[i] or 'pit' in matrix[i]:
            continue
        return [47,i]
    else:
        print("no Empty Row on board")
        return [47,2]

def walk_dinosaur(matrix,x,y,is_right,state):
    for h in range(len(matrix[0])): # שיבדוק את אורך הושרה
        if matrix[y][h] != 'legs' or matrix[y][h] != 'body': # אם האיבר לא שווה לרגליים או לגוף אז שיהיה 0 בעיקרון הוא מנקה את המיקום הקודם שהיה בו השחקן
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