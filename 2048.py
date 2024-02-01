import pygame as pg
import random

pg.init()


SQUARE_SIZE = 100

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((200, 200, 200))
pg.display.set_caption("2048")
score = 0

def is_lose():
    if not board_filled():
        return False
    for i in range(4):
        if board[i][0] == board[i][1] or board[i][1] == board[i][2] or board[i][2] == board[i][3]\
        or board[0][i] == board[1][i] or board[1][i] == board[2][i] or board[2][i] == board[3][i]:
            return False
    return True
       
#def is_win():

def board_filled():
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return False
    return True

def new_tile():
    if board_filled():
        return
    while (True):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if board[r][c] == 0:
            break
    if random.random() < 0.1:
        board[r][c] = 4
    else:
        board[r][c] = 2

move_done = True                

def up():
    global score, move_done
    move_done = False
    board_changed = False
    for c in range(len(board[0])):
        zero = False
        unzero = False
        index = 0
        for r in range(len(board)):            
            if board[r][c] != 0:
                board[index][c] = board[r][c]
                index += 1
                if zero:
                    unzero = True
            else:
                zero = True
        if zero and unzero: 
            board_changed = True
        for r in range(index, len(board)):
            board[r][c] = 0

        temp = []
        r = 0
        while r < len(board) - 1 and board[r][c] != 0:
            if board[r][c] == board[r + 1][c]:
                temp.append(2 * board[r][c])
                score += 2 * board[r][c]
                board_changed = True
                r += 1
            else:
                temp.append(board[r][c])
                if r == len(board) - 2:
                    temp.append(board[r + 1][c])
            r += 1

        for r in range(len(board)):
            board[r][c] = 0
            if r < len(temp):
                board[r][c] = temp[r]
    if not board_filled() and board_changed:
        new_tile() 
    move_done = True      
        
def down():
    global score, move_done
    move_done = False
    board_changed = False   
    for c in range(len(board[0]) - 1, -1, -1):
        zero = False
        unzero = False
        index = len(board) - 1
        for r in range(len(board) - 1, -1, -1):            
            if board[r][c] != 0:
                board[index][c] = board[r][c]
                index -= 1
                if zero: 
                    unzero = True
            else:
                zero = True
        if zero and unzero:
            board_changed = True
        for r in range(index + 1):
            board[r][c] = 0
            
        temp = []
        r = len(board) - 1
        while r >= 1 and board[r][c] != 0:
            if board[r][c] == board[r - 1][c]:
                temp.append(2 * board[r][c])
                score += 2 * board[r][c]
                board_changed = True
                r -= 1
            else:
                temp.append(board[r][c])
                if r == 1:
                    temp.append(board[0][c])
            r -= 1
        for r in range(len(board)):
            board[3 - r][c] = 0
            if r < len(temp):
                board[3 - r][c] = temp[r]
    if not board_filled() and board_changed:
        new_tile()
    move_done = True

def left():
    global score, move_done
    move_done = False
    board_changed = False
    for r in range(len(board)):
        zero = False
        unzero = False
        index = 0
        for c in range(len(board[r])):            
            if board[r][c] != 0:
                board[r][index] = board[r][c]
                index += 1
                if zero: 
                    unzero = True
            else:
                zero = True
        if zero and unzero:
            board_changed = True
        for c in range(index, len(board)):
            board[r][c] = 0

        temp = []
        c = 0
        while c < len(board[r]) - 1 and board[r][c] != 0:
            if board[r][c] == board[r][c + 1]:
                temp.append(2 * board[r][c])
                score += 2 * board[r][c]
                board_changed = True
                c += 1
            else:
                temp.append(board[r][c])
                if c == len(board) - 2:
                    temp.append(board[r][c + 1])
            c += 1

        for c in range(len(board[r])):
            board[r][c] = 0
            if c < len(temp):
                board[r][c] = temp[c]
    if not board_filled() and board_changed:
        new_tile()
    move_done = True

def right():
    global score, move_done
    move_done = False
    board_changed = False
    for r in range(len(board) - 1, -1, -1):
        zero = False
        unzero = False
        index = len(board[0]) - 1
        for c in range(len(board[r]) - 1, -1, -1):            
            if board[r][c] != 0:
                board[r][index] = board[r][c]
                index -= 1
                if zero: 
                    unzero = True
            else:
                zero = True
        if zero and unzero:
            board_changed = True
        for c in range(index + 1):
            board[r][c] = 0
        temp = []
        c = len(board[r]) - 1
        while c >= 1 and board[r][c] != 0:
            if board[r][c] == board[r][c - 1]:
                temp.append(2 * board[r][c])
                score += 2 * board[r][c]
                board_changed = True
                c -= 1
            else:
                temp.append(board[r][c])
                if c == 1:
                    temp.append(board[r][0])
            c -= 1
        for c in range(len(board[r])):
            board[r][3 - c] = 0
            if c < len(temp):
                board[r][3 - c] = temp[c]
    if not board_filled() and board_changed:
        new_tile()
    move_done = True

board = [[0 for x in range(4)] for x in range(4)]
new_tile() 
new_tile()

run = True
lose = False
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN and move_done:
            if event.key == pg.K_DOWN:
                down()
            elif event.key == pg.K_UP:
                up()
            elif event.key == pg.K_LEFT:
                left()
            elif event.key == pg.K_RIGHT:
                right()
        
    if not lose:
        screen.fill((182, 182, 182))
        for r in range(len(board)):
            for c in range(len(board[r])):                
                if board[r][c] == 0:
                    color = (210, 210, 210)
                elif board[r][c] == 2:
                    color = (238, 228, 218)
                elif board[r][c] == 4:
                    color = (237, 224, 200)
                elif board[r][c] == 8:
                    color = (242, 177, 121)
                elif board[r][c] == 16:
                    color = (245, 149, 99)
                elif board[r][c] == 32:
                    color = (246, 124, 96)
                elif board[r][c] == 64:
                    color = (246, 94, 59)
                elif board[r][c] == 128:
                    color = (237, 207, 115)
                elif board[r][c] == 256:
                    color = (237, 204, 98)
                elif board[r][c] == 512:
                    color = (237, 200, 80)
                elif board[r][c] == 1024:
                    color = (237, 197, 63)
                elif board[r][c] == 2048:
                    color = (237, 194, 45)
                elif board[r][c] > 2048:
                    color = (70, 70, 70)
                pg.draw.rect(screen, color, ((c + 0.05) * SQUARE_SIZE, (r + 0.05) * SQUARE_SIZE, SQUARE_SIZE - 10, SQUARE_SIZE - 10))
                if (board[r][c] < 100):
                    font = pg.font.SysFont(None, 70)
                elif (board[r][c] < 1000):
                    font = pg.font.SysFont(None, 55)
                elif (board[r][c] < 10000):
                    font = pg.font.SysFont(None, 45)
                elif (board[r][c] < 100000):
                    font = pg.font.SysFont(None, 40)
                else:
                    font = pg.font.SysFont(None, 37)
                text_color = (255, 255, 255)
                if board[r][c] <= 4:
                    text_color = (100, 100, 100)
                if (board[r][c] != 0):
                    img = font.render(str(board[r][c]), True, text_color)
                    if (board[r][c] < 10):
                        screen.blit(img, ((c + 0.36) * SQUARE_SIZE, (r + 0.3) * SQUARE_SIZE))
                    elif (board[r][c] < 100):
                        screen.blit(img, ((c + 0.22) * SQUARE_SIZE, (r + 0.3) * SQUARE_SIZE))
                    elif (board[r][c] < 1000):
                        screen.blit(img, ((c + 0.18) * SQUARE_SIZE, (r + 0.35) * SQUARE_SIZE))
                    elif (board[r][c] < 10000):
                        screen.blit(img, ((c + 0.14) * SQUARE_SIZE, (r + 0.38) * SQUARE_SIZE))
                    elif (board[r][c] < 100000):
                        screen.blit(img, ((c + 0.0975) * SQUARE_SIZE, (r + 0.39) * SQUARE_SIZE))
                    else:
                        screen.blit(img, ((c + 0.07) * SQUARE_SIZE, (r + 0.42) * SQUARE_SIZE))
        pg.display.set_caption("Score: " + str(score))
        #if is_win():
        if is_lose():
            lose = True
            s = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            s.set_alpha(140)
            s.fill((255,255,255))
            screen.blit(s, (0,0))
            font = pg.font.SysFont(None, 50)
            img = font.render("Game Over", True, (0, 0, 0))
            screen.blit(img, (106, 130))
        pg.display.update()
pg.quit()


