import turtle
import os

#configuring the window, title, dimensions(important in coordination) and background color
window = turtle.Screen()
window.title("Pong by Collins")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#scores
score_a = 0
score_b = 0

#pad A
pad_a = turtle.Turtle()
#this sets the speed of animation, not the speed of the movement of the pad, sets to max speed
pad_a.speed(1)
pad_a.shape("square")
pad_a.color('white')
pad_a.shapesize(stretch_wid = 5, stretch_len = 1)
pad_a.penup()
pad_a.goto(-350,0)

#pad B
pad_b = turtle.Turtle()
pad_b.speed(1)
pad_b.shape("square")
pad_b.color('white')
pad_b.shapesize(stretch_wid = 5, stretch_len = 1)
pad_b.penup()
pad_b.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0,0)


#pen/ scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 23, "normal"))

#pen2/ game over
end = turtle.Turtle()
end.speed(0)
end.color("white")
end.penup()
end.hideturtle()
end.goto(0,-30)

#ball movements separated into x axis movements and y axis movements
# .dx , d means delta or change in: basically change in x = 2
ball.dx = 2
ball.dy = 2

#functions that allow upward/downward movement for pad a
def pad_a_up():
    y = pad_a.ycor()
    if y > 300:
        pad_a.sety(-300)
    else:
        y += 20
        pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    if y < -300:
        pad_a.sety(300)
    else:
        y -= 20
        pad_a.sety(y)

#functions that allow upward/downward movement for pad b
def pad_b_up():
    y = pad_b.ycor()
    if y > 300:
        pad_b.sety(-300)
    else:
        y += 20
        pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    if y < -300:
        pad_b.sety(300)
    else:
        y -= 20
        pad_b.sety(y)
#function that moves the ball

#keyboard binding
window.listen()
window.onkeypress(pad_a_up, "w")
window.onkeypress(pad_a_down, "s")
window.onkeypress(pad_b_up, "Up")
window.onkeypress(pad_b_down, "Down")


#main game loop
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #top and bottom border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #left and right border checking/ score count
    if ball.xcor() > 390:
        os.system("afplay sounds/miss.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 23, "normal"))

    if ball.xcor() < -390:
        os.system("afplay sounds/miss.wav&")
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 23, "normal"))

    #pad and ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50:
        os.system("afplay sounds/hit.wav&")
        ball.setx(340)
        ball.dx *= -1


    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < pad_a.ycor() + 50  and ball.ycor() > pad_a.ycor() - 50:
        os.system("afplay sounds/hit.wav&")
        ball.setx(-340)
        ball.dx *= -1

    #ending the game
    if score_a == 5:
        window.clear()
        window.bgcolor("black")
        window.tracer(0)
        end.write("GAME OVER \nPlayer A wins!", align = "center", font = ("Courier", 90, "normal"))
        os.system("afplay sounds/winner.wav")
        break


    if score_b == 5:
        window.clear()
        window.bgcolor("black")
        window.tracer(0)
        end.write("GAME OVER \nPlayer B wins!", align = "center", font = ("Courier", 90, "normal"))
        os.system("afplay sounds/winner.wav")
        break
