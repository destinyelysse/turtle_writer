# fd(100) / bk(100) moves it forward or backward 100 px
# lt(90) and rt(90) turn it left or right 90 degrees
# pu picks up the pen; pd puts it down, drawing where the turtle moves

# set up turtle
import turtle

screen = turtle.getscreen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

# turtle functions
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def hello(t):
    t.pu()
    t.bk(500)
    # H
    t.pd()
    t.lt(90)
    t.fd(100)
    t.pu()
    t.bk(50)
    t.rt(90)
    t.pd()
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.bk(100)
    t.rt(90)
    t.pu()
    t.fd(10)
    # E
    t.lt(90)
    t.pd()
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pd()
    t.fd(50)
    t.pu()
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pd()
    t.fd(50)
    t.pu()
    t.fd(10)
    # L
    t.pd()
    t.lt(90)
    t.fd(100)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.fd(10)
    # L
    t.pd()
    t.lt(90)
    t.fd(100)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.fd(10)
    # O
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(180)
    t.pu()
    t.fd(60)


# turtle directions
hello(my_turtle)

# finish
turtle.done()