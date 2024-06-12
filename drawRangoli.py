import turtle
pen = turtle.Pen()
pen.pensize(3)
pen.speed(0)
pen.penup()
pen.lt(70)
pen.pendown()
colors = ['red', "green", "blue", "yellow"]
i = 0
for x in range(40):
    pen.begin_fill()
    pen.fillcolor(colors[i])
    i+=1
    if i==4:
        i=0
    pen.lt(70)
    pen.fd(150)
    pen.rt(140)
    pen.fd(150)
    pen.end_fill()

