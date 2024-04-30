import gspread
from random import randint
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)     
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('timestables game')
player_name_str=""
number_correct=[]

print ("W   W  EEEEE  L       CCC    OOO   M   M  EEEEE")
print ("W   W  E      L      C      O   O  MM MM  E    ")
print ("W   W  E      L      C      O   O  MM MM  E    ")
print ("W W W  EEEEE  L      C      O   O  M M M  EEEEE")
print ("WW WW  E      L      C      O   O  M   M  E    ")
print ("WW WW  E      L      C      O   O  M   M  E    ")
print ("W   W  EEEEE  LLLLL   CCC    OOO   M   M  EEEEE")


def welcome_player():
    """
    Welcomes player to game and gets their name.
    """
    print("\n")
    print("Welcome to the timestables game.")
    player_name_str = input("Enter your name here:\n ")
    print (f"Nice you meet you {player_name_str}")


def player_options():
    """  
    Asks the player what they would like to do.
    """
    print(
        """Would you like to 
        a) see the instructions for the game 
        or 
        b) see the leader board 
        or 
        c) get straight into the game?\n""")

    options = input("Type in a, b or c\n").lower()

    if options == "a":
        print(f"You picked 'a' for instructions.")
        print("Welcome to the timestable practice game. To play this game you need to select which level you would like to play and then you can race against the clock to try to answer the questions correctly." )
        player_options()
 
    elif options == "b":
        print(f"You picked 'b' for the leader board")
        leader_board()

    elif options == "c":
        """
        give options for the game levels
        """
        print(f"You picked 'c' to play a game. How tricky would you like the questions to be?") 
        level = input ("Type in 1 for easy, 2 for medium or 3 for the harderst level.\n")
        if level == "1":
            play_game("easy")
        elif level == "2":
            play_game("medium")
        elif level == "3":
            play_game("hard")
        else:
            print("You need to answer with 1,2 or 3 to continue.")            
    else:
        print("You need to answer with a,b or c to continue.")            
#if possible add option to add a timer giving player 5 sec to answer questions, or time how long it takes to answer all

def instrustions():
    """
    Explains how to play the game to a new player.
    """
    print(
        """Welcome to the timestable practice game.
     To play this game you need to select which level you would like 
     to play and then you can race against the clock to try to answers 
     the questions correctly."""
      )
    player_options()


def play_game(difficulty):   
    """
    Playes the game, providing random questions for the times tables. 
    """
    num_questions = 10

    list_values_x = [2,3,4,5,6,7,8,9,10,11,12]
    list_values_y = []
    rand_values_x = []
    rand_values_y = []
    if difficulty == "easy":
        list_values_y = [2,5,10]
    elif difficulty =="medium":
        list_values_y = [2,3,4,5,6,10]
    else: list_values_y = [2,3,4,5,6,7,8,9,10,11,12]    

    for x in range(num_questions):
            x = randint(1,12)
            rand_values_x.append(x)

    for y in range(num_questions):
            y = randint(0,len(list_values_y))
            rand_values_y.append(y) 

    number_correct = 0    

    for z in range(num_questions):
        answer = rand_values_x[z] * rand_values_y[z]   
        print("\n") 
        print("How much is", rand_values_x[z], "*", rand_values_y[z], end = "")   
        test_quest = int(input(" What is your answer?"))
        if answer == test_quest:
            number_correct = number_correct+ 1
    #add in input validation here to check answers are int and to provide user feedback if not        
    print("\n")
    print("You scored", number_correct)
    #I still need to find a way to send the name and score to worksheets

def leader_board():
    """   
    Show the player the top 5 scores.
    """
    print("Showing the top 5 scores...")
    #I need to figure out how to retrieve the previous players' scores and display them in tabulate
    leader_board_worksheet = SHEET.worksheet("leader board")
    #2d list for name and score
    leader_board = []
    leader_board.append(player_name_str)
    leader_board.append(number_correct)
    leader_board = range(0-4)
    scores = leader_board.get_all_values()
    #print() range 0-4 to show top 5 players
    print(player_name_str + scores)
    #tabulate = {player_name_str + scores}
   



welcome_player()    
player_options()
play_game()
leader_board()
instructions()








