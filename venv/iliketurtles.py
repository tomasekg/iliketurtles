from turtle import Turtle

tina = Turtle()
tina.shape("turtle")

for x in range(50):
    tina.forward(50)
    tina.right(50)

input("Press any key to exit")
