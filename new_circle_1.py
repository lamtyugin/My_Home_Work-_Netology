import turtle

turtle.shape('turtle')

count = 100
radius_1 = 100
radius_2 = -100

while count > 0:
    turtle.circle(radius_2)
    turtle.circle(radius_1)
    count -= 1
    radius_1 -= 1
    radius_2 += 1


