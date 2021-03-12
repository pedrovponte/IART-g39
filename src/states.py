# returns true if final state is reached
def objectiveTest(board):
    for row in board:
        for cel in row:
            if(cel[0]=='F'):
                return False
            
            
    return True

print(objectiveTest([
		['X','-','-','I'],
		['I','-','-','-'],
		['X','F','-','-'],
		['X','F','-','-']
		]))

# conditions so it can move to given direction (must have empty or final state in the op direction of at least one cell)
def precond(board, op):
    for row in range(len(board)):
        for col in range(len(board)):
            # means it is movable piece
            if board[row][col][0]=="I":
                if op=="up":
                    if row!=0 and board[row-1][col]!="X":
                        return True
            if board[row][col][0]=="I":
                if op=="down":
                    if row!=len(board)-1 and board[row+1][col]!="X":
                        return True
            if board[row][col][0]=="I":
                if op=="left":
                    if col!=0 and board[row][col-1]!="X":
                        return True
            if board[row][col][0]=="I":
                if op=="right":
                    if col!=len(board)-1 and board[row][col+1]!="X":
                        return True
    return False

print(precond([
		['X','-','-','-'],
		['I','-','-','-'],
		['X','F','-','-'],
		['X','F','-','I']
		], "right"))

#def effects(board,op):
