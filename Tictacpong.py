#!/usr/bin/env python

"""
Written and tested with python 3.7.0 on Linux
By: Lorenzo Gurri
"""
import tkinter as tk
from tkinter import font
import Pong

class Tictacpong:
    def __init__(self):
        # the root window
        self.root = tk.Tk()
        # blank img for the buttons that haven't been pressed yet
        self.BLANKIMG = tk.PhotoImage(file = "img/blank.png")
        # player one X img
        self.XIMG = tk.PhotoImage(file = "img/X.png")
        # player two O img
        self.OIMG = tk.PhotoImage(file = "img/O.png")
        # font used later in challenge button
        self.HELV32 = font.Font(family='Helvetica', size=32, weight=font.BOLD)
        # holds the actual button objects
        self.buttons = list()

        # holds the images at spots on the list
        # ex1: self.buttonsPictures[0] returns a string for what picture is at the top left spot
        #      ("X" or "O")
        # ex2: self.buttonsPictures[self.currentMove] returns the same but of the last move
        self.buttonsPictures = dict()
        # frame for the buttons
        self.centerFrame = tk.Frame(self.root)
        # player alternates between True and False
        # True means player one's turn
        # False means player two's turn
        self.player = True
        # the challenge button
        self.challenge = tk.Button(self.root, state="disabled", bg="RED", text="Challenge!", width = 12, height=1, font=self.HELV32, command=self.__challengeOnPress)
        # the last move that was made
        # it holds an index that corresponds to the buttons and buttonsPictures lists
        self.currentMove = None

    # defines what happens when the challenge button is pressed
    def __challengeOnPress(self):
        # dissable it
        self.challenge.configure(state = "disabled")
        # get its background color
        bg = self.challenge.cget("bg")
        # if it is blue, player two challenged
        if bg == "blue":
            # make a new pong object and play
            pong = Pong.Pong()
            # pass a two into the play function to tell pong that player two challenged
            pongWin = pong.play(2)
            #  if player two wins the pong match
            if pongWin == 1:
                # set the spot that was player one's to player two's because he won
                self.buttons[self.currentMove].configure(state = "disabled", image = self.OIMG)
                # update the dictionary that holds the positions
                self.buttonsPictures[self.currentMove] = "O"
                # player two's turn again
                self.player = False
                # check for a game winning move
                gameWin = self.__checkWin("O")
                # if that was a game winning move make a crappy looking popup
                # and say congrats to player two. Also dissables the root window
                if gameWin == 1:
                    finWin = tk.Toplevel()
                    finWin.grab_set()
                    finWin.grab_set()
                    finWin.protocol('WM_DELETE_WINDOW', quit)
                    lbl = tk.Label(finWin, text="Player 2 Wins!!", font=("Courier", 44)).grid(row=10, column=10)
                # if it was the last move possible and no one won, make a crappy
                # popup saying it was a tie
                elif gameWin == 0:
                    finWin = tk.Toplevel()
                    finWin.grab_set()
                    finWin.grab_set()
                    finWin.protocol('WM_DELETE_WINDOW', quit)
                    lbl = tk.Label(finWin, text="Tie!!",font=("Courier", 44)).grid(row=10, column=10)
            # if player two lost the pong game, shame him by making it player one's turn
            if pongWin == 2:
                self.player = True
        # if background of challenge button is red, player one challenged
        elif bg == "red":
            pong = Pong.Pong()
            pongWin = pong.play(1)
            #  if player one wins the pong match
            if pongWin == 1:
                # set the spot that was player two's to player one's because he won
                self.buttons[self.currentMove].configure(state = "disabled", image = self.XIMG)
                # update the dictionary that holds the positions
                self.buttonsPictures[self.currentMove] = "X"
                # player one's turn again
                self.player = True
                # check for a game winning move
                gameWin = self.__checkWin("X")
                # if that was a game winning move make a crappy looking popup
                # and say congrats to player one. Also dissables the root window
                if gameWin == 1:
                    finWin = tk.Toplevel()
                    finWin.grab_set()
                    finWin.protocol('WM_DELETE_WINDOW', quit)
                    lbl = tk.Label(finWin, text="Player 1 Wins!!", font=("Courier", 44)).grid(row=10, column=10)
                # if it was the last move possible and no one won, make a crappy
                # popup saying it was a tie
                elif gameWin == 0:
                    finWin = tk.Toplevel()
                    finWin.grab_set()
                    finWin.protocol('WM_DELETE_WINDOW', quit)
                    lbl = tk.Label(finWin, text="Tie!!", font=("Courier", 44)).grid(row=10, column=10)
            # if player one lost the pong game, shame him by making it player two's turn
            if pongWin == 2:
                self.player = False

    # defines what qualifies as a win in TicTacToe
    def __checkWin(self, s):
        """
        Board layout for reference:
            0 1 2
            3 4 5
            6 7 8
        Basically if it is three in a row in any way
        s means is the symbol for where it is, it'll either be "X", "O", or "B"
        "B" means blank
        """
        # for win
        if((self.buttonsPictures[0] == s and self.buttonsPictures[1] == s and self.buttonsPictures[2] == s) or
           (self.buttonsPictures[3] == s and self.buttonsPictures[4] == s and self.buttonsPictures[5] == s) or
           (self.buttonsPictures[6] == s and self.buttonsPictures[7] == s and self.buttonsPictures[8] == s) or
           (self.buttonsPictures[0] == s and self.buttonsPictures[3] == s and self.buttonsPictures[6] == s) or
           (self.buttonsPictures[1] == s and self.buttonsPictures[4] == s and self.buttonsPictures[7] == s) or
           (self.buttonsPictures[2] == s and self.buttonsPictures[5] == s and self.buttonsPictures[8] == s) or
           (self.buttonsPictures[0] == s and self.buttonsPictures[4] == s and self.buttonsPictures[8] == s) or
           (self.buttonsPictures[2] == s and self.buttonsPictures[4] == s and self.buttonsPictures[6] == s)):
            return 1
        # for tie
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
        # this will never happen but needed so python doesn't yell at me (don't hurt me plz)
        else:
            return -1

    # defines what happens when a button is pressed
    def __tttOnPress(self, index):
        # if it's player one's turn
        if(self.player):
            # get the index for where the move was made and set the currentMove to that
            self.currentMove = index
            # change the color of the challenge button to tell player two he could
            # challenge if he wanted to
            self.challenge.configure(state = "normal", bg="blue")
            # dissable the pressed button and set it's picture to X
            self.buttons[index].configure(state = "disabled", image = self.XIMG)
            # set the corresponding buttonsPictures index to X
            self.buttonsPictures[index] = "X"
            # check if player one won
            win = self.__checkWin("X")
            # if he won
            if win == 1:
                # make a crappy popup saying congrats
                finWin = tk.Toplevel()
                finWin.grab_set()
                finWin.protocol('WM_DELETE_WINDOW', quit)
                lbl = tk.Label(finWin, text="Player 1 Wins!!", font=("Courier", 44)).grid(row=10, column=10)
            # if it was a tie
            elif win == 0:
                # make a crappy popup for a tie. dissable root window
                finWin = tk.Toplevel()
                finWin.grab_set()
                finWin.protocol('WM_DELETE_WINDOW', quit)
                lbl = tk.Label(finWin, text="Tie!!", font=("Courier", 44)).grid(row=10, column=10)
            # player one's turn ended, it's player two's turn now
            self.player = False
        # if it's player two's turn
        else:
            # get the index for where the move was made and set the currentMove to that
            self.currentMove = index
            # change the color of the challenge button to tell player one he could
            # challenge if he wanted to
            self.challenge.configure(state = "normal", bg="red")
            # dissable the pressed button and set it's picture to O
            self.buttons[index].configure(state = "disabled", image = self.OIMG)
            # set the corresponding buttonsPictures index to O
            self.buttonsPictures[index] = "O"
            # check if player two won
            win = self.__checkWin("O")
            # if he won
            if win == 1:
                # make a crappy popup saying congrats
                finWin = tk.Toplevel()
                finWin.grab_set()
                finWin.protocol('WM_DELETE_WINDOW', quit)
                lbl = tk.Label(finWin, text="Player 2 Wins!!", font=("Courier", 44)).grid(row=10, column=10)
            # if it was a tie
            elif win == 0:
                finWin = tk.Toplevel()
                finWin.grab_set()
                finWin.protocol('WM_DELETE_WINDOW', quit)
                lbl = tk.Label(finWin, text="Tie!!",font=("Courier", 44)).grid(row=10, column=10)
            # player one's turn ended, it's player two's turn now
            self.player = True

    # define the main fuction. brings everything together
    def main(self):
        # set the window title
        self.root.wm_title("TicTacPong")
        # make it unresizable
        self.root.resizable(width=False, height=False)
        # set its background
        self.root.configure(background = "#ffffd7")
        # set the center frame grid layout with a little bit of padding
        self.centerFrame.grid(padx=10, pady=5)

        # make the challenge button
        self.challenge.grid(rowspan=2, columnspan=3, pady= 5)
        """ TODO: understand why doesn't the code below work
        for i in range(9):
            self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(i)))
        """
        # make everything blank
        for i in range(9):
            self.buttonsPictures[i] = "B"
        # define all the buttons, add them to the buttons list and define it's action (self.__tttOnPress)
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(0)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(1)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(2)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(3)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(4)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(5)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(6)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(7)))
        self.buttons.append(tk.Button(self.centerFrame, image=self.BLANKIMG, width=100, height=100, command=lambda: self.__tttOnPress(8)))

        # set where each button is
        self.buttons[0].grid(row = 2, column = 0)
        self.buttons[1].grid(row = 2, column = 1)
        self.buttons[2].grid(row = 2, column = 2)
        self.buttons[3].grid(row = 3, column = 0)
        self.buttons[4].grid(row = 3, column = 1)
        self.buttons[5].grid(row = 3, column = 2)
        self.buttons[6].grid(row = 4, column = 0)
        self.buttons[7].grid(row = 4, column = 1)
        self.buttons[8].grid(row = 4, column = 2)
        # start the main loop
        self.root.mainloop()

# if it's not being imported, let's play!
if __name__=='__main__':
    ttt = Tictacpong()
    ttt.main()
