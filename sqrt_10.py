import turtle

turtle.shape('turtle')


def squares_right(forward, right, x, y):
    for _ in range(4):
        turtle.forward(forward)
        turtle.right(right)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black')


forward_ = 200
right_ = 90
x_ = 10
y_ = -10


for _ in range(10):
    squares_right(forward_, right_, x_, y_)
    forward_ -= 20
    x_ += 10
    y_ -= 10

turtle.up()
turtle.home()
turtle.mainloop()
