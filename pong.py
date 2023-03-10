
import turtle

wn = turtle.Screen()
wn.title("Pong by Maryam Muska")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #allows the screen to stop from updating

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 #every time our ball moves, it goes by 2 pixels
ball.dy = -2

#functions
def paddle_a_up():
    y = paddle_a.ycor() #returning the y coordinate
    y += 20 #add 20 pixels to y coordinate
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

#Keyboard binding
wn.listen() #this tells it to listen
wn.onkeypress(paddle_a_up, "w") #when w is pressed, call the function to press paddle a up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #when w is pressed, call the function to press paddle a up
wn.onkeypress(paddle_b_down, "Down")
#main game loops
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0) 
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0) 
        ball.dx *= -1

    # Paddle and Ball collisions
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.dx *= -1 