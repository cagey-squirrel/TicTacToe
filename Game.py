import pygame
import sys


pygame.init()

# screen
WIDTH = 300
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
L_BLUE = (0, 255, 230)
WHITE = (255, 255, 255)

# mouse
mouse_pos_x = 0
mouse_pos_y = 0
B1 = False  # Left mouse buton pressed?
B2 = False  # Right mouse button pressed?
B3 = False  # Middle mouse button pressed?

# boxes: Drawing standard 3x3 field
line_start = [(100, 0), (200, 0), (0, 100), (0, 200)]
line_end = [(100, 300), (200, 300), (300, 100), (300, 200)]
matrix = [ [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# text
text_x = "X"
text_o = "o"
MyFont = pygame.font.SysFont("monospace", 100)
MyFontWin = pygame.font.SysFont("8-Bit-Madness", 100)
label_x = MyFont.render(text_x, 1, BLACK)
label_o = MyFont.render(text_o, 1, WHITE)
label_win_x = MyFontWin.render("X WINS", 1, BLACK)
label_win_o = MyFontWin.render("O WINS", 1, BLACK)

# specification
clock = pygame.time.Clock()
run = True
box_size = 100

# creating win lines
win_columns = 0
win_rows = 0
win_diagonals = 0
win = 0


# FUNCTONS

# mouse action
def mouse_action(mouse_pos_x, mouse_pos_y, B1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        (mouse_pos_x, mouse_pos_y) = pygame.mouse.get_pos()
        (B1, B2, B3) = pygame.mouse.get_pressed()
    return (mouse_pos_x, mouse_pos_y, B1)

# draw lines
def draw_lines(line_start, line_end):
    for idx in range(len(line_start)):
        pygame.draw.line(screen, BLACK, line_start[idx], line_end[idx])

# check for clicks
def check_for_clicks(mouse_pos_x, mouse_pos_y, B1):
    x = 10 # function has to return something
    y = 10 # so we give it random values
    for idx1 in range(3):
        for idx2 in range(3):
            if idx1*box_size < mouse_pos_x < (idx1+1)*box_size and idx2*box_size < mouse_pos_y < (idx2+1)*box_size and B1:
                x = idx1 #actual values we would like to return
                y = idx2
                return (x, y)
    return (x, y)

# get counter: we count the sum of matrix, if its odd its X's turn, if it's even it's O's turn
def get_counter():
    counter = 0
    for i in range(3):
        for j in range(3):
            counter += matrix[i][j]
    return counter

# fill matrix: we check if return values are valid (not 10) and check if matrix sum is even or odd
    # if its odd its X's turn and we put 1, if its even its O's turn and we put 5
        # also we check if matrix[i][j] is 0 which means that square is not already taken
            # BONUS: Wwe also check if the game is not finished (win is equal to 0)
def fill_matrix(draw_shape_x, draw_shape_y, matrix, counter, win):
    if draw_shape_x != 10 and draw_shape_y != 10:
        if counter % 2 == 0 and matrix[draw_shape_x][draw_shape_y] == 0 and win == 0:
            matrix[draw_shape_x][draw_shape_y] = 1
        elif counter % 2 == 1 and matrix[draw_shape_x][draw_shape_y] == 0 and win == 0:
            matrix[draw_shape_x][draw_shape_y] = 5
        # print(str(counter))
    return matrix

# draw shape: for X we put 1 in matrix for O we put 5, so we check the number and print the letter
def draw_shape(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 1:
                screen.blit(label_x, (i * 100 + 20, j * 100))
            elif matrix[i][j] == 5:
                screen.blit(label_o, (i * 100 + 20, j * 100 -10))


# check columns: check columns to see if there are 3 X's (sum in matrix will be equal to 1+1+1 = 3)
    # same applies for 3 O's --- sum will be equal to 5+5+5 = 15
def check_columns(matrix, win_columns):
    for i in range(3):
        sum = 0
        for j in range(3):
            sum += matrix[i][j]
        if sum == 3:
            pygame.draw.line(screen, BLACK, (i * 100 + 50, 0), (i * 100 + 50, win_columns), 5)
            win_columns += 1
            if win_columns == 300:
                win_columns -= 300
        if sum == 15:
            pygame.draw.line(screen, WHITE, (i * 100 + 50, 0), (i * 100 + 50, win_columns), 10)
            win_columns += 1
            if win_columns == 300:
                win_columns -= 300
    return win_columns

# check rows : works the same as chack columns just for rows
def check_rows(matrix, win_rows):
    for j in range(3):
        sum = 0
        for i in range(3):
            sum += matrix[i][j]
        if sum == 3:
            # screen.blit(label_win_x, (20, 120))
            pygame.draw.line(screen, BLACK, (0, j*100+50), (win_rows, j*100+50), 5)
            win_rows += 1
            if win_rows == 300:
                win_rows -= 300

        if sum == 15:
            # screen.blit(label_win_o, (20, 120))
            pygame.draw.line(screen, WHITE, (0, j*100+50), (win_rows, j*100+50), 5)
            win_rows += 1
            if win_rows == 300:
                win_rows -= 300
    return win_rows

# check diagonals: works the same as previous 2 just checks diagonals
def chack_diagonals(matrix, win_diagonals):
    sum = 0
    sum2 = 0
    for i in range(3):
        for j in range(3):
            if i==j:  # checks elements on left diagonal
                sum += matrix[i][j]
            if i+j == 2: # checks elements of right diagonal
                sum2 += matrix[i][j]
        if sum == 3:
            pygame.draw.line(screen, BLACK, (0, 0), (win_diagonals, win_diagonals), 5)
            win_diagonals += 1
            if win_diagonals == 300:
                win_diagonals -= 300
        if sum2 == 3:
            pygame.draw.line(screen, BLACK, (0, 300), (win_diagonals, 300 - win_diagonals), 5)
            win_diagonals += 1
            if win_diagonals == 300:
                win_diagonals -= 300
        if sum2 == 15:
            pygame.draw.line(screen, WHITE, (0, 300), (win_diagonals, 300 - win_diagonals), 5)
            win_diagonals += 1
            if win_diagonals == 300:
                win_diagonals -= 300
        if sum == 15:
            pygame.draw.line(screen, WHITE, (0, 0), (win_diagonals, win_diagonals), 5)
            win_diagonals += 1
            if win_diagonals == 300:
                win_diagonals -= 300
    return win_diagonals



# PROGRAM
while run:


    mouse_pos_x, mouse_pos_y, B1 = mouse_action(mouse_pos_x, mouse_pos_y, B1)

    draw_lines(line_start, line_end)

    pygame.display.update()
    screen.fill(L_BLUE)

    draw_shape_x, draw_shape_y = check_for_clicks(mouse_pos_x, mouse_pos_y, B1)
    draw_shape(matrix)

    counter = get_counter()

    matrix = fill_matrix(draw_shape_x, draw_shape_y, matrix, counter, win)

    win_columns = check_columns(matrix, win_columns)
    win_rows = check_rows(matrix, win_rows)
    win_diagonals = chack_diagonals(matrix, win_diagonals)

    win = win_columns + win_rows + win_diagonals  # we add them so if their sum is 0 each of them is 0 as well so its
                                                    #easier to check if there's a win

    clock.tick(60)
