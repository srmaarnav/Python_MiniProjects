#Simple pong game in python

import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle in left and right ball in mid
#sound in python is not compatible in crossplatform

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.35
ball.dy = 0.35 #we can check for pixel speed at last

#scoring mechanism
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #no penup shows white line going from centre to 260
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

#scores
score_a=0
score_b=0

#functions to move the paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding means to search for any key pressed during turtle screem
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




#main game loop
#it will be in all games


while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking for bounce
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear() #to clear the screen else we get overlapping
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear() #to clear the screen else we get overlapping
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #paddle and ball collision

    if (ball.xcor() >340 and ball.xcor()<350)and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() <-340 and ball.xcor()>-350)and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

