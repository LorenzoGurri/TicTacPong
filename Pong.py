#!/usr/bin/env python
"""
By: Lorenzo Gurri
Inspired by "Pong in Python 3" 7 part youtube series by Christian Thompson
https://www.youtube.com/watch?v=LH8WgrUWG_I
"""
# used for the paddles, ball, and for drawing the score board and winner
import turtle
# sed to decide which direction the ball goes
import random
# used for count down at start as well as when displaying the winner at end
import time

class Pong:
    def __init__(self):
        self.p1Score = 0
        self.p2Score = 0
        # for the main loop
        self.finished = False
        """
        will end as 1 or 2
        1: challenger wins
        2: defender wins
        """
        self.winner = 0

    # defines the count down at the start of the game
    def _countDown(self, pen):
        # have the pen turtle go to center screen and count down
        pen.goto(0,0)
        for i in [3, 2, 1]:
            pen.clear()
            pen.write("{}".format(i), align="center", font=("Courier", 50, "normal"))
            time.sleep(1)
        pen.clear()

    # defines what happens to the ball when it collides with a paddle
    def _paddleBallCollision(self, paddle1, paddle2, ball):
        """
        if the ball is right infront of the paddle and
        is within the range of the paddle, set the ball at the paddle and change
        its direction
        """
        if (ball.xcor() > 380 and ball.xcor() < 390) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() -50):
            ball.setx(380)
            ball.dx *= -1
        if (ball.xcor() < -380 and ball.xcor() > -390) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() -50):
            ball.setx(-380)
            ball.dx *= -1

    # defines the movement of the ball, also updates the score board and player scores
    def _ballMove(self, ball, pen):

        # defines the actual movement of the ball based on its delta x and y
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # if it hits the ceiling
        if ball.ycor() > 290:
            ball.dy *= -1
        # if it hits the floor
        elif ball.ycor() < -290:
            ball.dy *= -1
        # if it passes the defenders paddle
        if ball.xcor() > 390:
            ball.goto(0,0)
            # randomly pick which direction the ball will go
            ball.dx *= random.choice([-1,1])
            # add to challengers score
            self.p1Score+= 1
            # update score board accordingly
            pen.clear()
            pen.write("Challenger: {}  Defending: {}".format(self.p1Score, self.p2Score), align="center", font=("Courier", 16, "normal"))
            # 3 goals equals a win
            if(self.p1Score == 3):
                self.finished = True;
                self.winner = 1;
        # if it passes the challengers paddle
        if ball.xcor() < -390:
            ball.goto(0,0)
            # randomly pick which direction the ball will go
            ball.dx *= random.choice([-1,1])
            # add to challengers score
            self.p2Score+=1
            # update score board accordingly
            pen.clear()
            pen.write("Challenger: {}  Defending: {}".format(self.p1Score, self.p2Score), align="center", font=("Courier", 16, "normal"))
            # 3 goals equals a win
            if(self.p2Score == 3):
                self.finished = True;
                self.winner = 2;


    """
    defines paddle movement and manages their bounds
    dir is a string that says which direction the paddle is moving
    it is either "u" or "d" for up and down
    """
    def _paddleMove(self, paddle, dir):
        y = paddle.ycor()
        # if the paddle is moving up
        if dir == "u":
            """
            if the paddle is at or above the ceiling,
            set it at the ceiling so it doesn't fall off the board
            """
            if y >= 250:
                paddle.sety(250)
            # move paddle up by 20 otherwise
            else:
                paddle.sety(paddle.ycor() + 20)
        # if the paddle is moving down
        elif dir == "d":
            """
            if the paddle is at or below the floor,
            set it at the floor so it doesn't fall off the board
            """
            if y <= -250:
                paddle.sety(-250)
            # move paddle down by 20 otherwise
            else:
                paddle.sety(paddle.ycor() - 20)

    """
    defines the game by bringing all the components together
    basically the equivalent of a main function
    challenger is an integer and it tells the program who the challenger is
    either player one or player 2
    """
    def play(self, challenger):
        # this is here so there can be more than one challenge per game
        turtle.TurtleScreen._RUNNING = True
        # the window of the game
        win = turtle.Screen()
        # set the title
        win.title("Pong")
        # set the background color
        win.bgcolor("black")
        # set the size
        win.setup(width=800, height=600)
        """
        don't update the screen automatically,
        make me update it manually with <windowName>.update()
        """
        win.tracer(0)

        # challenger's paddle
        p1 = turtle.Turtle()
        p1.speed(0)
        p1.shape("square")
        # make paddle tall
        p1.shapesize(stretch_wid=5,stretch_len=0.5)
        p1.penup()
        p1.goto(-380,0)
        # defender's paddle
        p2 = turtle.Turtle()
        p2.speed(0)
        p2.shape("square")
        # make paddle tall
        p2.shapesize(stretch_wid=5,stretch_len=0.5)
        p2.penup()
        p2.goto(380,0)
        # set the colors of each depending on who the challenger is
        if challenger == 1:
            p1.color("red")
            p2.color("blue")
        else:
            p1.color("blue")
            p2.color("red")
        # the ball
        ball = turtle.Turtle()
        """
        the ball moves as fast as the CPU will permit it which makes it speed up
        and slow down slightly depending on the CPU. Still in the process of
        determining if this should be a feature or a bug
        """
        ball.speed(0)
        ball.shape("square")
        # make it smaller
        ball.shapesize(stretch_wid=0.5,stretch_len=0.5)
        ball.color("white")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.2
        ball.dy = -0.2

        # the pen draws the count down, score board and who wins
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        self._countDown(pen)
        # display the initial score
        pen.goto(0,260)
        pen.write("Challenger: {}  Defending: {}".format(self.p1Score, self.p2Score), align="center", font=("Courier", 16, "normal"))
        # listen for keyboard events
        win.listen()
        win.onkeypress(lambda: self._paddleMove(p1,"u"), "w")
        win.onkeypress(lambda: self._paddleMove(p1,"d"), "s")
        win.onkeypress(lambda: self._paddleMove(p2,"u"), "Up")
        win.onkeypress(lambda: self._paddleMove(p2,"d"), "Down")
        # self.finished is changed after a win is determined (3 goals) is hit
        while not self.finished:
            # move the ball
            self._ballMove(ball, pen)
            # check for collisions
            self._paddleBallCollision(p1, p2, ball)
            # update the screen
            win.update()
        # hide the ball and paddles when displaying the final score
        ball.hideturtle()
        p1.hideturtle()
        p2.hideturtle()
        # send the pen to the center of the screen
        pen.goto(0,0)
        # if player one challenges
        if challenger == 1:
            # and wins
            if self.winner == 1:
                pen.color("red")
                pen.write("The Challenger Wins!!", align="center", font=("Courier", 24, "normal"))
            # and looses
            elif self.winner == 2:
                pen.color("blue")
                pen.write("The Defender Wins!!", align="center", font=("Courier", 24, "normal"))
        # if player two challenges
        elif challenger == 2:
            # and wins
            if self.winner == 2:
                pen.color("blue")
                pen.write("The Challenger Wins!!", align="center", font=("Courier", 24, "normal"))
            # and looses
            elif self.winner == 1:
                pen.color("red")
                pen.write("The Defender Wins!!", align="center", font=("Courier", 24, "normal"))
        # update the screen so the turtles are hidden and the message is printed
        win.update()
        # wait three seconds so users can see it
        time.sleep(3)
        # exit the window
        win.bye()
        # return the winner
        return self.winner
