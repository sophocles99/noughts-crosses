winning_lines = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8],
                 [0, 3, 6],
                 [1, 4, 7],
                 [2, 5, 8],
                 [0, 4, 8],
                 [2, 4, 6]]

def move_is_win(_move, _symbol, _board):
    for line in winning_lines:
        if _move - 1 in line:
            if all((_board[square] == _symbol) for square in line):
                print(line)
                return True
    return False

def display_board(_board):
    print('-------------')
    print(f'| {_board[0]} | {_board[1]} | {_board[2]} |')
    print('-------------')
    print(f'| {_board[3]} | {_board[4]} | {_board[5]} |')
    print('-------------')
    print(f'| {_board[6]} | {_board[7]} | {_board[8]} |')
    print('-------------\n')


board = [' ' for _ in range(0, 9)]
demo_board = [str(i + 1) for i in range(0, 9)]
current_player = 1

print('\nNoughts and Crosses')
print('===================\n')
print('Board squares are numbered as follows:')
display_board(demo_board)

print('\nCurrent board:')
display_board(board)

for i in range(0, 9):
    
    while True:
        try:
            move = int(input(f'\nPlease enter move for Player {current_player}: '))
            if move < 1 or move > 9:
                raise ValueError
        except ValueError:
            print('Please enter a whole number between 1 and 9')
            continue
        if board[move - 1] != ' ':
            print('That square is already taken')
            continue
        break

    symbol = 'X' if current_player == 1 else 'O'
    board[move - 1] = symbol
    current_player = current_player % 2 + 1

    print('\nCurrent board:')
    display_board(board)

    if move_is_win(move, symbol, board):
        print(f'Player {current_player} wins!!\n')
        break