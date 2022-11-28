from turtle import *

speed(10)
#house
begin_fill()
width(7)
color("green")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()


#door
forward(70)
color("black")
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
penup()
goto(200, 200)
pendown()


#roof
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows
begin_fill()
color("pink")
penup()
goto(0,60)
pendown()
left(120)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()


penup()
goto(200,60)
begin_fill()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

exitonclick()