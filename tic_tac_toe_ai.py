import math
import winsound

# Score board
user_score = 0
ai_score = 0
draw_score = 0

# Display board
def print_board(board):

    print()

    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")

    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")

    print(board[6], "|", board[7], "|", board[8])

    print()


# Check winner
def check_winner(board, player):

    win_positions = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in win_positions:

        if (
            board[position[0]] ==
            board[position[1]] ==
            board[position[2]] == player
        ):

            return True

    return False


# Check draw
def check_draw(board):

    return " " not in board


# User move
def user_move(board):

    while True:

        move = int(input("😊 Enter position (1-9): ")) - 1

        if move >= 0 and move <= 8 and board[move] == " ":

            board[move] = "X"
            break

        else:

            print("⚠️ Invalid move! Try again.")


# Minimax Algorithm
def minimax(board, depth, is_maximizing):

    if check_winner(board, "O"):

        return 1

    if check_winner(board, "X"):

        return -1

    if check_draw(board):

        return 0

    # AI TURN
    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, depth + 1, False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    # PLAYER TURN
    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, depth + 1, True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


# AI Move
def ai_move(board):

    best_score = -math.inf
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > best_score:

                best_score = score
                best_move = i

    board[best_move] = "O"


# MAIN PROGRAM
while True:

    # Create fresh board every game
    board = [" " for x in range(9)]

    print("\n🎮 TIC TAC TOE AI GAME 🎮")

    # Ask who plays first
    first = input("👉 Do you want to play first? (yes/no): ").lower()

    player_turn = True if first == "yes" else False

    # Game loop
    while True:

        print_board(board)

        # PLAYER TURN
        if player_turn:

            user_move(board)

            if check_winner(board, "X"):

                user_score += 1

                print_board(board)

                print("🎉 Congratulations! You Win! 😄")

                winsound.Beep(1000, 500)

                break

            if check_draw(board):

                draw_score += 1

                print_board(board)

                print("🤝 Match Draw!")

                winsound.Beep(700, 500)

                break

            player_turn = False

        # AI TURN
        else:

            print("🤖 AI is thinking...")

            ai_move(board)

            if check_winner(board, "O"):

                ai_score += 1

                print_board(board)

                print("😢 Computer Wins!")

                winsound.Beep(500, 700)

                break

            if check_draw(board):

                draw_score += 1

                print_board(board)

                print("🤝 Match Draw!")

                winsound.Beep(700, 500)

                break

            player_turn = True

    # SCORE BOARD
    print("\n🏆 SCORE BOARD 🏆")

    print("😊 User Score :", user_score)
    print("🤖 AI Score   :", ai_score)
    print("🤝 Draws      :", draw_score)

    # PLAY AGAIN OPTION
    choice = input("\n🔁 Do you want to play again? (yes/no): ").lower()

    if choice != "yes":

        print("\n👋 Thanks for playing!")
        print("💖 Have a great day!")

        break