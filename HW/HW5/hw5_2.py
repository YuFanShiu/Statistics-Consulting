import random

def initialize_board(size=30, penalty_probability=0.3):
    return ['P' if random.random() < penalty_probability else '_' for _ in range(size)]

def roll_dice():
    return random.randint(1, 6)

def print_board(board, pos_A, pos_B, penalties_A, penalties_B):
    display = ['_' for _ in board]
    
    if pos_A == pos_B:
        if board[pos_A] == 'P':
            display[pos_A] = 'x'
        else:
            display[pos_A] = 'X'
    else:
        if pos_A < len(board):
            if board[pos_A] == 'P':
                display[pos_A] = 'a'
            else:
                display[pos_A] = 'A'
        if pos_B < len(board):
            if board[pos_B] == 'P':
                display[pos_B] = 'b'
            else:
                display[pos_B] = 'B'

    print("".join(display), f"(A: {penalties_A}, B: {penalties_B})")

def game():
    board_size = 30
    board = initialize_board(board_size)
    pos_A, pos_B = 0, 0
    penalties_A, penalties_B = 0, 0

    while pos_A < board_size - 1 and pos_B < board_size - 1:
        if penalties_A == 0:
            move_A = roll_dice()
            pos_A = min(pos_A + move_A, board_size - 1)
            penalties_A = 1 if board[pos_A] == 'P' else 0
        else:
            penalties_A = 0

        if penalties_B == 0:
            move_B = roll_dice()
            pos_B = min(pos_B + move_B, board_size - 1)
            penalties_B = 1 if board[pos_B] == 'P' else 0
        else:
            penalties_B = 0

        print_board(board, pos_A, pos_B, penalties_A, penalties_B)

    if pos_A >= board_size - 1 and pos_B >= board_size - 1:
        print("Both players win!")
    elif pos_A >= board_size - 1:
        print("Player A wins!")
    else:
        print("Player B wins!")

    reveal_board = ['P' if cell == 'P' else '_' for cell in board]
    print("".join(reveal_board))

if __name__ == "__main__":
    game()