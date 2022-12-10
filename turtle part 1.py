import turtle

turtle.Screen().setup(800, 600)
pen = turtle.Pen()

pen.penup()
pen.pendown()
pen.goto(0, 0)


pen.forward(50)
pen.left(90)

pen.penup()
pen.forward(50)
pen.left(90)
pen.pendown()

pen.forward(50)
pen.left(90)

turtle.Screen().mainloop()