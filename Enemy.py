import consts

right = True

def find_empty_row(matrix):
    for i in range(consts.MATRIX_ROWS-1,1,-1):
        if 'mine' in matrix[i] or 'pit' in matrix[i]:
            continue
        return 49,i
    else:
        print("no Empty Row on board")
        return 49,2

def walk_dinosaur(matrix,x,y,walk_right=right):

    if x == 0 :
        walk_right = True
    elif x == 49:
        walk_right = False

    if walk_right: #אם ללכת ימינה ללכת ימינה עד שהוא נוגע בקיר ואם הוא נוגע בקיר להחליף ל right=False
        print("walking right")
    else:
        print("walking left")