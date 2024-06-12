import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

screen = turtle.Screen()
screen.tracer(0)
screen.setup(500,500)

def drawStar():
    pen.begin_fill()
    for i in range(5):
        pen.forward(100)
        pen.right(144)
    pen.end_fill()
    
s = 0
nx = -380
pen.goto(nx,0)
colors = ["red", "green", "blue", "yellow", "violet", "indigo", "orange"]
c = 0

while True:
    pen.clear()
    pen.fillcolor(colors[c])
    c+=1
    if c==len(colors):
        c=0
    drawStar()
    screen.update()
    pen.fd(0.1)
    s+=0.1
    if int(s)==246*2+150:
        s = 0
        pen.goto(nx,0)
