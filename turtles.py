# fd(100) / bk(100) moves it forward or backward 100 px
# lt(90) and rt(90) turn it left or right 90 degrees
# pu picks up the pen; pd puts it down, drawing where the turtle moves

# set up turtle
import turtle

screen = turtle.getscreen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

# turtle functions
def draw_square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def write_hello(t):
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

def write_letter_a(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(60)
    
def write_letter_b(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.fd(10)
    t.rt(90)
    t.fd(50)
    t.lt(90)

def write_letter_c(t):
    t.pd()
    t.fd(50)
    t.bk(50)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(10)

def write_letter_d(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(46)
    t.rt(30)
    t.fd(5)
    t.rt(60)
    t.fd(94)
    t.rt(30)
    t.fd(5)
    t.rt(60)
    t.fd(46)
    t.rt(180)
    t.pu()
    t.fd(60)

def write_letter_e(t):
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

def write_letter_f(t):
    t.lt(90)
    t.pd()
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.bk(50)
    t.rt(90)
    t.pu()
    t.fd(50)
    t.lt(90)
    t.fd(60)

def write_letter_g(t):
    t.pd()
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(25)
    t.bk(25)
    t.pu()
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.pd()
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(10)

def write_letter_h(t):
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

def write_letter_i(t):
    t.pd()
    t.fd(50)
    t.bk(25)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(25)
    t.bk(50)
    t.pu()
    t.fd(60)
    t.rt(90)
    t.fd(100)
    t.lt(90)

def write_letter_j(t):
    t.pd()
    t.lt(90)
    t.fd(50)
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    t.pu()
    t.bk(100)
    t.rt(90)
    t.fd(10)

def write_letter_k(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.bk(50)
    t.rt(45)
    t.fd(62)
    t.bk(62)
    t.rt(90)
    t.fd(62)
    t.bk(62)
    t.rt(45)
    t.fd(50)
    t.pu()
    t.lt(90)
    t.fd(60)

def write_letter_l(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.fd(10)

def write_letter_m(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(135)
    t.fd(35)
    t.bk(35)
    t.rt(45)
    t.fd(100)
    t.lt(90)
    t.pu()
    t.fd(50)
    t.lt(90)
    t.pd()
    t.fd(100)
    t.lt(135)
    t.fd(35)
    t.bk(35)
    t.lt(45)
    t.pu()
    t.fd(100)
    t.lt(90)
    t.fd(10)

def write_letter_n(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(154)
    t.fd(113)
    t.bk(113)
    t.rt(26)
    t.fd(100)
    t.lt(90)
    t.pu()
    t.fd(50)
    t.lt(90)
    t.pd()
    t.fd(100)
    t.pu()
    t.bk(100)
    t.rt(90)
    t.fd(10)

def write_letter_o(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.rt(180)
    t.fd(60)


def write_letter_p(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.pu()
    t.bk(50)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(10)

def write_letter_q(t):
    t.pd()
    t.fd(50)
    t.bk(50)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(135)
    t.fd(35)
    t.bk(35)
    t.rt(135)
    t.pu()
    t.fd(10)

def write_letter_r(t):
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.lt(135)
    t.fd(65)
    t.pu()
    t.bk(65)
    t.rt(45)
    t.fd(50)
    t.lt(90)
    t.fd(60)
    

def write_letter_s(t):
    t.pd()
    t.lt(90)
    t.fd(25)
    t.bk(25)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(25)
    t.pu()
    t.fd(75)
    t.lt(90)
    t.fd(10)


def write_letter_t(t):
    t.fd(25)
    t.pd()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.bk(25)
    t.fd(50)
    t.pu()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(10)

def write_letter_u(t):
    t.lt(90)
    t.pd()
    t.fd(100)
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    t.pu()
    t.bk(100)
    t.rt(90)
    t.fd(10)

def write_letter_v(t):
    t.lt(90)
    t.fd(100)
    t.rt(165)
    t.pd()
    t.fd(100)
    t.bk(100)
    t.pu()
    t.lt(75)
    t.fd(50)
    t.rt(104)
    t.pd()
    t.fd(100)
    t.bk(100)
    t.pu()
    t.lt(14)
    t.fd(100)
    t.lt(90)
    t.fd(10)


def write_letter_w(t):
    t.lt(90)
    t.fd(100)
    t.pd()
    t.rt(175)
    t.fd(100)
    t.lt(125)
    t.fd(25)
    t.rt(80)
    t.fd(25)
    t.lt(125)
    t.fd(100)
    t.pu()
    t.bk(100)
    t.rt(125)
    t.bk(25)
    t.lt(80)
    t.bk(25)
    t.rt(125)
    t.bk(100)
    t.lt(175)
    t.bk(100)
    t.rt(90)
    t.fd(60)



def write_letter_x(t):
    t.lt(65)
    t.pd()
    t.fd(112)
    t.bk(112)
    t.rt(65)
    t.pu()
    t.fd(50)
    t.pd()
    t.lt(115)
    t.fd(112)
    t.bk(112)
    t.rt(115)
    t.pu()
    t.fd(10)


def write_letter_y(t):
    t.fd(25)
    t.pd()
    t.lt(90)
    t.fd(50)
    t.lt(35)
    t.fd(55)
    t.bk(55)
    t.rt(70)
    t.fd(55)
    t.bk(55)
    t.rt(145)
    t.fd(50)
    t.pu()
    t.lt(90)
    t.fd(35)

def write_letter_z(t):
    t.pd()
    t.fd(50)
    t.lt(115)
    t.fd(110)
    t.rt(115)
    t.fd(50)
    t.pu()
    t.bk(50)
    t.lt(115)
    t.bk(110)
    t.rt(115)
    t.fd(10)

def write_space(t):
    t.pu()
    t.fd(60)


# turtle directions
write_letter_d(my_turtle)
write_letter_e(my_turtle)
write_letter_s(my_turtle)
write_letter_t(my_turtle)
write_letter_i(my_turtle)
write_letter_n(my_turtle)
write_letter_y(my_turtle)



# finish
turtle.done()