#1700011605#
import turtle
import math
p=math.pi
turtle.speed(0)
Saturn=turtle.Pen()
Jupiter=turtle.Pen()
Mars=turtle.Pen()
Earth=turtle.Pen()
Venus=turtle.Pen()
Mercury=turtle.Pen()

Saturn.penup()
Saturn.goto(290,0)
Saturn.pendown()
Saturn.color('purple')

Jupiter.penup()
Jupiter.goto(300,0)
Jupiter.pendown()
Jupiter.color('yellow')

Mars.penup()
Mars.goto(180,0)
Mars.pendown()

Earth.penup()
Earth.goto(170,0)
Earth.pendown()
Earth.color('red')


Venus.penup()
Venus.goto(100,0)
Venus.pendown()
Venus.color('green')

Mercury.penup()
Mercury.goto(20,0)
Mercury.pendown()
Mercury.color('blue')

for i in range(0,721):    
    Saturn.goto(300*math.cos(0.9*i*p/360)-10,180*math.sin(0.9*i*p/360))
    Jupiter.goto(250*math.cos(1.2*i*p/360)+50,150*math.sin(1.2*i*p/360))
    Mars.goto(200*math.cos(1.5*i*p/360)-20,120*math.sin(1.5*i*p/360))
    Earth.goto(150*math.cos(1.75*i*p/360)+20,90*math.sin(1.75*i*p/360))
    Venus.goto(100*math.cos(2*i*p/360),60*math.sin(2*i*p/360))
    Mercury.goto(50*math.cos(2.5*i*p/360)-30,30*math.sin(2.5*i*p/360))

#Let's go#
