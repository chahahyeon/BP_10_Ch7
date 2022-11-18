#1번 문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("black", "white")
s = turtle.Screen(); s.bgcolor('skyblue');

def draw_snowman(x, y):
 t.up()
 t.goto(x, y)
 t.down()
 t.begin_fill()
 t.circle(20)
 t.end_fill()
 t.goto(x, y-25)
 t.setheading(135)
 t.forward(50)
 t.backward(50)
 t.setheading(30)
 t.forward(50)
 t.backward(50)
 t.setheading(0)
 t.begin_fill()
 t.circle(15)
 t.end_fill()
 t.goto(x, y-70)
 t.begin_fill()
 t.circle(30)
 t.end_fill()
draw_snowman(0, 0)
draw_snowman(100, 0)
draw_snowman(200, 0)


#2번문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def hexagon():
 for i in range(6):
  turtle.forward(100)
  turtle.left(360/6)

for i in range (6):
 hexagon()
 turtle.forward(100)
 turtle.right(60)

#3번문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def f(x):
 return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
 t.goto(x, int(0.01*f(x)))

#4번문제
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_line():
 t.forward(100)
 t.backward(100)

for x in range(12):
 t.right(30)
 draw_line()
