# Cau 1 đa giác đều

import turtle

t = turtle.Turtle()
t.pensize(2)
t.color("blue")

side = 100  # thay đổi độ dài cạnh ở đây
for _ in range(6):
    t.forward(side)
    t.right(60)

t.hideturtle()
turtle.done()
