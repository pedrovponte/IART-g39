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

        self.heuristic = None


# returns true if final state is reached
def objectiveTest(board):
    for row in board:
        for cel in row:
            # If there is any cell starting with "F" it means there is one final cell empty
            if(cel[0] == 'F'):
                return False
            # If the lenght of the cell is higher than 2 it means a cell is on top of a final cell
            if len(cel) > 2:
                if cel[1] != cel[3]:
                    return False
    return True


# conditions so it can move to given direction (must have empty or final state in the op direction of at least one cell)
def precond(oldboard, op):
    # Copies the passed argument so it can be modified and studied
    board = [x[:] for x in oldboard]

    # Preconditions for movement: Have at least one piece that can move in the asked direction (doesn't have a wall or end of board in asked direction)
    for row in range(len(board)):
        for col in range(len(board)):
            # means it is movable piece
            if board[row][col][0] == "I":
                if op == "up":
                    if row != 0 and board[row-1][col] != "X" and board[row-1][col][0] != "I":
                        return True
                if op == "down":
                    if row != len(board)-1 and board[row+1][col] != "X" and board[row+1][col][0] != "I":
                        return True
                if op == "left":
                    if col != 0 and board[row][col-1] != "X" and board[row][col-1][0] != "I":
                        return True
                if op == "right":
                    if col != len(board)-1 and board[row][col+1] != "X" and board[row][col+1][0] != "I":
                        return True
    return False


# Movement effects if preconditions are satisfied
def effects(oldboard, op):

    # Copies the passed argument so it can be modified and studied
    board = [x[:] for x in oldboard]

    # Verifies if the preconditions are satisfied
    if precond(board, op)==False:
        return None
    
    # Auxiliar board
    newboard = []
    if(op == "up"):
        # Since each movement makes the pieces go until there is no more room to move, then if the previous board is the same as the current it means no more movements can be made in this direction
        while(newboard != board):
            newboard = [x[:] for x in board]
            for row in range(len(board)-1, 0, -1):
                for col in range(len(board)):
                    if board[row][col][0] == "I":
                        # Top piece is not final
                        if board[row-1][col] == "-":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row-1][col] = board[row][col][:2]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row-1][col] = board[row][col]
                                board[row][col] = "-"

                        # Top piece is final
                        if board[row-1][col][0] == "F":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row-1][col] = board[row][col][:2] + board[row-1][col]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row-1][col] = board[row][col] + board[row-1][col]
                                board[row][col] = "-"             
        return board
    elif(op == "down"):
        while(newboard != board):
            newboard = [x[:] for x in board]
            for row in range(len(board)-1):
                for col in range(len(board)):
                    if board[row][col][0] == "I":
                        # Bottom is not final
                        if board[row+1][col] == "-":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row+1][col] = board[row][col][:2]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row+1][col] = board[row][col]
                                board[row][col] = "-"

                        # Bottom is final
                        if board[row+1][col][0] == "F":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row+1][col] = board[row][col][:2]+board[row+1][col]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row+1][col] = board[row][col]+board[row+1][col]
                                board[row][col] = "-"
        return board
    elif(op == "right"):
        while(newboard != board):
            newboard = [x[:] for x in board]
            for col in range(len(board)-1):
                for row in range(len(board)):
                    if board[row][col][0] == "I":
                        # Current piece is on top of another final piece
                        if board[row][col+1] == "-":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row][col+1] = board[row][col][:2]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row][col+1] = board[row][col]
                                board[row][col] = "-"
                        # Current piece is on top of another final piece
                        if board[row][col+1][0] == "F":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row][col+1] = board[row][col][:2] + board[row][col+1]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row][col+1] = board[row][col] + board[row][col+1]
                                board[row][col] = "-"
        return board
    elif(op == "left"):
        while(newboard != board):
            newboard = [x[:] for x in board]
            for col in range(len(board) - 1,0,-1):
                for row in range(len(board)):
                    if board[row][col][0] == "I":
                        # Current piece is on top of another final piece
                        if board[row][col-1] == "-":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row][col-1] = board[row][col][:2]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row][col-1] = board[row][col]
                                board[row][col] = "-"
                        # Current piece is on top of another final piece
                        if board[row][col-1][0] == "F":
                            # Current piece is on top of another final piece
                            if len(board[row][col]) > 2:
                                board[row][col-1] = board[row][col][:2] + board[row][col-1]
                                board[row][col] = board[row][col][2:]

                            # Current piece is not on top of another final piece
                            else:
                                board[row][col-1] = board[row][col] + board[row][col-1]
                                board[row][col] = "-"
        return board


# Expands a node and gets all possible nodes it can reach 
def expand_node(node):

    # List of expanded nodes to be returned
    expanded_nodes = []

    # Gets expanded nodes with movement up, donw, left and right
    expanded_nodes.append(Node(effects(node.state,"up"), node, "up", node.depth + 1, 1))
    expanded_nodes.append(Node(effects(node.state,"down"), node, "down", node.depth + 1, 1))
    expanded_nodes.append(Node(effects(node.state,"left"), node, "left", node.depth + 1, 1))
    expanded_nodes.append(Node(effects(node.state,"right"), node, "right", node.depth + 1, 1))

    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]
    
    return expanded_nodes



