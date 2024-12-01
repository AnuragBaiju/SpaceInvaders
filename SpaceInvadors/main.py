import turtle
import math

win = turtle.Screen()
win.title("Space Invaders")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("blue")
player.penup()
player.goto(0, -250)
player.setheading(90)

player_speed = 15


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)


win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(0, 250)
enemy_speed = 2

bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.hideturtle()
bullet.setheading(90)
bullet_speed = 20
bullet_state = "ready"


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()


def move_bullet():
    global bullet_state
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"


def move_enemy():
    global enemy_speed
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    if enemy.xcor() > 370:
        enemy.sety(enemy.ycor() - 40)
        enemy_speed *= -1

    if enemy.xcor() < -370:
        enemy.sety(enemy.ycor() - 40)
        enemy_speed *= -1


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 15


win.onkeypress(fire_bullet, "space")

while True:
    win.update()

    move_enemy()
    move_bullet()

    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bullet_state = "ready"
        bullet.setposition(0, -400)
        enemy.setposition(0, 250)
