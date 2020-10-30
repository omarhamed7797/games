import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# setup the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgpic("wallpaper2you_199968.gif")
wn.bgcolor("black")
wn.setup(width=700, height=757)
wn.tracer(0)
wn.register_shape("apple.gif")
wn.register_shape("snake head(10).gif")
wn.register_shape("right.gif")
wn.register_shape("left.gif")

# snake head
head = turtle.Turtle()
head.speed(0)
head.shapesize(1.5,1.5)
head.color("red")
head.shape("snake head(10).gif")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# food
food = turtle.Turtle()
food.color("blue")
food.penup()
food.goto(100, 0)
food.shape("apple.gif")

# segment of the body
segment = []

# score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 340)
pen.write("Your score: 0    High score is: 0", align="center", font=("Fontfabric", 30, "italic"))

# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("snake head(10).gif")
def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("snake head(10).gif")
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)
        head.shape("right.gif")

    if head.direction == "left":
        head.setx(head.xcor() - 20)
        head.shape("left.gif")


def clear_segment(): #clear segment ans start again
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segment:
        seg.goto(1000, 1000)
    segment.clear()
# keyboard
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    wn.update()

    # check for borders
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
        clear_segment()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Your score: {}    High score is: {}".format(score, high_score), align="center", font=("Fontfabric", 25, "italic"))

    if head.distance(food) < 40:
        x = random.randint(-340,340)
        y = random.randint(-340,340)
        food.goto(x,y)
        # body of the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("#86231E")
        new_segment.shape("circle")
        new_segment.shapesize(1.5, 1.5)
        new_segment.penup()
        segment.append(new_segment)

        delay -= 0.001

        # calculate score
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Your score: {}    High score is: {}".format(score, high_score), align="center", font=("Fontfabric", 25, "italic"))
    # move the end segment s first in reverse order
    for index in range(len(segment)-1,0,-1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x, y)
    # move segment 0 to the body
    if len(segment) > 0:
        segment[0].goto(head.xcor(),head.ycor())

    move()

    # check for body accident
    for seg in segment:
        if seg.distance(head)<20:
            clear_segment()
            score = 0
            delay =0.1
            pen.clear()
            pen.write("Your score: {}    High score is: {}".format(score, high_score), align="center",
                      font=("Fontfabric", 25, "italic"))

    time.sleep(delay)

turtle.done()