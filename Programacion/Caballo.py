
# board: Array de 2 dimensiones de booleanos
# ej: [ [False,False],[False,False]]
def getPossibleRoutes(x,y,board, getTotal):
    totalRoutes = 0
    arrayPossible = []

    if (x+2 > 0) and (y+3 > 0):
        if not board[x+2][y+3]:
            arrayPossible.append([x+2][y+3])
            totalRoutes += 1
    if (x+2 > 0) and (y-3 > 0):
        if not board[x+2][y-3]:
            arrayPossible.append([x+2][y-3])
            totalRoutes += 1
    if (x-2 > 0) and (y+3 > 0):
        if not board[x-2][y+3]:
            arrayPossible.append([x-2][y+3])
            totalRoutes += 1
    if (x-2 > 0) and (y-3 > 0):
        if not board[x-2][y-3]:
            arrayPossible.append([x-2][y-3])
            totalRoutes += 1
    if (x+3 > 0) and (y+2 > 0):
        if not board[x+3][y+2]:
            arrayPossible.append([x+3][y+2])
            totalRoutes += 1
    if (x+3 > 0) and (y-2 > 0):
        if not board[x+3][y-2]:
            arrayPossible.append([x+3][y-2])
            totalRoutes += 1
    if (x-3 > 0) and (y+2 > 0):
        if not board[x-3][y+2]:
            arrayPossible.append([x-3][y+2])
            totalRoutes += 1
    if (x-3 > 0) and (y-2 > 0):
        if not board[x-3][y-2]:
            arrayPossible.append([x-3][y-2])
            totalRoutes += 1

    if getTotal:
        return totalRoutes
    else:
        return arrayPossible

def caballo(board):
    stillThere = True
    x = 0
    y = 0
    board[x][y] = True

    while stillThere:
        minimum = 9999999
        destinyCells = getPossibleRoutes(x,y,board,False)
        for cell in destinyCells:
            total = getPossibleRoutes(cell[0],cell[1],board,True)
            if total < minimum:
                minimum = total
                xtoGo = cell[0]
                ytoGo = cell[1]
        x = xtoGo
        y = ytoGo
        board[x][y] = True
        print board
        nothing = False
        for row in board:
            if not row.index(False):
                nothing = True
        if not nothing:
            stillThere = False
    
    return

