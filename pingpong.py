import turtle

s = turtle.Screen()
s.title("Ping Pong By @real0M4R")
s.bgcolor("black")
s.setup(width=800, height=600)
s.tracer(0)

board1 = turtle.Turtle()
board1.speed(0)
board1.shapesize(stretch_wid=5, stretch_len=1)
board1.shape("square")
board1.color("blue")
board1.penup()
board1.goto(-350, 0)

board2 = turtle.Turtle()
board2.speed(0)
board2.shapesize(stretch_wid=5, stretch_len=1)
board2.shape("square")
board2.color("red")
board2.penup()
board2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

score = turtle.Turtle()
score.speed(0)
score.pencolor("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0    Player 2: 0", align="center", font=("8514oem", 20, "normal"))
score1 = 0
score2 = 0

lead = turtle.Turtle()
lead.pencolor("white")
lead.penup()
lead.hideturtle()
lead.goto(0, 240)

def board1_up():
    y = board1.ycor()
    y += 20
    board1.sety(y)


def board1_down():
    y = board1.ycor()
    y -= 20
    board1.sety(y)


s.listen()
s.onkeypress(board1_up, "w")
s.onkeypress(board1_down, "s")  # Pass the function, not the result of calling it


def board2_up():
    y = board2.ycor()
    y += 20
    board2.sety(y)


def board2_down():
    y = board2.ycor()
    y -= 20
    board2.sety(y)


s.listen()
s.onkeypress(board2_up, "Up")
s.onkeypress(board2_down, "Down")  # Pass the function, not the result of calling it

while True:
    s.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(score1, score2), align="center",
                    font=("8514oem", 20, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {}    Player 2: {}".format(score1, score2), align="center",
                    font=("8514oem", 20, "normal"))

    if (340 < ball.xcor() < 350) and (board2.ycor() + 40 > ball.ycor() > board2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (board1.ycor() + 40 > ball.ycor() > board1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if score1 > score2:
        lead.clear()
        lead.write("Player 1 Has the lead!", align="center", font=("8514oem", 18, "normal"))

    if score2 > score1:
        lead.clear()
        lead.write("Player 2 Has the lead!", align="center", font=("8514oem", 18, "normal"))

