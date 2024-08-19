import turtle

turtle.bgcolor("lightblue")

cap = turtle.Turtle()

# pen up becouse the first move is to get turtle into right pleace
cap.penup()


def circle(r, c):
	cap.goto(0, -r)
	cap.pendown()
	cap.color(c)
	cap.begin_fill()

	cap.circle(r)

	cap.end_fill()
	cap.penup()

circle(200, 'red')
circle(170, 'whitesmoke')
circle(140, 'red')
circle(110, 'blue')


cap.goto(0, 110)
cap.right(72)
cap.color("#edf0f2")
cap.begin_fill()
# occasionally when i do'nt wanna use the for loop 'i' set it as '_'
for _ in range(5):
	cap.forward(210)
	cap.right(144)
cap.end_fill()

cap.hideturtle()
turtle.done()