from turtle import * # import turtle module

speed('fastest')     # set turtle speed

side = 10
size = 50

# create a hexagon
for i in range(side):
    fd(size)
    lt(360/side)
    write(i)           

hideturtle()        # hide turtle
mainloop()          # keep window open
