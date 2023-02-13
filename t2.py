from turtle import *

speed('fastest')
pencolor('green')

gap = 3
angle = 32
for i in range(100):
    fd(i*gap)
    lt(angle)

hideturtle()
mainloop()
