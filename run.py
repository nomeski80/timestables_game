import gspread
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



def welcome_player():
    """
    Welcomes player to game and gets their name.
    """
    print("Welcome to the timestables game.")
    print("What is your name?")
    print("Only use letter when typing your name.")

    player_name_str = input ("Enter your name here:")

    print (f"Nice you meet you {player_name_str}")

welcome_player()    


def player_options():
    """  
    Asks the player what they would like to do next
    """
    print("Would you like to a) see the instructions for the game or b)see the leader board or c)get straight into the game")
    if result == a:
        print(instructions) 
    elif result == b:
        print(leader_board)
    elif result == c:
        """
        give options for the game levels
        """
    else: 
        print("You need to answer with a,b or c to continue.")            

player_options()     

def instrustions ():
    """
    Explains how to play the game to a new player.
    """
    print("Welcome to the timestable practice game. To play this game you need to select which level you would liek to play and thenm you can race against the clock to try to answers the questions correctly." )


def leader_board():
    """
    Show the player the top 5 scores.
    """
    leader_board = SHEET.worksheet('leader board')


    scores = leader_board.get_all_values()

    print(scores)



def play_game_one ():   
    """
    Playes the beginner level game, providing random questions for the 2,5 and 10 times tables. 
    """    

def play_game_two ():   
    """
    Playes the medium level game, providing random questions for the 3,4 and 8 times tables. 
    """       

def play_game_three ():   
    """
    Playes the hardest level game, providing random questions for all of the times tables from 2-12. 
    """       




