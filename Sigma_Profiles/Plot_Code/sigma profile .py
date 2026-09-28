import matplotlib.pyplot as plt 
import numpy as np
import csv 

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\G1.csv" , "r") as z:
    reader=csv.reader(z)
    a=[]
    b=[]
    for row in reader:
        a.append(float(row[0]))
        b.append(float(row[1]))
z.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\G2.csv" , "r") as y:
    reader=csv.reader(y)
    c=[]
    d=[]
    for row in reader:
        c.append(float(row[0]))
        d.append(float(row[1]))
y.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\G3.csv" , "r") as x:
    reader=csv.reader(x)
    e=[]
    f=[]
    for row in reader:
        e.append(float(row[0]))
        f.append(float(row[1]))
x.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\7.7S C2.csv" , "r") as w:
    reader=csv.reader(w)
    g=[]
    h=[]
    for row in reader:
        g.append(float(row[0]))
        h.append(float(row[1]))
w.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\7.7S C3.csv" , "r") as v:
    reader=csv.reader(v)
    i=[]
    j=[]
    for row in reader:
        i.append(float(row[0]))
        j.append(float(row[1]))
v.close



plt.figure(figsize=(8,8))

plt.plot(a,b,label='G1')
plt.plot(c,d,label='G2')
plt.plot(e,f,label='G3')
#plt.plot(g,h,label='C2')
#plt.plot(i,j,label='C3')


x1=[-0.0075,-0.0075]
y1=[0,100]
x2=[+0.0075,+0.0075]
y2=[0,100]
y=[0,0]
x=[-0.02,+0.02]
#plt.plot(x1,y1,'k--')
#plt.plot(x2,y2,'k--')
plt.plot(x,y,'k--')



#plt.title('(6,6) BNNT')
plt.xticks(np.arange(-0.02,+0.02,0.005))
#plt.yticks([])
plt.xlabel('Screening Charge Density, σ(e/Å  )')
plt.ylabel('Sigma profile, P(σ)')
plt.legend(loc='upper right',fontsize=8)



plt.grid(False)
plt.show()