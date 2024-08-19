import turtle

turtle.bgcolor("black")

bat = turtle.Turtle()
bat.pensize(4)
bat.color("yellow")
bat.begin_fill()


# right side
bat.left(90)
bat.circle(50, 85)
bat.circle(15, 110)
bat.right(180)
bat.circle(30, 160)
bat.right(5)
bat.forward(10)
bat.right(90)
bat.circle(-70, 145)
bat.forward(45)
bat.right(110)
bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

# head part
bat.forward(30)
bat.left(55)
bat.forward(20)
bat.left(55)
bat.forward(30)

# left side
bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)
bat.right(110)
bat.forward(45)
bat.circle(-70, 145)
bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 160)
bat.right(180)
bat.circle(15, 110)
bat.circle(50, 85)


bat.end_fill()
bat.hideturtle()
turtle.done()