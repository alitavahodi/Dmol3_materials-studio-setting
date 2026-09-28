import matplotlib.pyplot as plt 
import csv 

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\pristine DOS.csv" , "r") as z:
    reader=csv.reader(z)
    a=[]
    b=[]
    for row in reader:
        a.append(float(row[0]))
        b.append(float(row[1]))
z.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\Fe DOS.csv" , "r") as y:
    reader=csv.reader(y)
    c=[]
    d=[]
    for row in reader:
        c.append(float(row[0]))
        d.append(float(row[1])+30)
y.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\C1 DOS.csv" , "r") as x:
    reader=csv.reader(x)
    e=[]
    f=[]
    for row in reader:
        e.append(float(row[0]))
        f.append(float(row[1])+60)
x.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\C2 DOS.csv" , "r") as w:
    reader=csv.reader(w)
    g=[]
    h=[]
    for row in reader:
        g.append(float(row[0]))
        h.append(float(row[1])+80)
w.close

with open("D:\\BOOKS & Notes\\پایان نامه\\2024 BNNT\\Article\\DOS\\5.5\\C3 DOS.csv" , "r") as v:
    reader=csv.reader(v)
    i=[]
    j=[]
    for row in reader:
        i.append(float(row[0]))
        j.append(float(row[1])+110)
v.close



plt.figure(figsize=(5,5))

plt.plot(a,b,label='Pristine')
plt.plot(c,d,label='Fe doped')
plt.plot(e,f,label='C1')
plt.plot(g,h,label='C2')
plt.plot(i,j,label='C3')


plt.title('(5,5) BNNT')
plt.xticks([-14,-12,-10,-8,-6,-4,-2,0,2,4],fontsize=6)
plt.yticks([])
plt.xlabel('Energy(eV)')
plt.ylabel('Density of States, (DOS)')
plt.legend(loc='upper right',fontsize=8)

plt.grid(False)
plt.show()