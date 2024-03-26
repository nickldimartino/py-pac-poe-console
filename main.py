# Global Variables
state = {}

# Intiialize the game
def init_game():
    # game board starts with empty values
    state["board"] = {
        "a1": " ", "b1": " ", "c1": " ",
        "a2": " ", "b2": " ", "c2": " ",
        "a3": " ", "b3": " ", "c3": " ",
    }

    # game starts with Player 1 (Player 2 is -1)
    state["turn"] = 1
    state["turns"] = 0

    #call the print_board function
    print_board()

# Print the game board
def print_board():
    print("""
            A   B   C
        1)  {a1} | {b1} | {c1}
           -----------
        2)  {a2} | {b2} | {c2}
           -----------
        3)  {a3} | {b3} | {c3}
          """.format(**state["board"]))

    # get the first move from Player 1
    get_move()

# Get the next player's move
def get_move():
    # set the prompt to the current player
    if state["turn"] == 1:
        prompt = "Player 1"
    else:
        prompt = "Player 2"
    
    # ask the current player to enter their guess
    guess = input(f"It's {prompt}'s turn! Enter a letter and a number to take a guess (a1-c3):")

    # save the user input and make it lowercase
    letter = guess[0].lower()
    num = guess[1]

    # combine the user inputted values and check their move
    check_move(letter+str(num))

# Check the player's move against the game board
def check_move(guess):
    # find the player's guess on the board and place and X or O if it's empty
    for square in state["board"]:
        if (square == guess and state["board"][square] == " "):
            if state["turn"] == 1:
                state["board"][square] = 'X'
            else:
                state["board"][square] = 'O'

    # alternate the player turn
    state["turn"] *= -1
    state["turns"] += 1

    # check for the board for a winner
    check_winner()

# Check if the board for a winner
def check_winner():
    # check if their is a winner in the vertical, horizontal, or diagonal squares
    vertWin = check_vertical()
    horiWin = check_horizontal()
    diagWin = check_diagonal()

    # if a winner was found in one of the directions, the game is over
    # else, continue game play
    if vertWin == True or horiWin == True or diagWin == True:
        # get the last player to make a guess
        turn = state["turn"] * -1

        # set the winner to the current turn and increment that players wins
        if turn == 1:
            winner = "Player 1"
            state["player1_wins"] += 1
        else:
            winner = "Player 2"
            state["player2_wins"] += 1

        # display the winner
        print(f"{winner} wins this game!")

        # display the player scores
        print("SCORE:")
        print(f"Player 1: {state['player1_wins']}   Player 2: {state['player2_wins']}   Ties: {state['ties']}")

        # determine if a player reached the number of games
        if (int(state["num_wins"]) == state['player1_wins'] or int(state["num_wins"]) == state['player2_wins']):
            
            # display the overall winner
            print(f"{winner} reached the score count! They win!")

            # ask the player's if they would like to play again
            play_again = input("Would you like to play again? (y/n): ").lower()

            # if an n was enterd, exit the game, else re-initialize the game
            if play_again == 'n':
                exit()
            else:
                init()
        else:
            init_game()
    else:
        if (state["turns"] == 9):
            print("It's a tie!")
            init_game()
        else:
            print_board()

# Check the vertical columns if all the values in each row are equal   
def check_vertical():
    # create arrays for the three vertical columns
    vertA = []
    vertB = []
    vertC = []

    # save off each square value in their designated array
    for v in state["board"]:
        if (v[0] == 'a'):
            vertA.append(state["board"][v])
        if (v[0] == 'b'):
            vertB.append(state["board"][v])
        if (v[0] == 'c'):
            vertC.append(state["board"][v])

    # if every value in the designated arrays is an X or O, return true because a winner has been found
    if vertA[0] == 'X' and vertA[1] == 'X' and vertA[2] == 'X':
        return True
    if vertB[0] == 'X' and vertB[1] == 'X' and vertB[2] == 'X':
        return True
    if vertC[0] == 'X' and vertC[1] == 'X' and vertC[2] == 'X':
        return True
    if vertA[0] == 'O' and vertA[1] == 'O' and vertA[2] == 'O':
        return True
    if vertB[0] == 'O' and vertB[1] == 'O' and vertB[2] == 'O':
        return True
    if vertC[0] == 'O' and vertC[1] == 'O' and vertC[2] == 'O':
        return True

    # no winner has been found
    return False
    
# Check the horizontal rows if all the values in each row are equal       
def check_horizontal():
    # create arrays for the three horizontal rows
    horiA = []
    horiB = []
    horiC = []

    # save off each square value in their designated array
    for v in state["board"]:
        if (v[1] == '1'):
            horiA.append(state["board"][v])
        if (v[1] == '2'):
            horiB.append(state["board"][v])
        if (v[1] == '3'):
            horiC.append(state["board"][v])

    # if every value in the designated arrays is an X or O, return true because a winner has been found
    if horiA[0] == 'X' and horiA[1] == 'X' and horiA[2] == 'X':
        return True
    if horiB[0] == 'X' and horiB[1] == 'X' and horiB[2] == 'X':
        return True
    if horiC[0] == 'X' and horiC[1] == 'X' and horiC[2] == 'X':
        return True
    if horiA[0] == 'O' and horiA[1] == 'O' and horiA[2] == 'O':
        return True
    if horiB[0] == 'O' and horiB[1] == 'O' and horiB[2] == 'O':
        return True
    if horiC[0] == 'O' and horiC[1] == 'O' and horiC[2] == 'O':
        return True

    # no winner has been found
    return False   

# Check the diagonal squares to determine if they're equal
def check_diagonal():
    # create a new board
    board = []

    # add each value of the game board in the new board
    for i in state["board"]:
        board.append(state["board"][i])

    # if one of the two diagonal rows has all X's or all O's, a winner has been found
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return True
    if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return True
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        return True
    if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        return True

    # no winner has been found
    return False 

# initialize the game file
def init():
    # print intro message to the terminal
    print("""
          ----------------------
          Let's play Py-Pac-Poe!
          ----------------------
          """)
    
    # both players start with 0 wins and there are no ties
    state["player1_wins"] = 0
    state["player2_wins"] = 0
    state["ties"] = 0
    
    # ask the players how many games they would like to play
    num_wins = input("How many wins would you like to play to?:")
    state["num_wins"] = num_wins

    # start the game
    init_game()


# Call the initialize game function
init()
