def get_integer(min, max, message):
    while True:
        try:
            _int = int(input(message))
            if _int < min or _int > max:
                raise ValueError
        except ValueError:
            print(f'Please enter a whole number between {min} and {max}\n')
            continue
        break
    return _int

def display_board(board, b_size, is_demo = False):
    max_width = len(str(b_size ** 2)) if is_demo else 1
    print('-' * (b_size * (max_width + 3) + 1))
    for i in range(0, b_size ** 2, b_size):
        row_string = '|'
        for j in range(i, i + b_size):
            row_string += ' ' + str(board[j]).ljust(max_width)
            row_string += ' |'
        print(row_string)
        print('-' * (b_size * (max_width + 3) + 1))

def get_winning_lines():
    win_lines = []
    b_len = b_size ** 2
    for i in range(0, b_len, b_size):
        win_lines.append([j for j in range(i, i + b_size)])
    for i in range(0, b_size):
        win_lines.append([j for j in range(i, b_len, b_size)])
    win_lines.append([i for i in range(0, b_len, b_size + 1)])
    win_lines.append([i for i in range(b_size - 1, (b_len) - 1, b_size - 1)])
    return (win_lines)

def computer_move(board):
    move_scores = {pos: 0 for pos in range(b_size ** 2) if board[pos] == ' '}
    for line in win_lines:
        line_contents = [board[pos] for pos in line]
        if line_contents.count('O') == b_size - 1 and \
           line_contents.count(' ') == 1:
            return line[line_contents.index(' ')] + 1
        if line_contents.count('X') == b_size -1 and \
           line_contents.count(' ') == 1:
            return line[line_contents.index(' ')] + 1
        if 'X' not in line_contents:
            for i in range(len(line_contents)):
                if line_contents[i] == ' ':
                    move_scores[line[i]] += 1
    return max(move_scores, key=move_scores.get) + 1

def move_is_win(_move, _symbol, board):
    for line in win_lines:
        if _move - 1 in line:
            if all((board[pos] == _symbol) for pos in line):
                return True
    return False

def game_intro():
    print('\nNoughts and Crosses')
    print('===================\n')

    print('Would you like to play a 1-player or a 2-player game?')
    num_players = get_integer(1, 2, 'Please enter number of players: ')
    
    print('\nWhat size of board would you like to play on?')
    b_size = get_integer(1,10, 'Please enter board size: ')
    print('Board squares are numbered as follows:')
    demo_board = [str(i + 1) for i in range(b_size ** 2)]
    display_board(demo_board, b_size, True)
    return (num_players, b_size)

def play_game():
    b_len = b_size ** 2
    board = [' ' for _ in range(b_len)]
    current_player = 1
    is_draw = True

    print('\nCurrent board:')
    display_board(board, b_size)

    for i in range(b_len):
        if current_player == 2 and num_players == 1:
            move = computer_move(board)
            print(f'Computer has played in square {move}')
        else:
            if num_players == 1:
                move_message = 'Please enter your move: '
            else:
                move_message = \
                    f'Please enter move for Player {current_player}: '
            while True:    
                move = get_integer(1, b_len, move_message)
                if board[move - 1] != ' ':
                    print('That square is already taken\n')
                    continue
                break

        symbol = 'X' if current_player == 1 else 'O'
        board[move - 1] = symbol
        print('\nCurrent board:')
        display_board(board, b_size)

        if move_is_win(move, symbol, board):
            if num_players == 1 and current_player == 1:
                win_message = 'You win!!\n'
            elif num_players == 1 and current_player == 2:
                win_message = 'Computer wins!! Better luck next time\n'
            else:
                win_message = f'Player {current_player} wins!!\n'
            print(win_message)
            is_draw = False
            break

        current_player = current_player % 2 + 1

    if is_draw:
        print('The game is a draw!!\n')

while True:
    
    num_players, b_size = game_intro()
    win_lines = get_winning_lines()
    play_game()

    play_again = input('Would you like to play another game? (Y/N) ')
    if play_again.lower()[0] != 'y':
        break