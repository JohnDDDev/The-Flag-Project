import consts


def find_empty_row(matrix):
    for i in range(consts.MATRIX_ROWS-1,1,-1):
        if 'mine' in matrix[i] or 'pit' in matrix[i]:
            continue
        return i
    else:
        print("no Empty Row on board")
        return 2

def walk_dinosaur(matrix):
    right = True

    if right: #אם ללכת ימינה ללכת ימינה עד שהוא נוגע בקיר ואם הוא נוגע בקיר להחליף ל right=False
        pass
    else:
        pass