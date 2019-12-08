#GITHUB CALENDER (WEEKLY)
#AMLAN SAHA KUNDU

import turtle

#col = ["ffffff","58d68d","2ecc71","28b463","239b56","1d8348","186a3b"] GREEN(82e0aa)
#col = ["ffffff","81d4fa","4fc3f7","29b6f6","03a9f4","039be5","01579b"] BLUE(85C1E9)
#col = ["ffffff","ec7063","e74c3c","cb4335","b03a2e","943126","78281f"] RED(f1984a)

x1 = -200
y1 = 200
side = 20
#=======================================================================
csv = open(".CSV location")
d = []
h = []
for col in csv:
    d.append(col.split(',')[0])
    h.append(col.split(',')[1])
day = d[1:]
hour = h[1:]

#print(day)
#print(hour)

#========================================================================

col = ["ffffff","81d4fa","4fc3f7","29b6f6","03a9f4","039be5","01579b"]
n = len(day)


l = []
for c in range (n):
    d = c+1
    st = hour[c]
    l.append(st)

t = turtle.Turtle()
t.ht()
x= x1
y= y1
t.penup()
t.goto(x,y)

for j in range(1,n+1):
    k = int(l[j-1])
    if k == 0:
        q = 0
    elif k>=10:
        q=6
    else :
        q = k//2+1
    t.begin_fill()
    for i in range(4):
        t.pendown()
        t.fillcolor('#'+col[q])
        t.forward(side)
        t.right(90)
        t.penup()
    t.end_fill()
    if j%7==0:
        q = x
        r = y
        t.goto(q,(r-40))
        t.write(j)
        x += int(side+5)
        y = y1
        
        
    else:
        y -=int(side+5)
    t.goto(x,y)

cv = turtle.getcanvas()
cv.postscript(file=".ps location", colormode='color')

turtle.done()



