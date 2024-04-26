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
    print("Welcome to the timestables game.")
    print("What is your name?")
    print("Only use letters when typing your name.")

    player_name_str = input ("Enter your name here:\n ")

    print (f"Nice you meet you {player_name_str}")

welcome_player()    


def player_options():
    """  
    Asks the player what they would like to do next
    """
    print("Would you like to a) see the instructions for the game or b)see the leader board or c)get straight into the gam \n")
    options = input("Type in a, b or c\n")
    if options == "a":
        print(f"You picked 'a' for instructions.")
        print("Welcome to the timestable practice game. To play this game you need to select which level you would like to play and then you can race against the clock to try to answer the questions correctly." )
 
    elif options == "b":
        print(f"You picked 'b' for the leader board")
    elif options == "c":
        """
        give options for the game levels
        """
        print(f"You picked 'c' to play a game. How tricky would you like the questions to be?") 
        level = input ("Type in 1 for easy, 2 for medium or 3 for the harderst level.\n")
        if level == "1":
            play_game_one ()
        elif level == "2":
            play_game_two ()
        elif level == "3":
            play_game_three ()
        else: 
            print("You need to answer with 1,2 or 3 to continue.")            
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

import random

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




