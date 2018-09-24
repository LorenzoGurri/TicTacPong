#!/usr/bin/env python
"""
By: Lorenzo Gurri
Inspired by "Pong in Python 3" 7 part youtube series by Christian Thompson
https://www.youtube.com/watch?v=LH8WgrUWG_I
"""
import turtle
import random
import time

class Pong:

    def __init__(self):
        self.p1Score = 0
        self.p2Score = 0
        self.finished = False
        self.winner = 0

    def _countDown(self, pen):
        pen.goto(0,0)
        for i in [3, 2, 1]:
            pen.clear()
            pen.write("{}".format(i), align="center", font=("Courier", 50, "normal"))
            time.sleep(1)
        pen.clear()
    def _paddleBallCollision(self, paddle1, paddle2, ball):
        if (ball.xcor() > 380 and ball.xcor() < 390) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() -50):
            ball.setx(380)
            ball.dx *= -1
        if (ball.xcor() < -380 and ball.xcor() > -390) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() -50):
            ball.setx(-380)
            ball.dx *= -1

    def _ballMove(self, ball, pen):
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        if ball.ycor() > 290:
            ball.dy *= -1
        elif ball.ycor() < -290:
            ball.dy *= -1
        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= random.choice([-1,1])
            self.p1Score+= 1
            pen.clear()
            pen.write("Challenger: {}  Defending: {}".format(self.p1Score, self.p2Score), align="center", font=("Courier", 16, "normal"))
            if(self.p1Score == 3):
                self.finished = True;
                self.winner = 1;
        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= random.choice([-1,1])
            self.p2Score+=1
            pen.clear()
            pen.write("Challenger: {}  Defending: {}".format(self.p1Score, self.p2Score), align="center", font=("Courier", 16, "normal"))
            if(self.p2Score == 3):
                self.finished = True;
                self.winner = 2;

    #  updates y coordinates of paddles and
    #+ manages their bounds
    def _paddleMove(self, paddle, dir):
        y = paddle.ycor()
        if dir == "u":
            if y >= 250:
                paddle.sety(250)
            else:
                paddle.sety(paddle.ycor() + 20)
        elif dir == "d":
            if y <= (-250):
                paddle.sety(-250)
            else:
                paddle.sety(paddle.ycor() - 20)

    def play(self, challenger):
        turtle.TurtleScreen._RUNNING = True
        win = None
        win = turtle.Screen()
        win.title("Pong")
        win.bgcolor("black")
        win.setup(width=800, height=600)
        win.tracer(0)

        p1 = turtle.Turtle()
        p1.speed(0)
        p1.shape("square")
        p1.shapesize(stretch_wid=5,stretch_len=0.5)
        p1.penup()
        p1.goto(-380,0)
        p2 = turtle.Turtle()
        p2.speed(0)
        p2.shape("square")
        p2.shapesize(stretch_wid=5,stretch_len=0.5)
        p2.penup()
        p2.goto(380,0)
        if challenger == 1:
            p1.color("red")
            p2.color("blue")
        else:
            p1.color("blue")
            p2.color("red")
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.shapesize(stretch_wid=0.5,stretch_len=0.5)
        ball.color("white")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.2
        ball.dy = -0.2

        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        self._countDown(pen)
        pen.goto(0,260)
        pen.write("Challenger: {}  Defending: {}".format(self.p1Score, self.p2Score), align="center", font=("Courier", 16, "normal"))

        win.listen()
        win.onkeypress(lambda: self._paddleMove(p1,"u"), "w")
        win.onkeypress(lambda: self._paddleMove(p1,"d"), "s")
        win.onkeypress(lambda: self._paddleMove(p2,"u"), "Up")
        win.onkeypress(lambda: self._paddleMove(p2,"d"), "Down")
        while not self.finished:
            self._ballMove(ball, pen)
            self._paddleBallCollision(p1, p2, ball)
            win.update()
        win.bye()
        return self.winner
