import os
import time
import random

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

player = "x"
computer = "o"
figur = ""


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
            checkwin(board, player)

        else:
            get_board()
            
            print("Player bitte Feld wählen:")
            player_set = int(input("> "))

            if board[player_set] != player and computer:
                board[player_set] = player
                checkwin(board, player)

            else:
                print("PC ist am Zug")
        think = True
        
        while think:
            random.seed()
            computer_set = random.randint(0,8)
            if board[computer_set] != player and computer:
                board[computer_set] = computer
                checkwin(board, computer)
                #get_board()
                break

def checkwin(board, figur):
    print(board)
    figur = figur
    if board[0] == figur:
        if board[1] == figur:
            if board[2] == figur:
                if figur == player:
                    print("Der Spieler hat gewonnen")
                    end_screen()
                else:
                    print("Der Computer hat gewonnen")
                    end_screen()
        elif board[4] == figur:
            if board[8] == figur:
                if figur == player:
                    print("Der Spieler hat gewonnen")
                    end_screen()
                else:
                    print("Der Computer hat gewonnen")
                    end_screen()
        elif board[3] == figur:
            if board[6] == figur:
                if figur == player:
                    print("Der Spieler hat gewonnen")
                    end_screen()
                else:
                    print("Der Computer hat gewonnen")
                    end_screen()

    if board[3] == figur:
        if board[4] == figur:
            if board[5] == figur:
                if figur == player:
                    print("Der Spieler hat gewonnen")
                    end_screen()
                else:
                    print("Der Computer hat gewonnen")
                    end_screen()

    if board[6] == figur:
        if board[7] == figur:
            if board[8] == figur:
                if figur == player:
                    print("Der Spieler hat gewonnen")
                    end_screen()
                else:
                    print("Der Computer hat gewonnen")
                    end_screen()
        
    
def get_board():
    print("Feld schon Belegt \nBitte nochmal eingeben")
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])
    print("")

def end_screen():
    time.sleep(1)

play_game()
