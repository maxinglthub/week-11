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
    pen.right(90)
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
        t.speed(0)
        t.up()
        t.shape("square")
        t.shapesize(0.9, 0.9)
        t.goto(x, y)
        x = x + 20
        raw.append(t)
    
    points.append(raw)
    y = y - 20

'''
points(len(points))
points[0][28].color("red")
points[28][28].color("red")
points[28][0].color("red")
points[14][14].color("red")
'''

wn.update()

x = int(input("Pls enter x:"))
y = int(input("Pls enter y:"))

while x < 0 or x > 28 or y < 0 or y > 28:
    print("Out of range, pls enter again")
    x = int(input("Pls enter x:"))
    y = int(input("Pls enter y:"))

points[x][y].color("red")