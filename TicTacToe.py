import os
import time
import random

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

player = "x"
computer = "o"


def play_game():

    playing = True
    
    while playing:
        
        print(board[0], "|", board[1], "|", board[2])
        print("----------")
        print(board[3], "|", board[4], "|", board[5])
        print("----------")
        print(board[6], "|", board[7], "|", board[8])
        print("")
        
        print("Player bitte Feld wählen:")
        player_set = int(input("> "))

        if board[player_set] != player and computer:
            board[player_set] = player

        else:
            print("Feld schon Belegt \nBitte nochmal eingeben")
            print(board[0], "|", board[1], "|", board[2])
            print("----------")
            print(board[3], "|", board[4], "|", board[5])
            print("----------")
            print(board[6], "|", board[7], "|", board[8])
            print("")
            
            print("Player bitte Feld wählen:")
            player_set = int(input("> "))

            if board[player_set] != player and computer:
                board[player_set] = player

            else:
                print("PC ist am Zug")
        think = True
        
        while think:
            random.seed()
            computer_set = random.randint(0,8)
            if board[computer_set] != player and computer:
                board[computer_set] = computer
                break


play_game()
