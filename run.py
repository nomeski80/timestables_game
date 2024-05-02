
import os 
from random import randint


player_name_str = ""
number_correct = []

def clear_terminal():
    """
    The clear terminal function has been added to keep the turminal tidy and easier to read. 
    code for this function was found in slack overflow. cited in the README file
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# add in a clear screen function
# take out the google sheets info

print("W   W  EEEEE  L       CCC    OOO   M   M  EEEEE")
print("W   W  E      L      C      O   O  MM MM  E    ")
print("W   W  E      L      C      O   O  MM MM  E    ")
print("W W W  EEEEE  L      C      O   O  M M M  EEEEE")
print("WW WW  E      L      C      O   O  M   M  E    ")
print("WW WW  E      L      C      O   O  M   M  E    ")
print("W   W  EEEEE  LLLLL   CCC    OOO   M   M  EEEEE")


def welcome_player():
    """
    Displays a welcome message and askes the player for their name.
    """
    print("\n")
    print("Welcome to the timestables game.")

    # player name validation to only allow letters and no empty entries
    while True:
        player_name_str = input("\nEnter your name here:\n ")
        if not (player_name_str).isalpha() or (player_name_str == ""):
            print("Invalid name, please try again using letters only.")
        else:
            print(f"Nice you meet you {player_name_str}")
            break


def instrustions():

    """
    Explains how to play the game to a new player.
    The code to create multiline strngs comes from Stack overflow,
    cited in the ReadMe file
    """
    print(
        """
    Welcome to the timestable practice game.
    To play this game you need to select which level you would like
    to play try to answers the questions correctly.
    Level 1 = easy: will test your 2,5 ad 10 timestables.
    Level 2 = medium: will test your 2,3,4,5,6, and 10 timestables
    Level 3 = Tricky: will test all of your
    times tables up to the 12 timestables!
    """)
    player_options()


def player_options():
    """
   Provides the player with options to select
   what they would like to do with the game.
    """

    print(
        """Would you like to
        a) see the instructions for the game
        or
        b) get straight into the game?\n""")
    while True:
        options = input("Type in a or b...\n").lower()

        if options == "a":
            clear_terminal()
            print(f"You picked 'a' for instructions.")
            instrustions()
            player_options()

       
        elif options == "b":
            """
            give options for the game levels
            """
            clear_terminal()
            print(
                """You picked 'b' to play a game. How tricky would you
                like the questions to be?\n""")
            while True:
                level = input(
                    """Type in 
                    1 for easy,
                    2 for medium or
                    3 for the harderst level.\n""")

                if level == "1":
                    play_game("easy")
                elif level == "2":
                    play_game("medium")
                elif level == "3":
                    play_game("hard")
                else:
                    print(
                        """Invalid choice. You need to answer with
                        1,2 or 3 to continue.\n""")
    else:
        print("You need to answer with a or b to continue.")


def play_game(difficulty):
    """
    Playes the game, providing random questions for the times tables.
    Checks that the valued inputted is an int
    if not t will reply with a message to say you have not entered a number,
    please try again.
    """
    num_questions = 10

    list_values_x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    list_values_y = []
    rand_values_x = []
    rand_values_y = []
    if difficulty == "easy":
        list_values_y = [2, 5, 10]
    elif difficulty == "medium":
        list_values_y = [2, 3, 4, 5, 6, 10]
    else:
        list_values_y = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for x in range(num_questions):
        x = randint(1, 12)
        rand_values_x.append(x)

    for y in range(num_questions):
        y = randint(0, len(list_values_y))
        rand_values_y.append(y)

    number_correct = 0

    for z in range(num_questions):
        answer = rand_values_x[z] * rand_values_y[z]
        print("\n")
        print("How much is", rand_values_x[z], "*", rand_values_y[z], end="")
        while True:
            test_quest = input(" What is your answer?\n")
            if not test_quest.isdigit():
                print("Not a number, please try again.")
            elif answer == int(test_quest):
                number_correct = number_correct + 1
                break
            else:
                print("incorrect answer")
                break

    print("\n")
    clear_terminal()
    print("You scored", number_correct,)
    player_restart()

def player_restart():
    """
    player_restart function is to give the player 
    an option to play again or to exit the game.
    """    
    while True:
        player_restart = input("\n Would  you like to play again "
                                "or exit the game? "
                                " Please answer Y/N\n") 
        if player_restart.lower() == "y":
            player_options()
            break
        elif player_restart.lower() == "n":
            clear_terminal()
            print("Thank you for playing! I hope you enjoyed the game.")
            break
        else:
            print(
                """Invalid choice. You need to answer with
                y or n to continue.\n""")
            
welcome_player()
player_options()
play_game()
instructions()
player_restart()
