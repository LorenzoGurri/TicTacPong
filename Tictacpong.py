#!/usr/bin/env python

"""
Written and tested with python 3.7.0
By: Lorenzo Gurri
"""
import tkinter as tk
from tkinter import font
import Pong

class Tictacpong:
    def __init__(self):
        self.root = tk.Tk()
        self.BLANKIMG = tk.PhotoImage(file = "img/blank.png")
        self.XIMG = tk.PhotoImage(file = "img/X.png")
        self.OIMG = tk.PhotoImage(file = "img/O.png")
        self.HELV32 = font.Font(family='Helvetica', size=32, weight=font.BOLD)
        self.buttons = list()
        self.buttonsPictures = dict()
        self.centerFrame = tk.Frame(self.root)
        self.player = True
        self.challenge = tk.Button(self.root, state="disabled", bg="RED", text="Challenge!", width = 12, height=1, font=self.HELV32, command=self.__challengeOnPress)
        self.currentMove = None

    def __challengeOnPress(self):
        bg = self.challenge.cget("bg")
        if bg == "blue":
            pong = Pong.Pong()
            pongWin = pong.play(2)
            #  Player 2 challenges and wins
            if pongWin == 1:
                print("Player 2 won pong")
                self.buttons[self.currentMove].configure(state = "disabled", image = self.OIMG)
                self.buttonsPictures[self.currentMove] = "O"
                self.player = False
                gameWin = self.__checkWin("O")
                if gameWin == 1:
                    print("Player 2 wins the game!")
                    exit(0)
                elif gameWin == 0:
                    print("TIE!")
                    exit(0)
            #  Player 2 challenges and looses
            if pongWin == 2:
                print("player 1 won pong")
                self.player = True
        elif bg == "red":
            pong = Pong.Pong()
            pongWin = pong.play(1)
            #  Player 1 challenges and wins
            if pongWin == 1:
                print("Player 1 won pong")
                self.buttons[self.currentMove].configure(state = "disabled", image = self.XIMG)
                self.buttonsPictures[self.currentMove] = "X"
                self.player = False
                gameWin = self.__checkWin("X")
                if gameWin == 1:
                    print("Player 1 wins the game!")
                    exit(0)
                elif gameWin == 0:
                    print("TIE!")
                    exit(0)


    def __checkWin(self, s):
        """ Layout for reference:
        0 1 2
        3 4 5
        6 7 8
        """
        if((self.buttonsPictures[0] == s and self.buttonsPictures[1] == s and self.buttonsPictures[2] == s) or
           (self.buttonsPictures[3] == s and self.buttonsPictures[4] == s and self.buttonsPictures[5] == s) or
           (self.buttonsPictures[6] == s and self.buttonsPictures[7] == s and self.buttonsPictures[8] == s) or
           (self.buttonsPictures[0] == s and self.buttonsPictures[3] == s and self.buttonsPictures[6] == s) or
           (self.buttonsPictures[1] == s and self.buttonsPictures[4] == s and self.buttonsPictures[7] == s) or
           (self.buttonsPictures[2] == s and self.buttonsPictures[5] == s and self.buttonsPictures[8] == s) or
           (self.buttonsPictures[0] == s and self.buttonsPictures[4] == s and self.buttonsPictures[8] == s) or
           (self.buttonsPictures[2] == s and self.buttonsPictures[4] == s and self.buttonsPictures[6] == s)):
            return 1
        elif(self.buttonsPictures[0] != "B" and
                self.buttonsPictures[1] != "B" and
                self.buttonsPictures[2] != "B" and
                self.buttonsPictures[3] != "B" and
                self.buttonsPictures[4] != "B" and
                self.buttonsPictures[5] != "B" and
                self.buttonsPictures[6] != "B" and
                self.buttonsPictures[7] != "B" and
                self.buttonsPictures[8] != "B"):
            return 0
        else:
            return -1

    # Responsible for:
    #   changing button image
    #   checking for a winner or tie and acting accordingly
    #   TODO: create a congradulations player X graphic instead of printing it out to console
    def __tttOnPress(self, index):
        # Player 1's turn
        if(self.player):
            self.currentMove = index
            self.challenge.configure(state = "normal", bg="blue")
            # Set image
            self.buttons[index].configure(state = "disabled", image = self.XIMG)
            self.buttonsPictures[index] = "X"
            # Check for win or tie
            win = self.__checkWin("X")
            if win == 1:
                print("Player 1 wins")
                exit(0)
            elif win == 0:
                print("TIE!")
                exit(0)
            else:
                pass
            self.player = False
        # Player 2's turn
        else:
            self.currentMove = index
            self.challenge.configure(state = "normal", bg="red")

            self.buttons[index].configure(state = "disabled", image = self.OIMG)
            self.buttonsPictures[index] = "O"
            win = self.__checkWin("O")
            if win == 1:
                print("Player 2 wins")
                exit(0)
            elif win == 0:
                print("TIE!")
                exit(0)
            else:
                pass
                self.player = True

    def main(self):
        self.root.resizable(width=False, height=False)
        self.root.configure(background = "#ffffd7")
        self.centerFrame.grid(padx=10, pady=5)

        # TODO: Define what the command will be to start the pong game
        self.challenge.grid(rowspan=2, columnspan=3, pady= 5)
        """ TODO: understand why doesn't the code below work
        for i in range(9):
            self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(i)))
        """
        for i in range(9):
            self.buttonsPictures[i] = "B"
        # TODO:
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(0)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(1)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(2)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(3)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(4)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(5)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(6)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(7)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(8)))

        #  TODO: Make a list comprehension / loop for code below
        self.buttons[0].grid(row = 2, column = 0)
        self.buttons[1].grid(row = 2, column = 1)
        self.buttons[2].grid(row = 2, column = 2)
        self.buttons[3].grid(row = 3, column = 0)
        self.buttons[4].grid(row = 3, column = 1)
        self.buttons[5].grid(row = 3, column = 2)
        self.buttons[6].grid(row = 4, column = 0)
        self.buttons[7].grid(row = 4, column = 1)
        self.buttons[8].grid(row = 4, column = 2)
        self.root.mainloop()

if __name__=='__main__':
    ttt = Tictacpong()
    ttt.main()
