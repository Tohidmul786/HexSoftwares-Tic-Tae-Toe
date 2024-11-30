import os
import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Function to print the game board
def print_board(board, player_x_name):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for better UI
    print(Fore.YELLOW + "Tic-Tac-Toe Game" + Fore.RESET)
    print(Fore.GREEN + f"{player_x_name} (X) - Player 2 (O)" + Fore.RESET)
    print()
    
    # Print the board with color
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                print(Fore.RED + "X", end=" ")
            elif board[row][col] == "O":
                print(Fore.BLUE + "O", end=" ")
            else:
                print(Fore.WHITE + "-", end=" ")
        print()

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full (tie game)
def is_board_full(board):
    for row in board:
        if "-" in row:
            return False
    return True

# Function to handle player's move
def player_move(board, player, player_name):
    while True:
        try:
            print(Fore.CYAN + f" Dear {player_name}, it's your turn!" + Fore.RESET)
            row = int(input(Fore.CYAN + f"Enter row (0-2): " + Fore.RESET))
            col = int(input(Fore.CYAN + f"Enter col (0-2): " + Fore.RESET))
            if board[row][col] == "-":
                board[row][col] = player
                break
            else:
                print(Fore.RED + "That spot is already taken. Try again." + Fore.RESET)
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid input. Please enter row and column numbers between 0 and 2." + Fore.RESET)

# Function for computer (Player O) to make a random move
def computer_move(board, player):
    print(Fore.CYAN + f"Player {player} (Computer) is making a move..." + Fore.RESET)
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == "-":
            board[row][col] = player
            break

# Function to handle game initialization and opponent selection
def choose_opponent():
    print(Fore.YELLOW + "Welcome to Tic-Tac-Toe!" + Fore.RESET)
    opponent_choice = input(Fore.CYAN + "Do you want to play against (1) Human or (2) Computer? (Enter 1 or 2): " + Fore.RESET)
    while opponent_choice not in ["1", "2"]:
        print(Fore.RED + "Invalid choice! Please enter 1 for Human or 2 for Computer." + Fore.RESET)
        opponent_choice = input(Fore.CYAN + "Do you want to play against (1) Human or (2) Computer? (Enter 1 or 2): " + Fore.RESET)
    return opponent_choice == "2"  # True if Computer, False if Human

# Main function to play the game
def play_game():
    # Ask for Player X's name
    player_x_name = input(Fore.CYAN + "Enter your cute name, Player X: " + Fore.RESET)
    opponent_is_computer = choose_opponent()
    board = [["-" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_names = [player_x_name, "Player 2"]  # Player 2 can be human or computer
    
    current_player = 0
    
    while True:
        print_board(board, player_x_name)
        
        player = players[current_player]
        player_name = player_names[current_player]
        
        if player == "X":
            player_move(board, player, player_name)  # Player X is human
        elif opponent_is_computer:
            computer_move(board, player)  # Player O is computer (random move)
        else:
            player_move(board, player, player_name)  # Player O is human (if playing against another human)
        
        if check_win(board, player):
            print_board(board, player_x_name)
            if player == "X":
                print(Fore.GREEN + f"Huuryy!! Dear..{player_name} (X) wins!" + Fore.RESET)
            else:
                if opponent_is_computer:
                    print(Fore.GREEN + f"Hurrry!! Computer (Player O) wins!" + Fore.RESET)
                else:
                    print(Fore.GREEN + f"Hurrry!! Dear.. {player_name} (O) wins!" + Fore.RESET)
            break
        
        if is_board_full(board):
            print_board(board, player_x_name)
            print("Ooops!! "+Fore.YELLOW + "It's a tie!" + Fore.RESET)
            break
        
        # Switch player
        current_player = 1 - current_player

# Entry point of the game
if __name__ == "__main__":
    play_game()
