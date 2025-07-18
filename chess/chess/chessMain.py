'''
This is going to be our main driver file
It will be responsible for handling user input and displaying the current GameState objects.
'''

import pygame as p
import chessEngine
# from chess import chessEngine

WIDTH = HEIGHT = 512 #here we are setting the height and width of the board
DIMENSION = 8      #dimensions of the chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION   #this will give us a nice square size { 512//8=64 }
MAX_FPS = 15  #this is for animations later on
IMAGES = {}

'''
We will now add images to our python file

when using pygame it is important to load the images one time and save them as variables
because if you add images everytime you want to use them your game will become laggy since loading images takes alot of power
'''

'''
Initialize a global dictionary of images. This will be called exactly once in this main
'''

def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying "IMAGES['wp']
    #now we will try to make the images fit into our square size 
    '''
    the above forloop can be replaced by doing it manually
    
    IMAGES["wp"] = p.image.load("images/wp.png")
    IMAGES["wR"] = p.image.load("images/wR.png")
    IMAGES["wN"] = p.image.load("images/wN.png")
    IMAGES["wB"] = p.image.load("images/wB.png")
    IMAGES["wQ"] = p.image.load("images/wQ.png")
    IMAGES["WK"] = p.image.load("images/wK.png")
    IMAGES["bp"] = p.image.load("images/bp.png")
    IMAGES["bR"] = p.image.load("images/bR.png")
    IMAGES["bN"] = p.image.load("images/bN.png")
    IMAGES["bB"] = p.image.load("images/bB.png")
    IMAGES["bQ"] = p.image.load("images/bQ.png")
    IMAGES["bK"] = p.image.load("images/bK.png")
    '''
#--------------------------------#

'''
the below code is for our main driver. This will handle user input and updating the graphics
'''
def main():
    p.init() # you should initialize pygame before using it. We initialized it here because our main fuction will be the only fuction will get called
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState() # what this does it calls the board from the chessEngine file
    # we now have access to board. we access the board by coding gs.board
    loadImages()  # only do ths once, before the while loop
    running = True # this is condition for our game loop
    
    # the below variable is for remembering which square spaces the user clicked on last. Rememebr in chess, the first click is for the piece the user wants to move and the 2nd click is where he wants to move it to.
    sqSelected = () # no square is selected. (tuple: (row, col))
    playerClicks = [] # keep track of the player's clicks (two tuples: eg.[(6, 4), (4, 4)])
    #game loop
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:  # here we making it possible to move pieces with a mouse.
                location = p.mouse.get_pos() # this will get us the (x,y) location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): # the user clicked on the same square twice
                    sqSelected = () # deselect [undo]
                    playerClicks = [] # clear player clicks
                else:
                    sqSelected = (row, col) #this is for if the player's click are correct and we can start registering their clicks
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks
                if len(playerClicks) == 2: #after the 2nd click
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # reset the user clicks
                    playerClicks = []
                
        drawGameState(screen, gs)  #this is a function
        clock.tick(MAX_FPS)
        p.display.flip()
        
        
''' Responsible for all graphics within a current game state'''
def drawGameState(screen, gs): 
    #the order we call these functions matters. We have to draw the board before we draw the pieces.
    drawBoard(screen) # this fuction is going to draw the squares on the board [this is a function]
    # we add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board) # draw pieces on top op those squares [this is another function]


''' Draw the squares on the board '''
def drawBoard(screen):
    # in a chess board the top left square is always light.
    colors = [p.Color("white"), p.Color("gray")] #here you can play around with the colors of the board [eg. p.color("green"),...]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)] # this is a smart way of checking which square is supposed to be light and which is supposed to be dark(grey)
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE)) # we now create our squares and color them in. 
            
            
            
''' Draw Pieces function is going to pieces on the board using the current GameState.boarder  '''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": # not an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
if __name__ == "__main__":
    main()
        
    