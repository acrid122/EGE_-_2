from turtle import *
tracer(0)
lt(90)
m = 10
screensize(6000, 6000)
for _ in range(3):
    fd(39 * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
lt(90)
down()
for _ in range(3):
    fd(29 * m)
    rt(90)
    
    bk(18 * m)
    rt(90)
update()
done()