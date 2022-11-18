#1번 문제
import turtle     #터틀 라이브러리를 가져옴
t = turtle.Turtle()     #turtle을 t로 대체하기
t.shape("turtle") #모양을 거북이로 설정
t.color("black", "white")
s = turtle.Screen(); s.bgcolor('skyblue');

def draw_snowman(x, y):
 t.up()       #거북이가 이동할 때 선 생기지 않음
 t.goto(x, y)  #좌표 (x, y) 이동
 t.down()     #거북이 이동할 때 선 생김
 t.begin_fill()    #도형안에 색깔을 칠하기 위해 준비
 t.circle(20)   #반지름이 20인 원을 그린다
 t.end_fill()    #도형 안에 색깔 칠하고 종료
 t.goto(x, y-25)   #좌표 (x, y-25) 이동
 t.setheading(135)   #커서를 135도로 바꿈
 t.forward(50)   #50만큼 전진
 t.backward(50)  #50만큼 뒤로 이동
 t.setheading(30)    #커서를 30도로 바꿈
 t.forward(50)   #50만큼 전진
 t.backward(50)   #50만큼 뒤로 이동
 t.setheading(0)    #커서를 0도로 바꿈
 t.begin_fill()    #도형안에 색깔을 칠하기 위해 준비
 t.circle(15)    #반지름이 15인 원을 그린다
 t.end_fill()    #도형 안에 색깔 칠하고 종료
 t.goto(x, y-70)    #좌표 (x, y-70) 이동
 t.begin_fill()    #도형안에 색깔을 칠하기 위해 준비
 t.circle(30)      #반지름이 30인 원을 그린다
 t.end_fill()     #도형 안에 색깔 칠하고 종료
draw_snowman(0, 0)
draw_snowman(100, 0)
draw_snowman(200, 0)


#2번문제
import turtle    #터틀 라이브러리를 가져옴
t = turtle.Turtle()    #turtle을 t로 대체하기
t.shape("turtle")    #모양을 거북이로 바꿈
t.speed(0)    #거북이 속도를 0으로 바꿈

def hexagon():
 for i in range(6):  #6번 반복
  turtle.forward(100)   #100만큼 전진
  turtle.left(360/6)    #왼쪽으로 360/6도 회전

for i in range (6):  #6번 바본
 hexagon()
 turtle.forward(100)  #100만큼 전진
 turtle.right(60)     #오른쪽으로 60도 회전

#3번문제
import turtle      #터틀 라이브러리를 가져옴
t = turtle.Turtle()
t.shape("turtle")      #모양을 거북이로 바꿈
t.speed(0)         #거북이 속도를 0으로 바꿈

def f(x):
 return x**2+1

t.goto(200, 0)    #좌표(200,0)으로 이동
t.goto(0, 0)      #좌표(0,0)으로 이동
t.goto(0, 200)    #좌표(0,200)으로 이동
t.goto(0, 0)      #좌표(0,0)으로 이동

for x in range(150):   #150번 
 t.goto(x, int(0.01*f(x)))

#4번문제
import turtle     #터틀 라이브러리를 가져옴
t = turtle.Turtle()          #turtle을 t로 대체하기
t.shape("turtle")     #모양을 거북이로 바꿈
t.speed(0)      #거북이 속도를 0으로 바꿈

def draw_line():
 t.forward(100)        #100만큼 전진
 t.backward(100)      #100만큼 뒤로 이동

for x in range(12):
 t.right(30)         #오른쪽으로 30도 회전
 draw_line()
