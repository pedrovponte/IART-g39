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
                    if row!=0 and board[row-1][col]!="X" and board[row-1][col][0]!="I":
                        return True
            if board[row][col][0]=="I":
                if op=="down":
                    if row!=len(board)-1 and board[row+1][col]!="X" and board[row+1][col][0]!="I":
                        return True
            if board[row][col][0]=="I":
                if op=="left":
                    if col!=0 and board[row][col-1]!="X" and board[row][col-1][0]!="I":
                        return True
            if board[row][col][0]=="I":
                if op=="right":
                    if col!=len(board)-1 and board[row][col+1]!="X" and board[row][col+1][0]!="I":
                        return True
    return False

print(precond([
		['X','-','-','-'],
		['-','I','-','I'],
		['X','F','-','-'],
		['X','F','-','-']
		], "right"))

def effects(board,op):
    if(op=="up"):
        for row in range(len(board)-1,0,-1):
            for col in range(len(board)):
                if board[row][col][0]=="I":
                    # Top is not F
                    if board[row-1][col]=="-":
                        if len(board[row][col])>2:
                            board[row-1][col]=board[row][col][:2]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row-1][col]=board[row][col]
                            board[row][col]="-"
                    if board[row-1][col][0]=="F":
                        if len(board[row][col])>2:
                            board[row-1][col]=board[row][col][:2]+board[row-1][col]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row-1][col]=board[row][col]+board[row-1][col]
                            board[row][col]="-"
    if(op=="down"):
        for row in range(len(board)-1):
            for col in range(len(board)):
                if board[row][col][0]=="I":
                    # Top is not F
                    if board[row+1][col]=="-":
                        if len(board[row][col])>2:
                            board[row+1][col]=board[row][col][:2]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row+1][col]=board[row][col]
                            board[row][col]="-"
                    if board[row+1][col][0]=="F":
                        if len(board[row][col])>2:
                            board[row+1][col]=board[row][col][:2]+board[row+1][col]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row+1][col]=board[row][col]+board[row+1][col]
                            board[row][col]="-"
    if(op=="right"):
        for col in range(len(board)-1):
            for row in range(len(board)):
                if board[row][col][0]=="I":
                    # Top is not F
                    if board[row][col+1]=="-":
                        if len(board[row][col])>2:
                            board[row][col+1]=board[row][col][:2]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row][col+1]=board[row][col]
                            board[row][col]="-"
                    if board[row][col+1][0]=="F":
                        if len(board[row][col])>2:
                            board[row][col+1]=board[row][col][:2]+board[row][col+1]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row][col+1]=board[row][col]+board[row][col+1]
                            board[row][col]="-"
    if(op=="left"):
        for col in range(len(board)-1,0,-1):
            for row in range(len(board)):
                if board[row][col][0]=="I":
                    # Top is not F
                    if board[row][col-1]=="-":
                        if len(board[row][col])>2:
                            board[row][col-1]=board[row][col][:2]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row][col-1]=board[row][col]
                            board[row][col]="-"
                    if board[row][col-1][0]=="F":
                        if len(board[row][col])>2:
                            board[row][col-1]=board[row][col][:2]+board[row][col-1]
                            board[row][col]=board[row][col][2:]
                        else:
                            board[row][col-1]=board[row][col]+board[row][col-1]
                            board[row][col]="-"
    return board

print(effects([
		['X','F1','-','I4'],
		['-','I1','F2','-'],
		['X','F2','F3','I2'],
		['X','-','I3','-']
		], "left"))