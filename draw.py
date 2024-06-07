import turtle
pen = turtle.Pen()

pen.fillcolor("green")
pen.begin_fill()
pen.forward(100)
pen.bk(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.end_fill()

color = "red"
pen.fillcolor(color)
pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.fd(200)
pen.lt(90)
pen.rt(90)
