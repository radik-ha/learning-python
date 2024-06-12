import turtle
screen = turtle.Screen()
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.hideturtle()

def drawSquare1(color, fwd):
    pen1.fillcolor(color)
    pen1.begin_fill()
    for s in range(4):
        pen1.fd(fwd)
        pen1.lt(90)
    pen1.end_fill()

def drawSquare(color, fwd):
    pen.fillcolor(color)
    pen.begin_fill()
    for s in range(4):
        pen.fd(fwd)
        pen.lt(90)
    pen.end_fill()
    
while True:
    pen.clear()
    pen1.clear()
    drawSquare("red", 50)
    drawSquare1("green", 80)
    screen.update()
    pen.fd(0.03)
    pen1.lt(0.01)
    pen.lt(0.01)
