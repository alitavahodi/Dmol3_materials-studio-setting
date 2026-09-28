import matplotlib.pyplot as plt 
import csv 

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\5.5pristine.csv" , "r") as z:
    reader=csv.reader(z)
    a=[]
    b=[]
    for row in reader:
        a.append(float(row[0]))
        b.append(float(row[1]))
z.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\5.5Fe.csv" , "r") as y:
    reader=csv.reader(y)
    c=[]
    d=[]
    for row in reader:
        c.append(float(row[0]))
        d.append(float(row[1]))
y.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\5.5S C1.csv" , "r") as x:
    reader=csv.reader(x)
    e=[]
    f=[]
    for row in reader:
        e.append(float(row[0]))
        f.append(float(row[1]))
x.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\5.5S C2.csv" , "r") as w:
    reader=csv.reader(w)
    g=[]
    h=[]
    for row in reader:
        g.append(float(row[0]))
        h.append(float(row[1]))
w.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\sigma profile\\5.5S C3.csv" , "r") as v:
    reader=csv.reader(v)
    i=[]
    j=[]
    for row in reader:
        i.append(float(row[0]))
        j.append(float(row[1]))
v.close



plt.figure(figsize=(8,8))

plt.plot(a,b,label='Pristine')
plt.plot(c,d,label='Fe doped')
plt.plot(e,f,label='C1')
plt.plot(g,h,label='C2')
plt.plot(i,j,label='C3')


#plt.title('(6,6) BNNT')
#plt.xticks([-14,-12,-10,-8,-6,-4,-2,0,2,4],fontsize=6)
#plt.yticks([])
plt.xlabel('Screening Charge Density, σ(e/Å^2)')
plt.ylabel('Sigma profile, P(σ)')
plt.legend(loc='upper right',fontsize=8)

plt.grid(False)
plt.show()