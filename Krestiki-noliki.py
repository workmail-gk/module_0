X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Ничья'
NUM_SQUARES = 9
SAMPLE_BOARD = range(9)

print('   ', '  ', 'поле для выбора', '<||>', '', 'игровое поле')

def choice_number(question, low, hight):
    response = None
    while response not in range(low, hight):
        response = int(input(question))
    return response

def new_board():
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def displey_board(board):
    print('\n\t',SAMPLE_BOARD[0], '|', SAMPLE_BOARD[1], '|', SAMPLE_BOARD[2], " ", " ", "<||>", " ",board[0], '|', board[1], '|', board[2])
    print('\n\t',SAMPLE_BOARD[3], '|', SAMPLE_BOARD[4], '|', SAMPLE_BOARD[5], " ", " ", "<||>", " ",board[3], '|', board[4], '|', board[5])
    print('\n\t',SAMPLE_BOARD[6], '|', SAMPLE_BOARD[7], '|', SAMPLE_BOARD[8], " ", " ", "<||>", " ",board[6], '|', board[7], '|', board[8])

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = (
                   (0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6)
                  )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] !=EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def first_move(board, first):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = choice_number('Первый игрок(Х), выберите поле (0-8)', 0, NUM_SQUARES)
        if move not in legal:
            print('Поле зянято')
    return move

def second_move(board, second):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = choice_number('Второй игрок(О), выберите поле (0-8)', 0, NUM_SQUARES)
        if move not in legal:
            print('Поле зянято')
    return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
def main():
    turn = X
    board = new_board()
    displey_board(board)
    first = X
    second = O
    while not winner(board):
        if turn == first:
            move = first_move(board, first)
            board[move] = first
        else:
            move = second_move(board, second)
            board[move] = second
        displey_board(board)
        turn = next_turn(turn)

main()
input('\n\n Нажмите Enter для заверщения...')