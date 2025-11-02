import csv, math

def f(a):
    t=[]
    for i in a:
        if float(i[1])>25:
            t.append(float(i[1])*1.8+32)
        else:
            t.append(float(i[1]))
    return t

def g(a):
    s=0
    for i in a:
        s+=i
    return s


r=open('./../../../data/weather_data.csv')
d=list(csv.reader(r))
r.close()
d=d[1:]
x=[]
for i in d:
    x.append([i[0],i[1],i[2],i[3],i[4]])
y=f(x)
z=g(y)
print('sum',z)
print('avg',z/(len(y) if len(y) else 1))
ws=0
for i in d:
    u=float(i[3]); v=float(i[4])
    ws+=math.sqrt(u*u+v*v)
print('wind',ws/len(d))
