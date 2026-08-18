import consts

def find_empty_row(matrix):
    for i in range(consts.MATRIX_ROWS-1,1,-1):
        if 'mine' in matrix[i] or 'pit' in matrix[i]:
            continue
        return [47,i]
    else:
        print("no Empty Row on board")
        return [47,2]

def walk_dinosaur(matrix,x,y,):
    pass