import  turtle
pen = turtle.Pen()
pen.speed(7)
pen.pensize(3)
pen.begin_fill()
pen.fillcolor("lightgreen")
for i in range(4):
    pen.lt(70)
    pen.fd(150)
    pen.rt(140)
    pen.fd(150)

pen.lt(70)
pen.fd(150)
pen.rt(140)
pen.fd(160)
pen.lt(60)
pen.fd(15)
pen.end_fill()
