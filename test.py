import turtle

wn = turtle.Screen()
wn.setup(width=600, height=600)

#視窗----------------------

pen = turtle.Turtle()
pen.up()
pen.goto(-300, 300)
pen.down()

count = 0

while count < 4:
    pen.forward(600)
    pen.left(90)
    count = count + 1

#------------------------

y = 280
alist = []
raw = []
points = []

while y >= -280:
    x = -280
    raw = []
    while x <= 280:
        t = turtle.Turtle()
        t.up()
        t.shape("square")
        t.shapesize(0.9, 0.9)
        t.goto(x, y)
        x = x + 20
        raw.append(t)
    
    points.append(raw)
    y = y - 20
