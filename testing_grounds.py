import time
import turtle
test = turtle.Turtle()
test.fd(107)
if test.pos()[0] > 7:
    print('yellow')
print(test.pos()[0])

turtle.done()