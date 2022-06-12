import turtle

turtle.getscreen()
t=turtle.Turtle()
turtle.bgcolor("yellow")
#circle_hexagon
t.circle(50, steps=6)
t.penup()
t.fd(100)
t.pendown()
t.pensize(4)
t.pencolor('blue')

#whileloop_hexagon
s=0
while (s<=6):
    t.fd(50)
    t.lt(60)
    s=s+1

t.penup()
t.goto(0,0)
t.pendown()
t.pensize(2)

#concentric_circles
for i in range (10, 70, 10):
    t.circle(i)
    t.penup()
    t.goto(0,-i*2)
    t.pendown()
    i=i+10
Turtle.mainloop()


