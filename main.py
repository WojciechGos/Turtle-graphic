import turtle

bob = turtle.Turtle()

bob.color("black", "blue")

table = [200]

bob.begin_fill()
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.right(90)
bob.forward(50)
bob.right(90)
bob.end_fill()

bob.sety(50)
bob.setx(50)
bob.sety(-50)

bob.color("black", "red")

bob.begin_fill()
bob.setposition(150, -50)
bob.setposition(150, 50)
bob.setposition(50, 50)
bob.end_fill()

bob.color("black", "pink")

bob.begin_fill()
bob.goto(0, 50)
bob.goto(0, 200)
bob.goto(150, 200)
bob.goto(150, 50)
bob.end_fill()

turtle.done()
