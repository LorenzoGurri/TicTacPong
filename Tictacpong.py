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
        self.pong = Pong.Pong()
    def __challengeOnPress(self):
        if(self.player):
            self.pong.play(1)
        else:
            self.pong.play(2)

    # Responsible for:
    #   changing button image
    #   checking for a winner or tie and acting accordingly
    #   TODO: starting congradulations graphic
    def __tttOnPress(self, index):

        # Player 1's turn
        if(self.player):
            self.currentMove = index
            self.challenge.configure(state = "normal", bg="blue")
            # Set image
            self.buttons[index].configure(state = "disabled", image = self.XIMG)
            self.buttonsPictures[index] = "X"
            # Check for win or tie
            """ Layout for reference:
            0 1 2
            3 4 5
            6 7 8
            """
            if((self.buttonsPictures[0] == "X" and self.buttonsPictures[1] == "X" and self.buttonsPictures[2] == "X") or
               (self.buttonsPictures[3] == "X" and self.buttonsPictures[4] == "X" and self.buttonsPictures[5] == "X") or
               (self.buttonsPictures[6] == "X" and self.buttonsPictures[7] == "X" and self.buttonsPictures[8] == "X") or
               (self.buttonsPictures[0] == "X" and self.buttonsPictures[3] == "X" and self.buttonsPictures[6] == "X") or
               (self.buttonsPictures[1] == "X" and self.buttonsPictures[4] == "X" and self.buttonsPictures[7] == "X") or
               (self.buttonsPictures[2] == "X" and self.buttonsPictures[5] == "X" and self.buttonsPictures[8] == "X") or
               (self.buttonsPictures[0] == "X" and self.buttonsPictures[4] == "X" and self.buttonsPictures[8] == "X") or
               (self.buttonsPictures[2] == "X" and self.buttonsPictures[4] == "X" and self.buttonsPictures[6] == "X")):
               # TODO: Make a propper winning animation / graphic
               print("Player 1 Wins!!")
               exit(0)
            elif(self.buttonsPictures[0] != "B" and
                    self.buttonsPictures[1] != "B" and
                    self.buttonsPictures[2] != "B" and
                    self.buttonsPictures[3] != "B" and
                    self.buttonsPictures[4] != "B" and
                    self.buttonsPictures[5] != "B" and
                    self.buttonsPictures[6] != "B" and
                    self.buttonsPictures[7] != "B" and
                    self.buttonsPictures[8] != "B"):
                print("Tie!!")
                exit(0)
            self.player = False
        # Player 2's turn
        else:
            self.currentMove = index
            self.challenge.configure(state = "normal", bg="red")

            self.buttons[index].configure(state = "disabled", image = self.OIMG)
            self.buttonsPictures[index] = "O"
            if((self.buttonsPictures[0] == "O" and self.buttonsPictures[1] == "O" and self.buttonsPictures[2] == "O") or
               (self.buttonsPictures[3] == "O" and self.buttonsPictures[4] == "O" and self.buttonsPictures[5] == "O") or
               (self.buttonsPictures[6] == "O" and self.buttonsPictures[7] == "O" and self.buttonsPictures[8] == "O") or
               (self.buttonsPictures[0] == "O" and self.buttonsPictures[3] == "O" and self.buttonsPictures[6] == "O") or
               (self.buttonsPictures[1] == "O" and self.buttonsPictures[4] == "O" and self.buttonsPictures[7] == "O") or
               (self.buttonsPictures[2] == "O" and self.buttonsPictures[5] == "O" and self.buttonsPictures[8] == "O") or
               (self.buttonsPictures[0] == "O" and self.buttonsPictures[4] == "O" and self.buttonsPictures[8] == "O") or
               (self.buttonsPictures[2] == "O" and self.buttonsPictures[4] == "O" and self.buttonsPictures[6] == "O")):
               # TODO: Make a propper winning animation / graphic
               print("Player 2 Wins!!")
               exit(0)
            elif(self.buttonsPictures[0] != "B" and
                 self.buttonsPictures[1] != "B" and
                 self.buttonsPictures[2] != "B" and
                 self.buttonsPictures[3] != "B" and
                 self.buttonsPictures[4] != "B" and
                 self.buttonsPictures[5] != "B" and
                 self.buttonsPictures[6] != "B" and
                 self.buttonsPictures[7] != "B" and
                 self.buttonsPictures[8] != "B"):
                 print("Tie!!")
                 exit(0)
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
    graph = Tictacpong()
    graph.main()
