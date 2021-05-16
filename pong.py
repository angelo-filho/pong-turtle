import turtle
import platform
import os

# Getting OS name
system = platform.system()

# Setting the audios configs
audio_bounce = ""
audio_score = ""

if system == "Windows":
    import winsound

    audio_bounce = "bounce.wav&"
    audio_score = "258020__kodack__arcade-bleep-sound.wav&"
elif system == "Linux":
    audio_bounce = "aplay bounce.wav&"
    audio_score = "aplay 258020__kodack__arcade-bleep-sound.wav&"
elif "Darwin":
    audio_bounce = "afplay bounce.wav&"
    audio_score = "afplay 258020__kodack__arcade-bleep-sound.wav&"


def play_audio(audio_name):
    if system == "Windows":
        winsound.PlaySound(audio_name, winsound.SND_ASYNC)
    else:
        os.system(audio_name)

# Draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Draw paddle function
def setup_paddle(x_goto):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x_goto, 0)

    return paddle


# Draw paddle 1
paddle_1 = setup_paddle(x_goto=-350)

# Draw paddle 2
paddle_2 = setup_paddle(x_goto=350)

# Draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1
ball_speed = 0.2

# Score
score_1 = 0
score_2 = 0

# Head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# Paddle 1 Movement
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)

    
# Paddle 2 Movement
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        paddle_2.forward(30)
    else:
        paddle_2.sety(250)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        paddle_2.back(30)
    else:
        paddle_2.sety(-250)


# Keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # Ball movement
    ball.setx(ball.xcor() + (ball_speed * ball.dx))
    ball.sety(ball.ycor() + (ball_speed * ball.dy))

    # Collision with the upper wall
    if ball.ycor() > 290:
        play_audio(audio_bounce)
        ball.sety(290)
        ball.dy *= -1

    # Collision with lower wall
    if ball.ycor() < -290:
        play_audio(audio_bounce)
        ball.sety(-290)
        ball.dy *= -1

   # Collision with Left or Right wall
    if ball.xcor() < -390 or ball.xcor() > 390:
        y_side = choice([1, -1])

        if ball.xcor() > 0:
            score_1 += 1
            change_ball_angle(-1, y_side)
        else:
            score_2 += 1
            change_ball_angle(direction_y=y_side)
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        ball.goto(0, 0)
        ball_speed += 0.0025
        play_audio(audio_bounce)

    # Collision with the paddle 1
    if ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        play_audio(audio_bounce)
    # Collision with the paddle 2
    if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        play_audio(audio_bounce)
