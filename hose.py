from turtle import *

#we want to paint a hous
#step 1: draw a square
width(7)
speed(30)
color ("purple")
forward (200)
left(90)

forward (200)
left (90)

forward (200)
left (90)

forward(200)
left(90)
#end of square

#drowing a door

forward (70)
color ("yellow")
left (90)
forward (120)
right(90)
forward (60)
right(90)
forward(120)

penup()
goto (200, 200)
pendown ( )

color("red" )
right (150)
forward(200)
left (120)
forward(200)

#paint window

penup()
goto (70, 230)
pendown ( )

color("red" )
right (150)
forward (50)
right (90)
forward (60)
right(90)
forward (50)
right (90)
forward(60)



penup()
goto (230, 50)
pendown ( )
color ("black")
right (180)
write ("First_Code_in_my_life")


exitonclick()
