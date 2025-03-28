import turtle

wn = turtle.Screen()
wn.setup(width=600, height=600)

pen = turtle.Turtle()

pen.up()
pen.goto(-300, 300)
pen.down()

count = 0

while count < 4:
    pen.forward(600)
    pen.left(90)
    count = count + 1

alist = []

count = 0
x = -280
y = 280

while x < 280:
    t = turtle.Turtle()
    t.up()
    t.shape("square")
    t.shapesize(0.9, 0.9)
    t.goto(x, y)
    x = x + 20

    alist.append(t)
    count = count + 1
