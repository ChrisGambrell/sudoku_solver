def solve(b):
    pos = find_empty(b)
    if not pos:
        return True
    else:
        row, col = pos

    for i in range(1, 10):
        if check_valid(b, i, pos):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0
    return False


def check_valid(b, val, pos):
    for i in range(0, len(b)):
        if b[i][pos[1]] == val and pos[0] != i:
            return False

    for j in range(0, len(b[0])):
        if b[pos[0]][j] == val and pos[1] != j:
            return False

    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if b[i][j] == val and (i, j) != pos:
                return False

    return True


def find_empty(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[0])):
            if b[i][j] == 0:
                return (i, j)

    return None


def print_board(b):
    for i in range(0, len(b)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')

        for j in range(0, len(b[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + ' ', end='')


board = []
for i in range(0, 9):
    curr_row = input('Row #' + str(i + 1) +
                     ' (0 for empty, spaces between cells): ')
    curr_row_arr = curr_row.split(' ')
    curr_row_arr = [int(i) for i in curr_row_arr]

    while len(curr_row_arr) != 9:
        print('There must be 9 cells entered')
        curr_row = input('Enter row #' + str(i + 1) + ' (0 for empty): ')
        curr_row_arr = curr_row.split(' ')
        curr_row_arr = [int(i) for i in curr_row_arr]

    board.append(curr_row_arr)

print('--------------------------------------')
solve(board)
print_board(board)
