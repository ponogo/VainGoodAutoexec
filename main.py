import turtle

turtle.title("My turtle Game")
turtle.bgcolor("blue")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
bob = turtle.Turtle()

def triangle(length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x = 0
  while x < 3:
    bob.forward(int(length))
    bob.right(120)
    x+=1
  bob.end_fill()

def drawCircle(radius, color):
  bob.fillcolor(color)
  bob.begin_fill()
  bob.circle(int(radius))
  bob.end_fill()

def star(length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x=0
  while x < 5:
    bob.forward(int(length))
    bob.right(144)
    x+=1
  bob.end_fill


input_shape = input("what shape do you want to draw? ")
input_length =  input("chooses how big: ")
input_color = input("Choose color: ")

if input_shape == "triangle":
  triangle(input_length, input_color)
elif input_shape == "circle":
  drawCircle(input_length, input_color)
elif input_shape == "star":
  star(input_length, input_color)  