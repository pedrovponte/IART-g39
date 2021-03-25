import time
from pythonds.basic.stack import Stack


class Node:
    def __init__(self, state, parent, operator, depth, cost):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost

        self.heuristic=None


# returns true if final state is reached
def objectiveTest(board):
    for row in board:
        for cel in row:
            if(cel[0]=='F'):
                return False
            if len(cel)>2:
                if cel[1]!=cel[3]:
                    return False
    return True


# =============================================================================
# print(objectiveTest([
# 		['X','-','-','-'],
# 		['-','-','-','-'],
# 		['X','IOFO','-','-'],
# 		['X','ICFC','-','-']
# 		]))
# =============================================================================


# conditions so it can move to given direction (must have empty or final state in the op direction of at least one cell)
def precond(oldboard, op):
    board = [x[:] for x in oldboard]
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


# =============================================================================
# print(precond([
# 		['X','-','-','-'],
# 		['-','I','-','I'],
# 		['X','F','-','-'],
# 		['X','F','-','-']
# 		], "right"))
# =============================================================================

    
def effects(oldboard,op):
    board = [x[:] for x in oldboard]
    if precond(board,op)==False:
        return None
    newboard=[]
    if(op=="up"):
        while(newboard!=board):
            newboard = [x[:] for x in board]
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
        return board
    elif(op=="down"):
        while(newboard!=board):
            newboard = [x[:] for x in board]
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
        return board
    elif(op=="right"):
        while(newboard!=board):
            newboard = [x[:] for x in board]
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
        return board
    elif(op=="left"):
        while(newboard!=board):
            newboard = [x[:] for x in board]
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


# =============================================================================
# node1 = [['X','-','-','-'],
# 		['IB','-','I2','IY'],
# 		['X','FB','-','IJ'],
# 		['X','FY','-','-']
# 		]
# print(effects(node1,"left"))
# =============================================================================


def expand_node(node):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    expanded_nodes.append(Node(effects(node.state,"up"), node, "up", node.depth + 1, 1))
    expanded_nodes.append(Node(effects(node.state,"down"), node, "down", node.depth + 1, 1))
    expanded_nodes.append(Node(effects(node.state,"left"), node, "left", node.depth + 1, 1))
    expanded_nodes.append(Node(effects(node.state,"right"), node, "right", node.depth + 1, 1))
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    return expanded_nodes


def h(state):
    dmatch=0
    for i in range(0,9):
        if (objectiveTest(state.state)!=True):
            dmatch+=1
    state.heuristic=dmatch


