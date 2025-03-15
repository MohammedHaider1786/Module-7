import turtle

turtle.Screen().bgcolor("Red")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to my turtle page")

board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    
turtle.done()