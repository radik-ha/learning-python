import turtle
pen = turtle.Turtle()
pen.speed(0)

colors = ["red","orange","violet","pink","green"]
x = 0
for i in range(50):
    pen.begin_fill()
    pen.fillcolor(colors[x])
    x+=1
    if x == 5:
        x = 0
    pen.fd(i*10)
    pen.rt(144)
    pen.end_fill()
turtle.done()



