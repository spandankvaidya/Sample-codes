# printing multicolored star shape using turtle
# Created by: Spandan Vaidya, Date:24-03-2023
import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.shape('turtle')
s.bgcolor('light pink')

colors=['blue','red','green','yellow','maroon']#array for colors
j=0#colors array variable
t.left(72)#setting initial direction for turtle

for i in range(5):
    t.color(colors[j])
    j+=1
    t.forward(200)
    t.right(144)
turtle.done()
