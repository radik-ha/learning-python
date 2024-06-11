import turtle
pen = turtle.Pen()
pen.pensize(3)
pen.color("white")
pen.begin_fill()
pen.fillcolor("blue")

for i in range(2):
    pen.fd(210)
    pen.lt(120)

pen.fd(210)
pen.end_fill()
