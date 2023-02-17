import turtle
t = turtle.Pen()
t.shape('turtle')
t.clear()
t.circle(150)
t.lt(72)
for i in range(5):
    t.forward(285)
    t.lt(144)
t.rt(72)
t.penup()
t.goto(0,-10)
t.pendown()
t.circle(160)
t.hideturtle()
t.done()


