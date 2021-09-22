import turtle as t

playerA_Score = 0
playerB_Score = 0

window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# create Left Pad
leftPad = t.Turtle()
leftPad.speed(0)
leftPad.shape("square")
leftPad.color("green")
leftPad.shapesize(stretch_wid=5, stretch_len=1)
leftPad.penup()
leftPad.goto(-350, 0)

# create Right Pad
rightPad = t.Turtle()
rightPad.speed(0)
rightPad.shape("square")
rightPad.color("green")
rightPad.shapesize(stretch_wid=5, stretch_len=1)
rightPad.penup()
rightPad.goto(350, 0)

# create ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5, 5)
ball_X_direction = 0.2
ball_Y_direction = 0.2

# create pen to update score
pen = t.Turtle()
pen.speed(0)
pen.color("light blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:", align="center", font=('Arial', 24, 'normal'))


# Moving Left Pad
def leftPadUp():
    y = leftPad.ycor()
    y = y + 90
    leftPad.sety(y)


def leftPadDown():
    y = leftPad.ycor()
    y = y - 90
    leftPad.sety(y)


# Moving Right Pad
def rightPadUp():
    y = rightPad.ycor()
    y = y + 90
    rightPad.sety(y)


def rightPadDown():
    y = rightPad.ycor()
    y = y - 90
    rightPad.sety(y)


# Assign the keys
window.listen()
window.onkeypress(leftPadUp, "w")    # function calling
window.onkeypress(leftPadDown, "s")  # function calling
window.onkeypress(rightPadUp, "Up")  # function calling
window.onkeypress(rightPadDown, "Down") # function calling

# movement to the ball
while True:
    window.update()

    # movement to the ball
    ball.setx(ball.xcor()+ball_X_direction)
    ball.sety(ball.ycor()+ball_Y_direction)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball_Y_direction = ball_Y_direction * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_Y_direction = ball_Y_direction * -1

    # points
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_X_direction = ball_X_direction
        playerA_Score = playerA_Score + 1
        pen.clear()
        pen.write("Player A: {}                     Player B: {}".format(playerA_Score, playerB_Score), align='center',
                  font=('Arial', 22, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_X_direction = ball_X_direction * -1
        playerB_Score = playerB_Score + 1
        pen.clear()
        pen.write(" Player A: {}                     Player B: {}".format(playerA_Score, playerB_Score), align='center',
                  font=('Arial', 22, 'normal'))

    # Handling of collision
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightPad.ycor()+40 and ball.ycor() > rightPad.ycor()-40):
        ball.setx(340)
        ball_X_direction = ball_X_direction * -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftPad.ycor()+40 and ball.ycor() > leftPad.ycor()-40):
        ball.setx(-340)
        ball_X_direction = ball_X_direction * -1


















