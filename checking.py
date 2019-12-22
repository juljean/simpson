x=[]
y=[]
new=3
b=5
N=10
dx=(b-new)/N
for el in range (N+1):
    new=new+dx
    y.append((new**2+3*new-2)**0.5)
    x.append(new)
print(x)
print(y)
y_first= y[0:-1:2]
y_four=y[1::2]
y_two=y[2::2]
print(y_first)#all evens without last
print(y_four)#odds
print(y_two)#all evens without first
count=0
for i in y_first:
    count=count+1
for i in y_two:
    count=count+i
for i in y_four:
    fourth=i+fourth
