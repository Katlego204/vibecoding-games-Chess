'''
This class is responsible for storing all the information about the current stateof a chess game. 

It will also be responsible for determining the valid moves at the current state.

It will also keep a move log.
'''

class GameState():
    # board is an 8x8 2d list. each element of the list has 2 charecters.
    # the first charecter represents the color of the piece ["b", "w"]
    # the second charecter represents the type of the piece ["K", "Q", "N", "R", "B", "p"]
    # the "--" represents an empty space with no piece
    
    def __init__(self): #we are creating a board using arrays, each list will represent a row on the chess board {Black Knight= BN}
        self.board = [ 
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], #ROW 1: [here we are using chess notation to discribe different pieces on the board.]
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"], #ROW 2: [the 2nd row in a chess board are always pawns]
            ["--", "--", "--", "--", "--", "--", "--", "--"], #ROW 3: [here I used "--" to represent an empty space in the board]
            ["--", "--", "--", "--", "--", "--", "--", "--"], #ROW 4: [here we have empty space on the row]
            ["--", "--", "--", "--", "--", "--", "--", "--"], #ROW 5: [empty space]
            ["--", "--", "--", "--", "--", "--", "--", "--"], #ROW 6: [empty space]
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"], #ROW 7: [here we have a row of white pawns]
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]  #ROW 8: [here we have a row of white royal pieces]
        
        self.whiteToMove = True # this tells us who's turn is it
        self.moveLog = [] # this will keep track of the moves made throughout this game
        
        
        # with python we are able to create nested classes. [which are classes inside of other classes]

    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap players
    
    
class Move():
    # maps keys to values
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()} # for loop to reverse a dictionary
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7} 
    colsTofiles = {v: k for k, v in filesToCols.items()} # for loop to reverse a dictionary
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow =  endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        
    
    
    def getChessNotation(self):
        #this fuction returns the chess Notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        
        
    def getRankFile(self, r, c):
        return self.colsTofiles[c] + self.rowsToRanks[r]
    
   
    