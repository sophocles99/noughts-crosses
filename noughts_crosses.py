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
            if all((_board[pos] == _symbol) for pos in line):
                return True
    return False

def computer_move(_board):
    move_scores = {pos: 0 for pos in range(9) if _board[pos] == ' '}
    for line in winning_lines:
        line_contents = [_board[pos] for pos in line]
        if line_contents.count('O') == 2 and line_contents.count(' ') == 1:
            return line[line_contents.index(' ')] + 1
        if line_contents.count('X') == 2 and line_contents.count(' ') == 1:
            return line[line_contents.index(' ')] + 1
        if 'X' not in line_contents:
            for i in range(len(line_contents)):
                if line_contents[i] == ' ':
                    move_scores[line[i]] += 1
    return max(move_scores, key=move_scores.get) + 1

def display_board(_board):
    print('-------------')
    print(f'| {_board[0]} | {_board[1]} | {_board[2]} |')
    print('-------------')
    print(f'| {_board[3]} | {_board[4]} | {_board[5]} |')
    print('-------------')
    print(f'| {_board[6]} | {_board[7]} | {_board[8]} |')
    print('-------------\n')

def get_integer(_min, _max, _message):
    while True:
        try:
            _int = int(input(_message))
            if _int < _min or _int > _max:
                raise ValueError
        except ValueError:
            print(f'Please enter a whole number between {_min} and {_max}\n')
            continue
        break
    return _int

def game_intro():
    _demo_board = [str(i + 1) for i in range(9)]
    print('\nNoughts and Crosses')
    print('===================\n')
    print('Board squares are numbered as follows:')
    display_board(_demo_board)

def play_game(_num_players):
    board = [' ' for _ in range(9)]
    current_player = 1
    is_draw = True

    print('\nCurrent board:')
    display_board(board)

    for i in range(9):
        if current_player == 2 and _num_players == 1:
            move = computer_move(board)
            print(f'Computer has played in square {move}')
        else:
            if _num_players == 1:
                move_message = 'Please enter your move: '
            else:
                move_message = \
                    f'Please enter move for Player {current_player}: '
            while True:    
                move = get_integer(1, 9, move_message)
                if board[move - 1] != ' ':
                    print('That square is already taken\n')
                    continue
                break

        symbol = 'X' if current_player == 1 else 'O'
        board[move - 1] = symbol
        print('\nCurrent board:')
        display_board(board)

        if move_is_win(move, symbol, board):
            if _num_players == 1 and current_player == 1:
                win_message = 'You win!!\n'
            elif _num_players == 1 and current_player == 2:
                win_message = 'Computer wins!! Better luck next time\n'
            else:
                win_message = f'Player {current_player} wins!!\n'
            print(win_message)
            is_draw = False
            break

        current_player = current_player % 2 + 1

    if is_draw:
        print('The game is a draw!!\n')

game_intro()

while True:
    print('Would you like to play a 1-player or a 2-player game?')
    num_players = get_integer(1, 2, 'Please enter number of players: ')
    
    play_game(num_players)

    play_again = input('Would you like to play another game? (Y/N) ')
    if play_again.lower()[0] != 'y':
        break