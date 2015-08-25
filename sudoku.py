import sys


# print board
def printBoard(board):
    print("-----------------------")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("-----------------------")
        for y in range(0, 9):
            if y == 0 or y == 3 or y == 6:
                print("|", end=" ")
            print(board[x][y], end=" ")
        print()
    print("-----------------------")


# check if board is full
def isFull(board):
    for x in range(0, 9):
        for y in range(0, 9):
            if board[x][y] == 0:
                return False
    return True


# find available space in board
def possibleEntries(board, i, j):

    possibilityArray = {}

    for x in range(1, 10):
        possibilityArray[x] = 0

    for y in range(0, 9):
        if not board[i][y] == 0:
            possibilityArray[board[i][y]] = 1

    for x in range(0, 9):
        if not board[x][j] == 0:
            possibilityArray[board[x][j]] = 1

    k = 0
    l = 0
    if i >= 0 and i <= 2:
        k = 0
    elif i >= 3 and i <= 5:
        k = 3
    else:
        k = 6
    if j >= 0 and j <= 2:
        l = 0
    elif j >= 3 and j <= 5:
        l = 3
    else:
        l = 6

    for x in range(k, k + 3):
        for y in range(l, l + 3):
            if not board[x][y] == 0:
                possibilityArray[board[x][y]] = 1

    for x in range(1, 10):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0

    return possibilityArray


def sudokuSolver(board):

    i = 0
    j = 0
    possiblities = {}

    if isFull(board):
        print("Board Solved Successfully!")
        printBoard(board)
        sys.exit()
    else:
        # find first free spot
        for x in range(0, 9):
            for y in range(0, 9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
            # all possible entries
        possiblities = possibleEntries(board, i, j)

        for x in range(1, 10):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]
                sudokuSolver(board)
        # backtracking
        board[i][j] = 0


# here is the input from user
def main():
    print("Bye, Bye. I'll miss u!")
SudokuBoard = [[0 for x in range(9)] for x in range(9)]
inp = input("Hello!! If u wanna to start the game just press any key.\nFor help just write help,for solve the puzzle just write start.\n")
if inp == "help":
    print("[start -- for solve the puzzle]")
    print("[exit -- for quitting the program]")
    print("[for input row and col use numbers: from 0 to 8 for row and 0 to 8 for col]\n[example ---if u wanna to put number in row 4 and col 3 just write 32]")
input1 = ""
while input1 != "exit":
    input1 = input("Insert row and col: ")
    if input1 == "exit":
        break
    elif input1 == "start":
        sudokuSolver(SudokuBoard)
        break
    else:
        input2 = int(input("insert number: "))

    if input1 == "00":
        SudokuBoard[0][0] = input2
    elif input1 == "01":
        SudokuBoard[0][1] = input2
    elif input1 == "02":
        SudokuBoard[0][2] = input2
    elif input1 == "03":
        SudokuBoard[0][3] = input2
    elif input1 == "04":
        SudokuBoard[0][4] = input2
    elif input1 == "05":
        SudokuBoard[0][5] = input2
    elif input1 == "06":
        SudokuBoard[0][6] = input2
    elif input1 == "07":
        SudokuBoard[0][7] = input2
    elif input1 == "08":
        SudokuBoard[0][8] = input2
    elif input1 == "10":
        SudokuBoard[1][0] = input2
    elif input1 == "11":
        SudokuBoard[1][1] = input2
    elif input1 == "12":
        SudokuBoard[1][2] = input2
    elif input1 == "13":
        SudokuBoard[1][3] = input2
    elif input1 == "14":
        SudokuBoard[1][4] = input2
    elif input1 == "15":
        SudokuBoard[1][5] = input2
    elif input1 == "16":
        SudokuBoard[1][6] = input2
    elif input1 == "17":
        SudokuBoard[1][7] = input2
    elif input1 == "18":
        SudokuBoard[1][8] = input2
    elif input1 == "20":
        SudokuBoard[2][0] = input2
    elif input1 == "21":
        SudokuBoard[2][1] = input2
    elif input1 == "22":
        SudokuBoard[2][2] = input2
    elif input1 == "23":
        SudokuBoard[2][3] = input2
    elif input1 == "24":
        SudokuBoard[2][4] = input2
    elif input1 == "25":
        SudokuBoard[2][5] = input2
    elif input1 == "26":
        SudokuBoard[2][6] = input2
    elif input1 == "27":
        SudokuBoard[2][7] = input2
    elif input1 == "28":
        SudokuBoard[2][8] = input2
    elif input1 == "30":
        SudokuBoard[3][0] = input2
    elif input1 == "31":
        SudokuBoard[3][1] = input2
    elif input1 == "32":
        SudokuBoard[3][2] = input2
    elif input1 == "33":
        SudokuBoard[3][3] = input2
    elif input1 == "34":
        SudokuBoard[3][4] = input2
    elif input1 == "35":
        SudokuBoard[3][5] = input2
    elif input1 == "36":
        SudokuBoard[3][6] = input2
    elif input1 == "37":
        SudokuBoard[3][7] = input2
    elif input1 == "38":
        SudokuBoard[3][8] = input2
    elif input1 == "40":
        SudokuBoard[4][0] = input2
    elif input1 == "41":
        SudokuBoard[4][1] = input2
    elif input1 == "42":
        SudokuBoard[4][2] = input2
    elif input1 == "43":
        SudokuBoard[4][3] = input2
    elif input1 == "44":
        SudokuBoard[4][4] = input2
    elif input1 == "45":
        SudokuBoard[4][5] = input2
    elif input1 == "46":
        SudokuBoard[4][6] = input2
    elif input1 == "47":
        SudokuBoard[4][7] = input2
    elif input1 == "48":
        SudokuBoard[4][8] = input2
    elif input1 == "50":
        SudokuBoard[5][0] = input2
    elif input1 == "51":
        SudokuBoard[5][1] = input2
    elif input1 == "52":
        SudokuBoard[5][2] = input2
    elif input1 == "53":
        SudokuBoard[5][3] = input2
    elif input1 == "54":
        SudokuBoard[5][4] = input2
    elif input1 == "55":
        SudokuBoard[5][5] = input2
    elif input1 == "56":
        SudokuBoard[5][6] = input2
    elif input1 == "57":
        SudokuBoard[5][7] = input2
    elif input1 == "58":
        SudokuBoard[5][8] = input2
    elif input1 == "60":
        SudokuBoard[6][0] = input2
    elif input1 == "61":
        SudokuBoard[6][1] = input2
    elif input1 == "62":
        SudokuBoard[6][2] = input2
    elif input1 == "63":
        SudokuBoard[6][3] = input2
    elif input1 == "64":
        SudokuBoard[6][4] = input2
    elif input1 == "65":
        SudokuBoard[6][5] = input2
    elif input1 == "66":
        SudokuBoard[6][6] = input2
    elif input1 == "67":
        SudokuBoard[6][7] = input2
    elif input1 == "68":
        SudokuBoard[6][8] = input2
    elif input1 == "70":
        SudokuBoard[7][0] = input2
    elif input1 == "71":
        SudokuBoard[7][1] = input2
    elif input1 == "72":
        SudokuBoard[7][2] = input2
    elif input1 == "73":
        SudokuBoard[7][3] = input2
    elif input1 == "74":
        SudokuBoard[7][4] = input2
    elif input1 == "75":
        SudokuBoard[7][5] = input2
    elif input1 == "76":
        SudokuBoard[7][6] = input2
    elif input1 == "77":
        SudokuBoard[7][7] = input2
    elif input1 == "78":
        SudokuBoard[7][8] = input2
    elif input1 == "80":
        SudokuBoard[8][0] = input2
    elif input1 == "81":
        SudokuBoard[8][1] = input2
    elif input1 == "82":
        SudokuBoard[8][2] = input2
    elif input1 == "83":
        SudokuBoard[8][3] = input2
    elif input1 == "84":
        SudokuBoard[8][4] = input2
    elif input1 == "85":
        SudokuBoard[8][5] = input2
    elif input1 == "86":
        SudokuBoard[8][6] = input2
    elif input1 == "87":
        SudokuBoard[8][7] = input2
    elif input1 == "88":
        SudokuBoard[8][8] = input2
    else:
        print("This is incorrect!")

    printBoard(SudokuBoard)

if __name__ == "__main__":
    main()
