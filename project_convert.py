import pandas as pd
from datetime import datetime,date
ag=pd.read_csv('agrin.csv')
print(ag.info())
s=[]
s1=[]
i=0
c=0
q=[]
g=[]
c1=0
d = ag['Date'][0]

def fun(p,l,m):
    global s,c,q
    t1=datetime.strptime(p,"%X")
    t2=t1.time()
    s.append(t2)
    c=c+1
    if(m=='OFF'):
            z = datetime.strptime(p, "%X")
            b = z.time()
            m=datetime.combine(date.today(), b) - datetime.combine(date.today(), s[0])
            print(m)
            q.append(m.seconds)
            c=c-1
            s=[]

d=ag['Date'][0]
for i in ag.index:
    #print(i)
    p=ag['Time'][i]
    l=ag['Date'][i]
    m=ag['Water Pump ON/OFF'][i]
    if l == d:
        fun(p,l,m)
    else:
        res = (sum(q) / len(q)).__round__()
        g.append(res)
        s1.append(c)
        q=[]
        d=l
        c=0
        fun(p,d,m)

res = (sum(q) / len(q)).__round__()
g.append(res)
#print(g)
s1.append(c)
#print(s1)

a=ag.groupby('Date').agg({'Water Level':['mean'],'Humidity ':['mean'],'Temperature':['mean'],'Ph':['mean']})
x=pd.DataFrame(a)
x.columns=['Soil Moisture Mean(%)' ,'Humidity Mean(%)','Temperature Mean(C)','Ph Mean']

y=x.round(3)
y['Avg Motor Running Time in seconds']=g
print(y)

o=y['Avg Motor Running Time in seconds']//60
p=y['Avg Motor Running Time in seconds']%60
def func(r):
    if r<10:
        r=r/10
        return r
    else:
        r=r/100
        return r
a1=list(map(lambda num:func(num), p))
o=o+a1
print(o)
y['Avg Motor Running Time in minutes']=o
print(y)
y['Number of times motor switched ON']=s1
y.to_csv('precision.csv')